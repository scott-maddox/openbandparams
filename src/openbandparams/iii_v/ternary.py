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

from openbandparams.algorithms import bisect
from openbandparams.base_material import BaseType, AlloyBase
from openbandparams.utils import classinstancemethod


class TernaryType(BaseType):
    def __getattr__(self, name):
        # acts like a class method for the Ternary class
        if (hasattr(self.binaries[0], name) and
            hasattr(self.binaries[1], name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)


class Ternary(AlloyBase):
    __metaclass__ = TernaryType

    def __init__(self, **kwargs):
        AlloyBase.__init__(self)
        self._x = self._get_x(kwargs)

    def __getattr__(self, name):
        if (hasattr(self.binaries[0], name) and
            hasattr(self.binaries[1], name)):
            def _param_accessor(**kwargs):
                return self._interpolate(name, **kwargs)
            return _param_accessor
        else:
            raise AttributeError(name)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return (type(self) == type(other) and
                self._x == other._x)

    @classmethod
    def _get_bowing(cls, param, x):
        if hasattr(cls, '_bowing_%s' % param):
            # a bowing parameter exists - use it
            C = getattr(cls, '_bowing_%s' % param)
            if callable(C):
                # assume the bowing paramter is composition dependent
                # if it's callable
                return C(x)
            else:
                return C
        else:
            return None

    @classinstancemethod
    def _interpolate(self, cls, param, **kwargs):
        if self is not None:
            x = self._x
        else:
            x = cls._get_x(kwargs)

        vals = []
        for b in [cls.binaries[0], cls.binaries[1]]:
            try:
                vals.append(getattr(b, param))
            except AttributeError as e:
                e.message += '. Binary `%s`' % b.name
                e.message += ' missing param `%s`' % param
                raise e
        if param[0] == '_':
            # assume it's a hard coded parameter if it starts with '_'
            A = vals[0]
            B = vals[1]
        else:
            # otherwise it's an accessor function
            A = vals[0](**kwargs)
            B = vals[1](**kwargs)
        C = cls._get_bowing(param, x)
        if C is not None:
            # a bowing parameter exists - use it
            return A * x + B * (1 - x) - C * x * (1 - x)
        else:
            # otherwise, use linear interpolation
            return A * x + B * (1 - x)

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
            T = cls._get_T(kwargs)
            return min(cls.Eg_Gamma(x=x, T=T), cls.Eg_X(x=x, T=T),
                       cls.Eg_L(x=x, T=T))


class Ternary1(Ternary):
    '''
    For alloys of the A_{x}B_{1-x}C type, where A and B are Group III
    elements, and C is a Group V element.
    '''

    def __repr__(self):
        return '{}({}={})'.format(self.name, self.elements[0], self._x)
    
    @classinstancemethod
    def LaTeX(self, cls):
        if self is not None:
            return "{A}_{{{:g}}}{B}_{{{:g}}}{C}".format(self._x, 1 - self._x,
                                                        A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
        else:
            return "{A}_{{x}}{B}_{{1-x}}{C}".format(A=cls.elements[0],
                                                    B=cls.elements[1],
                                                    C=cls.elements[2])

    @classmethod
    def _get_x(cls, kwargs):
        if 'x' in kwargs:
            return float(kwargs['x'])
        elif cls.elements[0] in kwargs:
            return float(kwargs[cls.elements[0]])
        elif cls.elements[1] in kwargs:
            return 1 - float(kwargs[cls.elements[1]])
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            if 'T' not in kwargs:
                raise TypeError('Lattice matching temperature, T, missing.')
            a = kwargs['a']
            T = kwargs['T']
            # make sure the lattice constant is available
            b1a = cls.binaries[0].a(T=T)
            b2a = cls.binaries[1].a(T=T)
            amin = min(b1a, b2a)
            amax = max(b1a, b2a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]' % (amin, amax))
            # find the correct composition, x
            x = bisect(func=lambda x: cls.a(x=x, T=T) - a, a=0, b=1)
            return x
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed." % (cls.elements[0],
                                                             cls.elements[1]))

    def elementFraction(self, element):
        if element == self.elements[0]:
            return self._x
        elif element == self.elements[1]:
            return (1 - self._x)
        elif element == self.elements[2]:
            return 1
        else:
            return 0


class Ternary2(Ternary):
    '''
    For alloys of the AB_{x}C_{1-x} type, where A is a Group III element,
    and B and C are Group V elements.
    '''

    def __repr__(self):
        return '{}({}={})'.format(self.name, self.elements[1], self._x)
    
    @classinstancemethod
    def LaTeX(self, cls):
        if self is not None:
            return "{A}{B}_{{{:g}}}{C}_{{{:g}}}".format(self._x, 1 - self._x,
                                                        A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
        else:
            return "{A}{B}_{{x}}{C}_{{1-x}}".format(A=cls.elements[0],
                                                    B=cls.elements[1],
                                                    C=cls.elements[2])

    @classmethod
    def _get_x(cls, kwargs):
        if 'x' in kwargs:
            return float(kwargs['x'])
        elif cls.elements[1] in kwargs:
            return float(kwargs[cls.elements[1]])
        elif cls.elements[2] in kwargs:
            return 1 - float(kwargs[cls.elements[2]])
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            if 'T' not in kwargs:
                raise TypeError('Lattice matching temperature, T, missing.')
            a = kwargs['a']
            T = kwargs['T']
            # make sure the lattice constant is available
            b1a = cls.binaries[0].a(T=T)
            b2a = cls.binaries[1].a(T=T)
            amin = min(b1a, b2a)
            amax = max(b1a, b2a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]' % (amin, amax))
            # find the correct composition, x
            x = bisect(func=lambda x: cls.a(x=x, T=T) - a, a=0, b=1)
            return x
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed." % (cls.elements[1],
                                                             cls.elements[2]))

    def elementFraction(self, element):
        if element == self.elements[0]:
            return 1
        elif element == self.elements[1]:
            return self._x
        elif element == self.elements[2]:
            return (1 - self._x)
        else:
            return 0

# class ReversedTernary(Ternary):
#    @classmethod
#    def _get_bowing(cls, param, x):
#        if hasattr(cls._ternary, '_bowing_%s'%param):
#            # a bowing parameter exists - use it
#            C = getattr(cls._ternary, '_bowing_%s'%param)
#            if callable(C):
#                # assume the bowing paramter is composition dependent
#                # if it's callable
#                return C(1-x) # reverse the composition
#            else:
#                return C
#        else:
#            return None

# def create_reversed_ternary(name, ternary):
#    new_type = type(name, (ReversedTernary,), {})
#    new_type.name = name
#    new_type.element1 = ternary.element2
#    new_type.binary1 = ternary.binary2
#    new_type.element2 = ternary.element1
#    new_type.binary2 = ternary.binary1
#    new_type._ternary = ternary
#    return new_type
