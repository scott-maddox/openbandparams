#
#   Copyright (c) 2013-2015, Scott J Maddox
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
__all__ = ['IIIVZincBlendeTernary']

from .iii_v_zinc_blende_mixed_alloy import IIIVZincBlendeMixedAlloy
from .algorithms import bisect

class IIIVZincBlendeTernary(IIIVZincBlendeMixedAlloy):
    '''
    The base class for all III-V zinc blende ternary alloys.
    '''
    def __init__(self, name, elements, binaries, parameters=None, x=None):
        if binaries[0].elements[1] == binaries[1].elements[1]:
            # A_{x}B_{1-x}C
            # e.g. AlGaAs
            self._type = 1
            self._element_x = elements[0]
            self._element_1mx = elements[1]
            self._element_y = elements[2]
        elif binaries[0].elements[0] == binaries[1].elements[0]:
            # AB_{x}C_{1-x}
            # e.g. GaAsSb
            self._type = 2
            self._element_y = elements[0]
            self._element_x = elements[1]
            self._element_1mx = elements[2]
        else:
            raise ValueError()
        super(IIIVZincBlendeTernary, self).__init__(name, elements,
                                                    parameters=parameters)
        self.binaries = binaries
        if x is not None:
            self._x = float(x)
        else:
            self._x = None

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.name == other.name and
                self.elements == other.elements,
                self.binaries == other.binaries,
                self._parameters == other._parameters,
                self._x == other._x)
    
    def _instance(self, x=None):
        return IIIVZincBlendeTernary(self.name, self.elements,
            self.binaries, parameters=self._parameters.values(), x=x)

    def __call__(self, **kwargs):
        '''
        Used to specify the alloy composition.
        '''
        if 'x' in kwargs:
            x = float(kwargs['x'])
        elif self._element_x in kwargs:
            x = float(kwargs[self._element_x])
        elif self._element_1mx in kwargs:
            x = 1. - float(kwargs[self._element_1mx])
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            a = kwargs['a']
            T = kwargs.get('T', 300.)
            # make sure the lattice constant is available
            b1a = self.binaries[0].a(T=T)
            b2a = self.binaries[1].a(T=T)
            amin = min(b1a, b2a)
            amax = max(b1a, b2a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]' % (amin, amax))
            # find the correct composition, x
            x = bisect(func=lambda x: self(x=x).a(T=T) - a, a=0, b=1)
        else:
            raise TypeError(
                "Missing required key word argument.\n" + self._get_usage())
        if not (0. <= x <= 1.):
            raise ValueError('The alloy fraction must be between 0 and 1')
        return self._instance(x=x)

    def _get_usage(self):
        return ("The supported kwarg combinations are as follows:"
                "\n    - 'x' or '{A}' or '{B}'"
                "\n    - 'a' [and 'T']"
                "".format(A=self._element_x, B=self._element_1mx))

    def __repr__(self):
        if self._x is None:
            return '{}'.format(self.name)
        elif self._type == 1 or self._type == 2:
            return '{}({}={})'.format(self.name, self._element_x, self._x)
        else:
            raise RuntimeError()
    
    def latex(self):
        if self._type == 1:
            if self._x is None:
                return "{A}_{{x}}{B}_{{1-x}}{C}".format(A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
            else:
                return "{A}_{{{:g}}}{B}_{{{:g}}}{C}".format(self._x,
                                                            1. - self._x,
                                                            A=self.elements[0],
                                                            B=self.elements[1],
                                                            C=self.elements[2])
        elif self._type == 2:
            if self._x is None:
                return "{A}{B}_{{x}}{C}_{{1-x}}".format(A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
            else:
                return "{A}{B}_{{{:g}}}{C}_{{{:g}}}".format(self._x,
                                                            1. - self._x,
                                                            A=self.elements[0],
                                                            B=self.elements[1],
                                                            C=self.elements[2])
        else:
            raise RuntimeError()

    def element_fraction(self, element):
        if self._x is None:
            raise RuntimeError('Alloy composition has not been specified.')
        if self._type == 1:
            if element == self.elements[0]:
                return self._x
            elif element == self.elements[1]:
                return (1 - self._x)
            elif element == self.elements[2]:
                return 1
            else:
                return 0
        elif self._type == 2:
            if element == self.elements[0]:
                return 1
            elif element == self.elements[1]:
                return self._x
            elif element == self.elements[2]:
                return (1 - self._x)
            else:
                return 0
        else:
            raise RuntimeError()
     
    def _get_bowing(self, name, kwargs):
        p = self.get_parameter(name+'_bowing', default=None)
        if p is None:
            return None
        return p(x=self._x, **kwargs)
    
    def _interpolate(self, name, kwargs):
        if self._x is None:
            raise RuntimeError('Alloy composition has not been specified.')
        x = self._x
        pA = self.binaries[0].get_parameter(name)
        if pA is None:
            raise AttributeError('"{}" is missing a required parameter: "{}".'
                                 ''.format(self.binaries[0].name,
                                           name))
        pB = self.binaries[1].get_parameter(name)
        if pB is None:
            raise AttributeError('"{}" is missing a required parameter: "{}".'
                                 ''.format(self.binaries[1].name,
                                           name))
        A = pA(**kwargs)
        B = pB(**kwargs)
        C = self._get_bowing(name, kwargs)
        if C is not None:
            # a bowing parameter exists - use it
            return A * x + B * (1 - x) - C * x * (1 - x)
        else:
            # otherwise, use linear interpolation
            return A * x + B * (1 - x)
