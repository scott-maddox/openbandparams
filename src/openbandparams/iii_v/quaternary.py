#
#   Copyright (c) 2013-2014, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

# std lib imports

# third party imports

# local imports
from openbandparams.base_material import AlloyBase
from openbandparams.utils import classinstancemethod
from openbandparams.algorithms import bisect

class Quaternary1or2Type(type):
    def __getattr__(self, name):
        # acts like a class method for Quaternary.__getattr__
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)

class Quaternary1Type(Quaternary1or2Type):
    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        return "{A}{B}_{{x}}{C}_{{y}}{D}_{{1-x-y}}".format(
                                              A=e1, B=e2, C=e3, D=e4)

class Quaternary2Type(Quaternary1or2Type):
    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        return "{A}_{{x}}{B}_{{y}}{C}_{{1-x-y}}{D}".format(
                                              A=e1, B=e2, C=e3, D=e4)

class Quaternary3Type(type):
    def __getattr__(self, name):
        # acts like a class method for Quaternary3.__getattr__
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name) and
            hasattr(self.ternary4, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)
    
    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        return "{A}_{{x}}{B}_{{1-x}}{C}_{{y}}{D}_{{1-y}}".format(
                                              A=e1, B=e2, C=e3, D=e4)

class Quaternary(AlloyBase):
    @classinstancemethod
    def Eg(self, cls, **kwargs):
        '''
        Returns the bandgap, Eg, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return min(self.Eg_Gamma(T=T), self.Eg_X(T=T), self.Eg_L(T=T))
        else:
            x = cls._get_x(kwargs)
            y = cls._get_y(kwargs)
            T = cls._get_T(kwargs)
            return min(cls.Eg_Gamma(x=x, y=y, T=T), cls.Eg_X(x=x, y=y, T=T),
                       cls.Eg_L(x=x, y=y, T=T))
    
    def __eq__(self, other):
        return (type(self) == type(other) and
                self._x == other._x and
                self._y == other._y)

class Quaternary1or2(Quaternary):
    '''
    For alloys of the AB_{x}C_{y}D_{1-x-y} and A_{x}B_{y}C_{1-x-y}D types [1].
    These require only three ternaries for interpolation.
    
    [1] C. K. Williams, T. H. Glisson, J. R. Hauser, and M. A. Littlejohn,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys of the form Ax By Cz D or A Bx Cy Dz," JEM, vol. 7, no. 5,
    pp. 639-646, Sep. 1978.
    '''
    
    def __init__(self, **kwargs):
        Quaternary.__init__(self)
        self._x, self._y, self._z = self._get_xyz(kwargs)

    def __getattr__(self, name):
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)
    
    @classmethod
    def _validate_xyz(cls, x, y, z):
        assert x >= 0. and x <= 1.
        assert y >= 0. and y <= 1.
        assert z >= 0. and z <= 1.
        
    @classmethod
    def _get_xyz(cls, kwargs):
        if cls._has_x(kwargs) and cls._has_y(kwargs):
            x = cls._get_x(kwargs)
            y = cls._get_y(kwargs)
            z = round(1 - x - y, 6)
        elif cls._has_x(kwargs) and cls._has_z(kwargs):
            x = cls._get_x(kwargs)
            z = cls._get_z(kwargs)
            y = round(1 - x - z, 6)
        elif cls._has_y(kwargs) and cls._has_z(kwargs):
            y = cls._get_y(kwargs)
            z = cls._get_z(kwargs)
            x = round(1 - y - z, 6)
        elif 'a' in kwargs and 'T' in kwargs and cls._has_x(kwargs):
            x, y, z = cls._lattice_match(kwargs['a'], kwargs['T'],
                                         x=cls._get_x(kwargs))
        elif 'a' in kwargs and 'T' in kwargs and cls._has_y(kwargs):
            x, y, z = cls._lattice_match(kwargs['a'], kwargs['T'],
                                         y=cls._get_y(kwargs))
        elif 'a' in kwargs and 'T' in kwargs and cls._has_z(kwargs):
            x, y, z = cls._lattice_match(kwargs['a'], kwargs['T'],
                                         z=cls._get_z(kwargs))
        else:
            raise TypeError(
                "Missing required key word argument.\n"+cls._get_usage())
        cls._validate_xyz(x, y, z)
        return x, y, z
    
    @classmethod
    def _lattice_match(cls, a, T, x=None, y=None, z=None):
        if x is not None:
            # make sure the lattice constant is in range
            a1 = cls.a(x=x, y=0, T=T)
            a2 = cls.a(x=x, y=(1-x), T=T)
            amin = min(a1, a2)
            amax = max(a1, a2)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]'%(amin, amax))
            # find the correct y composition
            y = bisect(func=lambda y: cls.a(x=x, y=y, T=T) - a, a=0, b=(1-x))
            z = round(1 - x - y, 6)
            return x, y, z
        elif y is not None:
            # make sure the lattice constant is in range
            a1 = cls.a(x=0, y=y, T=T)
            a2 = cls.a(x=(1-y), y=y, T=T)
            amin = min(a1, a2)
            amax = max(a1, a2)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]'%(amin, amax))
            # find the correct y composition
            x = bisect(func=lambda x: cls.a(x=x, y=y, T=T) - a, a=0, b=(1-y))
            z = round(1 - x - y, 6)
            return x, y, z
        elif z is not None:
            # make sure the lattice constant is in range
            a1 = cls.a(x=0, z=z, T=T)
            a2 = cls.a(x=(1-z), z=z, T=T)
            amin = min(a1, a2)
            amax = max(a1, a2)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]'%(amin, amax))
            # find the correct y composition
            x = bisect(func=lambda x: cls.a(x=x, z=z, T=T) - a, a=0, b=(1-z))
            y = round(1 - x - z, 6)
            return x, y, z
        else:
            raise ValueError('Need x, y or z')

    @classinstancemethod
    def _interpolate(self, cls, param, **kwargs):
        if self is not None:
            x = self._x
            y = self._y
            z = self._z
        else:
            x, y, z = cls._get_xyz(kwargs)
            
        vals = []
        for t in [cls.ternary1, cls.ternary2, cls.ternary3]:
            try:
                vals.append(getattr(t, param))
            except AttributeError as e:
                e.message +='. Ternary `%s`'%t.name
                e.message +=' missing param `%s`'%param
                raise e
        if param[0] == '_':
            # assume it's a hard coded parameter if it starts with '_'
            t12 = vals[0]
            t13 = vals[1]
            t23 = vals[2]
        else:
            # otherwise it's an accessor function.
            # See the reference in this class's docstring for more
            # information about the interpolation method.
            u = ( 1. + x - y ) / 2.
            v = ( 1. + y - z ) / 2.
            w = ( 1. + x - z ) / 2.
            new_kwargs = dict(kwargs)
            new_kwargs['x'] = u
            t12 = vals[0](**new_kwargs)
            new_kwargs['x'] = w
            t13 = vals[1](**new_kwargs)
            new_kwargs['x'] = v
            t23 = vals[2](**new_kwargs)
        weight12 = x*y
        weight13 = x*z
        weight23 = y*z
        denom = weight12 + weight13 + weight23
        if denom == 0.:
            # handle this explicitly, so there's no divide by zero
            if x == 0.:
                return t23
            else:
                return t13
        else:
            num = weight12*t12 + weight13*t13 + weight23*t23
            return num / denom

# Type 1: AB_{x}C_{y}D_{1-x-y}
# binary1 = AB
# binary2 = AC
# binary3 = AD
# ternary1 = t12
# ternary2 = t13
# ternary3 = t23
class Quaternary1(Quaternary1or2):
    '''
    For alloys of the AB_{x}C_{y}D_{1-x-y} type [1], where A is the only
    Group III element. These require only three ternaries for interpolation.
    
    [1] C. K. Williams, T. H. Glisson, J. R. Hauser, and M. A. Littlejohn,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys of the form Ax By Cz D or A Bx Cy Dz," JEM, vol. 7, no. 5,
    pp. 639-646, Sep. 1978.
    '''
    __metaclass__ = Quaternary1Type

    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f2 = self.elementFraction(e2)
        f3 = self.elementFraction(e3)
        f4 = self.elementFraction(e4)
        return "{A}{B}_{{{:g}}}{C}_{{{:g}}}{D}_{{{:g}}}".format(
                                              f2, f3, f4,
                                              A=e1, B=e2, C=e3, D=e4)
    def __repr__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f2 = self.elementFraction(e2)
        f3 = self.elementFraction(e3)
        return "{A}{B}{C}{D}({B}={:g}, {C}={:g})".format(f2, f3,
                                                 A=e1, B=e2, C=e3, D=e4)
    
    @classmethod
    def _has_x(cls, kwargs):
        '''Returns True if x is explicitly defined in kwargs'''
        return ('x' in kwargs) or (cls.element2 in kwargs)
    
    @classmethod
    def _get_x(cls, kwargs):
        '''
        Returns x if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'x' in kwargs:
            return round(float(kwargs['x']), 6)
        elif cls.element2 in kwargs:
            return round(float(kwargs[cls.element2]), 6)
        else:
            raise TypeError("Neither 'x' nor '{}' are in kwargs"
                            "".format(cls.element2))
    
    @classmethod
    def _has_y(cls, kwargs):
        '''Returns True if y is explicitly defined in kwargs'''
        return ('y' in kwargs) or (cls.element3 in kwargs)
    
    @classmethod
    def _get_y(cls, kwargs):
        '''
        Returns y if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'y' in kwargs:
            return round(float(kwargs['y']), 6)
        elif cls.element3 in kwargs:
            return round(float(kwargs[cls.element3]), 6)
        else:
            raise TypeError("Neither 'y' nor '{}' are in kwargs"
                            "".format(cls.element3))
    
    @classmethod
    def _has_z(cls, kwargs):
        '''Returns True if z is explicitly defined in kwargs'''
        return ('z' in kwargs) or (cls.element4 in kwargs)
    
    @classmethod
    def _get_z(cls, kwargs):
        '''
        Returns z if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'z' in kwargs:
            return round(float(kwargs['z']), 6)
        elif cls.element4 in kwargs:
            return round(float(kwargs[cls.element4]), 6)
        else:
            raise TypeError("Neither 'z' nor '{}' are in kwargs"
                            "".format(cls.element4))
    
    @classmethod
    def _get_usage(cls):
        return ("The  supported kwarg combinations are as follows:"
                "\n    - ('x' or '{2}') and ('y' or '{3}')"
                "\n    - ('x' or '{2}') and ('z' or '{4}')"
                "\n    - ('y' or '{3}') and ('z' or '{4}')"
                "\n    - 'a' and 'T' and ('x' or '{2}')"
                "\n    - 'a' and 'T' and ('y' or '{3}')"
                "\n    - 'a' and 'T' and ('z' or '{4}')"
                            "".format(None, cls.element1, cls.element2,
                                            cls.element3, cls.element4))

    @classinstancemethod
    def elementFraction(self, cls, element):
        # AB_{x}C_{y}D_{1-x-y}
        if element == cls.element1:
            return 1
        elif element == cls.element2:
            return self._x
        elif element == cls.element3:
            return self._y
        elif element == cls.element4:
            return self._z
        else:
            return 0

