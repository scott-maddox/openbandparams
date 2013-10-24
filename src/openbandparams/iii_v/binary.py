#
#   Copyright (c) 2013, Scott J Maddox
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
################################################################################

# std lib imports
import logging; log = logging.getLogger(__name__)
from math import tanh

# third party imports

# local imports
from openbandparams.base_material import Base
from openbandparams.equations import varshni

class Binary(Base):
    name = None
    
    # All methods should be class methods so that they can reference parameters
    # defined by the inheriting class.
    @classmethod
    def a(cls, **kwargs):
        '''
        Returns the lattice parameter, a, in Angstroms at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        T = cls._get_T(kwargs)
        return cls._a_300K + cls._da_dT * (T - 300)
    
    @classmethod
    def Eg_Gamma(cls, **kwargs):
        '''
        Returns the Gamma-valley bandgap, Eg_Gamma, in electron Volts at a
        given temperature, T, in Kelvin (default: 300 K).
        '''
        T = cls._get_T(kwargs)
        return varshni(cls._Eg_Gamma_0, cls._alpha_Gamma, cls._beta_Gamma, T)
    
    @classmethod
    def Eg_X(cls, **kwargs):
        '''
        Returns the X-valley bandgap, Eg_X, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        T = cls._get_T(kwargs)
        return varshni(cls._Eg_X_0, cls._alpha_X, cls._beta_X, T)
    
    @classmethod
    def Eg_L(cls, **kwargs):
        '''
        Returns the L-valley bandgap, Eg_L, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        T = cls._get_T(kwargs)
        return varshni(cls._Eg_L_0, cls._alpha_L, cls._beta_L, T)
    
    @classmethod
    def Eg(cls, **kwargs):
        '''
        Returns the bandgap, Eg, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        T = cls._get_T(kwargs)
        return min(cls.Eg_Gamma(T), cls.Eg_X(T), cls.Eg_L(T))