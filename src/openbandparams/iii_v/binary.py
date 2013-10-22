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
from math import tanh

# third party imports

# local imports
from openbandparams.base_material import Base
from openbandparams.equations import varshni

class Binary(Base):
    def __init__(self, name):
        self.name = name
    def a(self, T=300):
        '''
        Returns the lattice parameter, a, in Angstroms at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        return self._a_300K + self._da_dT * (T - 300)
    def Eg_Gamma(self, T=300):
        '''
        Returns the Gamma-valley bandgap, Eg_Gamma, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        return varshni(self._Eg_Gamma_0, self._alpha_Gamma, self._beta_Gamma, T)
    def Eg_X(self, T=300):
        '''
        Returns the X-valley bandgap, Eg_X, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        return varshni(self._Eg_X_0, self._alpha_X, self._beta_X, T)
    def Eg_L(self, T=300):
        '''
        Returns the L-valley bandgap, Eg_L, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        return varshni(self._Eg_L_0, self._alpha_L, self._beta_L, T)
    def Eg(self, T=300):
        '''
        Returns the bandgap, Eg, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K)
        '''
        return min(self.Eg_Gamma(T), self.Eg_X(T), self.Eg_L(T))