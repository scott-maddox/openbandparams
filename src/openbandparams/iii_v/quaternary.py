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

class Quaternary(AlloyBase):
    pass

class Quaternary1Type(type):
    def __getattr__(self, name):
        # acts like a class method for Quaternary1.__getattr__
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)

Quaternary2Type = Quaternary1Type

class Quaternary3Type(type):
    def __getattr__(self, name):
        # acts like a class method for Quaternary2.__getattr__
        if (hasattr(self.ternary1, name) and
            hasattr(self.ternary2, name) and
            hasattr(self.ternary3, name) and
            hasattr(self.ternary4, name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)

class Quaternary1(Quaternary):
    '''
    For alloys of the AB_{x}C_{y}D_{1-x-y} type [1-2], where A is the only
    Group III element. These require only three ternaries for interpolation.
    
    [1] T. H. Glisson, J. R. Hauser, M. A. Littlejohn, and C. K. Williams,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys," JEM, vol. 7, no. 1, pp. 1-16, Jan. 1978.

    [2] I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, "Band parameters
    for III-V compound semiconductors and their alloys," J. Appl. Phys.,
    vol. 89, no. 11, pp. 5815-5875, Jun. 2001.
    '''
    __metaclass__ = Quaternary1Type
    
    def __init__(self, **kwargs):
        Quaternary.__init__(self)
        raise NotImplementedError()

class Quaternary2(Quaternary):
    '''
    For alloys of the A_{x}B_{y}C_{1-x-y}D type [1-2], where D is the only
    Group V element. These require only three ternaries for interpolation.
    
    [1] T. H. Glisson, J. R. Hauser, M. A. Littlejohn, and C. K. Williams,
    "Energy bandgap and lattice constant contours of iii-v quaternary
    alloys," JEM, vol. 7, no. 1, pp. 1-16, Jan. 1978.

    [2] I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, "Band parameters
    for III-V compound semiconductors and their alloys," J. Appl. Phys.,
    vol. 89, no. 11, pp. 5815-5875, Jun. 2001.
    '''
    __metaclass__ = Quaternary1Type
    
    def __init__(self, **kwargs):
        Quaternary.__init__(self)
        raise NotImplementedError()

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
    
    @classmethod
    def _get_x(cls, kwargs):
        if 'x' in kwargs:
            return float(kwargs['x'])
        elif cls.element1 in kwargs:
            return float(kwargs[cls.element1])
        elif cls.element2 in kwargs:
            return 1 - float(kwargs[cls.element2])
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
            return float(kwargs['y'])
        elif cls.element3 in kwargs:
            return float(kwargs[cls.element3])
        elif cls.element4 in kwargs:
            return 1 - float(kwargs[cls.element4])
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