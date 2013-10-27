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

class TernaryType(type):
    def __getattr__(self, name):
        # acts like a class method for the Ternary class
        if hasattr(self.binary1, name) and hasattr(self.binary2, name):
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
        if hasattr(self.binary1, name) and hasattr(self.binary2, name):
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
        else:
            raise TypeError("Missing required key word argument."
                            "'x', '%s', or '%s' is needed."%(cls.element1,
                                                             cls.element2))
    
    @classmethod
    def _get_bowing(cls, param, x):
        if hasattr(cls, '_bowing_%s'%param):
            # a bowing parameter exists - use it
            C = getattr(cls, '_bowing_%s'%param)
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
        for b in [cls.binary1, cls.binary2]:
            try:
                vals.append(getattr(b, param))
            except AttributeError as e:
                e.message +='. Binary `%s`'%b.name
                e.message +=' missing param `%s`'%param
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
            return A*x + B*(1-x) - C*x*(1-x)
        else:
            # otherwise, use linear interpolation
            return A*x + B*(1-x)
    
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

class ReversedTernary(Ternary):
    @classmethod
    def _get_bowing(cls, param, x):
        if hasattr(cls._ternary, '_bowing_%s'%param):
            # a bowing parameter exists - use it
            C = getattr(cls._ternary, '_bowing_%s'%param)
            if callable(C):
                # assume the bowing paramter is composition dependent
                # if it's callable
                return C(1-x) # reverse the composition
            else:
                return C
        else:
            return None

def create_reversed_ternary(name, ternary):
    new_type = type(name, (ReversedTernary,), {})
    new_type.name = name
    new_type.element1 = ternary.element2
    new_type.binary1 = ternary.binary2
    new_type.element2 = ternary.element1
    new_type.binary2 = ternary.binary1
    new_type._ternary = ternary
    return new_type
