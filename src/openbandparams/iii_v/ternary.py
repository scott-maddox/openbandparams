#
#   Copyright (c) 2013, Scott J Maddox
#
#   This file is part of OpenBandParams.
#
#   OpenBandParams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   PhotonAcq is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with PhotonAcq.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

# std lib imports
import logging; log = logging.getLogger(__name__)

# third party imports

# local imports
from openbandparams.base_material import AlloyBase
from openbandparams.utils import classinstancemethod

class Ternary(AlloyBase):
    def __init__(self, **kwargs):
        AlloyBase.__init__(self)
        self._x = self._get_x(kwargs)
    
    @classmethod
    def _get_x(cls, kwargs):
        if 'x' in kwargs:
            return float(kwargs['x'])
        elif cls.element1 in kwargs:
            return float(kwargs[cls.element1])
        elif cls.element2 in kwargs:
            return 1 - float(kwargs[cls.element2])
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed."%(cls.element1,
                                                             cls.element2))
    
    @classinstancemethod
    def _interpolate(self, cls, param, **kwargs):
        if self is not None:
            x = self._x
        else:
            x = cls._get_x(kwargs)
            
        vals = []
        for b in [cls.binary1, cls.binary2]:
            try:
                vals.append(getattr(b, param))
            except AttributeError as e:
                e.message +='. Binary `%s`'%b.name
                e.message +=' missing param `%s`'%param
                raise e
        if kwargs is None:
            A = vals[0]
            B = vals[1]
        else:
            A = vals[0](**kwargs)
            B = vals[1](**kwargs)
        if hasattr(cls, '_bowing_%s'%param):
            C = getattr(cls, '_bowing_%s'%param)
            if callable(C):
                # composition dependent bowing paramter
                C = C(x)
            return A*x + B*(1-x) - C*x*(1-x)
        else:
            return A*x + B*(1-x)
    
    @classinstancemethod
    def a(self, cls, **kwargs):
        '''
        Returns the lattice parameter, a, in Angstroms at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return self._interpolate('a', T=T)
        else:
            x = cls._get_x(kwargs)
            T = cls._get_T(kwargs)
            return cls._interpolate('a', x=x, T=T)
            
    
    @classinstancemethod
    def Eg_Gamma(self, cls, **kwargs):
        '''
        Returns the Gamma-valley bandgap, Eg_Gamma, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return self._interpolate('Eg_Gamma', T=T)
        else:
            x = cls._get_x(kwargs)
            T = cls._get_T(kwargs)
            return cls._interpolate('Eg_Gamma', x=x, T=T)
    
    @classinstancemethod
    def Eg_X(self, cls, **kwargs):
        '''
        Returns the X-valley bandgap, Eg_X, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return self._interpolate('Eg_X', T=T)
        else:
            x = cls._get_x(kwargs)
            T = cls._get_T(kwargs)
            return cls._interpolate('Eg_X', x=x, T=T)
    
    @classinstancemethod
    def Eg_L(self, cls, **kwargs):
        '''
        Returns the L-valley bandgap, Eg_L, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return self._interpolate('Eg_L', T=T)
        else:
            x = cls._get_x(kwargs)
            T = cls._get_T(kwargs)
            return cls._interpolate('Eg_L', x=x, T=T)
    
    @classinstancemethod
    def Eg(self, cls, **kwargs):
        '''
        Returns the bandgap, Eg, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        if self is not None:
            T = self._get_T(kwargs)
            return min(self.Eg_Gamma(T=T), self.Eg_X(T=T), self.Eg_L(T=T))
        else:
            x = cls._get_x(kwargs)
            T = cls._get_T(kwargs)
            return min(cls.Eg_Gamma(x=x, T=T), cls.Eg_X(x=x, T=T),
                       cls.Eg_L(x=x, T=T))

class ReversedTernary(Ternary):
    def __init__(self, x=None, **kwargs):
        Ternary.__init__(self, x, **kwargs)
        self.reversed_ternary_inst = self.reversed_ternary(1 - self._x)

def create_reversed_ternary(name, reversed_ternary):
    new_type = type(name, (Ternary,), {})
    new_type.name = name
    new_type.reversed_ternary = reversed_ternary
    new_type.element1 = reversed_ternary.element2
    new_type.binary1 = reversed_ternary.binary2
    new_type.element2 = reversed_ternary.element1
    new_type.binary2 = reversed_ternary.binary1
    return new_type