# Type 2: A_{x}B_{y}C_{1-x-y}D
# binary1 = AD
# binary2 = BD
# binary3 = CD
# ternary1 = ABD
# ternary2 = ACD
# ternary3 = BCD
class Quaternary2(Quaternary1or2):
    '''
    For alloys of the A_{x}B_{y}C_{1-x-y}D type [1], where D is the only
    Group V element. These require only three ternaries for interpolation.
    
    [1] C. K. Williams, T. H. Glisson, J. R. Hauser, and M. A. Littlejohn,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys of the form Ax By Cz D or A Bx Cy Dz," JEM, vol. 7, no. 5,
    pp. 639-646, Sep. 1978.
    '''
    __metaclass__ = Quaternary2Type

    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f1 = self.elementFraction(e1)
        f2 = self.elementFraction(e2)
        f3 = self.elementFraction(e3)
        return "{A}_{{{:g}}}{B}_{{{:g}}}{C}_{{{:g}}}{D}".format(
                                              f1, f2, f3,
                                              A=e1, B=e2, C=e3, D=e4)
    def __repr__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f1 = self.elementFraction(e1)
        f2 = self.elementFraction(e2)
        return "{A}{B}{C}{D}({A}={:g}, {B}={:g})".format(f1, f2,
                                                 A=e1, B=e2, C=e3, D=e4)
    
    @classmethod
    def _has_x(cls, kwargs):
        '''Returns True if x is explicitly defined in kwargs'''
        return ('x' in kwargs) or (cls.element1 in kwargs)
    
    @classmethod
    def _get_x(cls, kwargs):
        '''
        Returns x if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'x' in kwargs:
            return round(float(kwargs['x']), 6)
        elif cls.element1 in kwargs:
            return round(float(kwargs[cls.element1]), 6)
        else:
            raise TypeError("Neither 'x' nor '{}' are in kwargs"
                            "".format(cls.element1))
    
    @classmethod
    def _has_y(cls, kwargs):
        '''Returns True if y is explicitly defined in kwargs'''
        return ('y' in kwargs) or (cls.element2 in kwargs)
    
    @classmethod
    def _get_y(cls, kwargs):
        '''
        Returns y if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'y' in kwargs:
            return round(float(kwargs['y']), 6)
        elif cls.element2 in kwargs:
            return round(float(kwargs[cls.element2]), 6)
        else:
            raise TypeError("Neither 'y' nor '{}' are in kwargs"
                            "".format(cls.element2))
    
    @classmethod
    def _has_z(cls, kwargs):
        '''Returns True if z is explicitly defined in kwargs'''
        return ('z' in kwargs) or (cls.element3 in kwargs)
    
    @classmethod
    def _get_z(cls, kwargs):
        '''
        Returns z if it is explicitly defined in kwargs.
        Otherwise, raises TypeError.
        '''
        if 'z' in kwargs:
            return round(float(kwargs['z']), 6)
        elif cls.element3 in kwargs:
            return round(float(kwargs[cls.element3]), 6)
        else:
            raise TypeError("Neither 'z' nor '{}' are in kwargs"
                            "".format(cls.element3))
    
    @classmethod
    def _get_usage(cls):
        return ("The  supported kwarg combinations are as follows:"
                "\n    - ('x' or '{1}') and ('y' or '{2}')"
                "\n    - ('x' or '{1}') and ('z' or '{3}')"
                "\n    - ('y' or '{2}') and ('z' or '{3}')"
                "\n    - 'a' and 'T' and ('x' or '{1}')"
                "\n    - 'a' and 'T' and ('y' or '{2}')"
                "\n    - 'a' and 'T' and ('z' or '{3}')"
                            "".format(None, cls.element1, cls.element2,
                                            cls.element3, cls.element4))

    @classinstancemethod
    def elementFraction(self, cls, element):
        # A_{x}B_{y}C_{1-x-y}D
        if element == cls.element1:
            return self._x
        elif element == cls.element2:
            return self._y
        elif element == cls.element3:
            return self._z
        elif element == cls.element4:
            return 1
        else:
            return 0

# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# binary1 = AC
# binary2 = AD
# binary3 = BC
# binary4 = BD
# ternary1 = ABC
# ternary2 = ABD
# ternary3 = ACD
# ternary4 = BCD
class Quaternary3(Quaternary):
    '''
    For alloys of the A_{x}B_{1-x}C_{y}D_{1-y} type [1-2]. Where A and B are
    Group III elements, and C and D are Group V elements. These require
    four ternaries for interpolation.
    
    [1] T. H. Glisson, J. R. Hauser, M. A. Littlejohn, and C. K. Williams,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys," JEM, vol. 7, no. 1, pp. 1-16, Jan. 1978.

    [2] I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, "Band parameters
    for III-V compound semiconductors and their alloys," J. Appl. Phys.,
    vol. 89, no. 11, pp. 5815-5875, Jun. 2001.
    '''
    __metaclass__ = Quaternary3Type
    
    def __init__(self, **kwargs):
        Quaternary.__init__(self)
        self._x = self._get_x(kwargs)
        self._y = self._get_y(kwargs)

    def __getattr__(self, name):
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name) and
            hasattr(self.ternary4, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)

    def __str__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f1 = self.elementFraction(e1)
        f2 = self.elementFraction(e2)
        f3 = self.elementFraction(e3)
        f4 = self.elementFraction(e4)
        return "{A}_{{{:g}}}{B}_{{{:g}}}{C}_{{{:g}}}{D}_{{{:g}}}".format(
                                              f1, f2, f3, f4,
                                              A=e1, B=e2, C=e3, D=e4)
    def __repr__(self):
        e1 = self.element1
        e2 = self.element2
        e3 = self.element3
        e4 = self.element4
        f1 = self.elementFraction(e1)
        f3 = self.elementFraction(e3)
        return "{A}{B}{C}{D}({A}={:g}, {C}={:g})".format(f1, f3,
                                                 A=e1, B=e2, C=e3, D=e4)
    
    @classmethod
    def _get_x(cls, kwargs):
        if 'x' in kwargs:
            return round(float(kwargs['x']), 6)
        elif cls.element1 in kwargs:
            return round(float(kwargs[cls.element1]), 6)
        elif cls.element2 in kwargs:
            return 1 - round(float(kwargs[cls.element2]), 6)
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            y = cls._get_y(kwargs) # need the other composition fixed
            if 'T' not in kwargs:
                raise ValueError('Lattice matching temperature, T, missing.')
            a = kwargs['a']
            T = kwargs['T']
            # make sure the lattice constant is available
            x0a = cls.a(x=0, y=y, T=T)
            x1a = cls.a(x=1, y=y, T=T)
            amin = min(x0a, x1a)
            amax = max(x0a, x1a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]'%(amin, amax))
            # find the correct composition, x
            x = bisect(func=lambda x: cls.a(x=x, y=y, T=T) - a, a=0, b=1)
            return x
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed."%(cls.element1,
                                                             cls.element2))
    
    @classmethod
    def _get_y(cls, kwargs):
        if 'y' in kwargs:
            return round(float(kwargs['y']), 6)
        elif cls.element3 in kwargs:
            return round(float(kwargs[cls.element3]), 6)
        elif cls.element4 in kwargs:
            return 1 - round(float(kwargs[cls.element4]), 6)
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            x = cls._get_x(kwargs) # need the other composition fixed
            if 'T' not in kwargs:
                raise ValueError('Lattice matching temperature, T, missing.')
            a = kwargs['a']
            T = kwargs['T']
            # make sure the lattice constant is available
            y0a = cls.a(x=x, y=0, T=T)
            y1a = cls.a(x=x, y=1, T=T)
            amin = min(y0a, y1a)
            amax = max(y0a, y1a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]'%(amin, amax))
            # find the correct composition, y
            y = bisect(func=lambda y: cls.a(x=x, y=y, T=T) - a, a=0, b=1)
            return y
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed."%(cls.element3,
                                                             cls.element4))
    
    @classinstancemethod
    def _interpolate(self, cls, param, **kwargs):
        if self is not None:
            x = self._x
            y = self._y
        else:
            x = cls._get_x(kwargs)
            y = cls._get_y(kwargs)
            
        vals = []
        for t in [cls.ternary1, cls.ternary2, cls.ternary3, cls.ternary4]:
            try:
                vals.append(getattr(t, param))
            except AttributeError as e:
                e.message +='. Ternary `%s`'%t.name
                e.message +=' missing param `%s`'%param
                raise e
        if param[0] == '_':
            # assume it's a hard coded parameter if it starts with '_'
            ABC = vals[0]
            ABD = vals[1]
            ACD = vals[2]
            BCD = vals[3]
        else:
            # otherwise it's an accessor function
            new_kwargs = dict(kwargs)
            new_kwargs['x'] = x
            ABC = vals[0](**new_kwargs)
            ABD = vals[1](**new_kwargs)
            new_kwargs['x'] = y
            ACD = vals[2](**new_kwargs)
            BCD = vals[3](**new_kwargs)
        xinv = 1. - x
        yinv = 1. - y
        xweight = x*xinv
        yweight = y*yinv
        denom = xweight + yweight
        if denom == 0.:
            # handle this explicitly, so there's no divide by zero
            if x == 0.:
                return BCD
            else:
                return ACD
        else:
            num = xweight*( y*ABC + yinv*ABD ) + yweight*( x*ACD + xinv*BCD )
            return num / denom
    
    @classinstancemethod
    def elementFraction(self, cls, element):
        if element == cls.element1:
            return self._x
        elif element == cls.element2:
            return (1 - self._x)
        elif element == cls.element3:
            return self._y
        elif element == cls.element4:
            return (1 - self._y)
        else:
            return 0