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
from openbandparams.iii_v.ternary import create_ternary, create_reversed_ternary
from openbandparams.iii_v.zinc_blende.binary import (AlN,  GaN,  InN,
                                                     AlP,  GaP,  InP,
                                                     AlAs, GaAs, InAs,
                                                     AlSb, GaSb, InSb)

# Each ternary below is dynamically created as a new class or type.
# An instance of the class must be created, and the alloy fraction passed in,
# before it can be used. See `simple_example_2.py` for examples.

# Nitrides
AlGaN = create_ternary('AlGaN', 'Al', AlN, 'Ga', GaN,
                       {
                        '_bowing_Eg_Gamma' : 0.76, #eV    lin_band_2002
                        '_bowing_Eg_X' : 0.3, #eV    lin_band_2002
                        })
AlInN = create_ternary('AlInN', 'Al', AlN, 'In', InN,
                       {
                        '_bowing_Eg_Gamma' : 2.73, #eV    lin_band_2002
                        '_bowing_Eg_X' : 3.62, #eV    lin_band_2002
                        })
GaInN = create_ternary('GaInN', 'Ga', GaN, 'In', InN,
                       {
                        '_bowing_Eg_Gamma' : 1.38, #eV    lin_band_2002
                        '_bowing_Eg_X' : 1.67, #eV    lin_band_2002
                        })

GaAlN = create_reversed_ternary('GaAlN', AlGaN)
InAlN = create_reversed_ternary('InAlN', AlInN)
InGaN = create_reversed_ternary('InGaN', GaInN)

# Phosphides
AlGaP = create_ternary('AlGaP', 'Al', AlP, 'Ga', GaP,
                       {
                        '_bowing_Eg_X' : 0.13, #eV    vurgaftman_band_2001
                        })
AlInP = create_ternary('AlInP', 'Al', AlP, 'In', InP,
                       {
                        '_bowing_Eg_Gamma' : -0.48, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.38, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : -0.19, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.22, #m_e    vurgaftman_band_2001
                        })
GaInP = create_ternary('GaInP', 'Ga', GaP, 'In', InP,
                       {
                        '_bowing_Eg_Gamma' : 0.65, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.2, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 1.03, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.051, #m_e    vurgaftman_band_2001
                        '_bowing_F' : 0.78, #vurgaftman_band_2001
                        })

GaAlP = create_reversed_ternary('GaAlP', AlGaP)
InAlP = create_reversed_ternary('InAlP', AlInP)
InGaP = create_reversed_ternary('InGaP', GaInP)

# Arsenides
def AlGaAs_init(self):
    '''
    AlGaAs's Eg_Gamma has an alloy dependent bowing parameter
    '''
    self._bowing_Eg_Gamma = 1.31*self._x - 0.127 #eV    vurgaftman_band_2001

AlGaAs = create_ternary('AlGaAs', 'Al', AlAs, 'Ga', GaAs,
                       {
                        '_init' : AlGaAs_init,
                        '_bowing_Eg_X' : 0.055, #eV    vurgaftman_band_2001
                        })
AlInAs = create_ternary('AlInAs', 'Al', AlAs, 'In', InAs,
                       {
                        '_bowing_Eg_Gamma' : 0.7, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.15, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.049, #m_e    vurgaftman_band_2001
                        '_bowing_Ep' : -4.81, #eV    vurgaftman_band_2001
                        '_bowing_F' : -4.44, #vurgaftman_band_2001
                        '_bowing_VBO' : -0.64, #eV    vurgaftman_band_2001
                        '_bowing_a_c' : -1.4, #eV    vurgaftman_band_2001
                        })
GaInAs = create_ternary('GaInAs', 'Ga', GaAs, 'In', InAs,
                       {
                        '_bowing_Eg_Gamma' : 0.477, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 1.4, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.33, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.15, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.0091, #m_e    vurgaftman_band_2001
                        '_bowing_meff_HH_DOS' : -0.145, #m_e    vurgaftman_band_2001
                        '_bowing_meff_LH_DOS' : 0.0202, #m_e    vurgaftman_band_2001
                        '_bowing_Ep' : -1.48, #eV    vurgaftman_band_2001
                        '_bowing_F' : 1.77, #vurgaftman_band_2001
                        '_bowing_VBO' : -0.38, #eV    vurgaftman_band_2001
                        '_bowing_a_c' : 2.61, #eV    vurgaftman_band_2001
                        })

GaAlAs = create_reversed_ternary('GaAlAs', AlGaAs)
InAlAs = create_reversed_ternary('InAlAs', AlInAs)
InGaAs = create_reversed_ternary('InGaAs', GaInAs)

# Antimonides
def AlGaSb_init(self):
    '''
    AlGaSb's Eg_Gamma has an alloy dependent bowing parameter
    '''
    self._bowing_Eg_Gamma = 1.22*self._x - 0.044 #eV    vurgaftman_band_2001
AlGaSb = create_ternary('AlGaSb', 'Al', AlSb, 'Ga', GaSb,
                       {
                        '_init' : AlGaSb_init,
                        '_bowing_Delta_SO' : 0.3, #eV    vurgaftman_band_2001
                        })
AlInSb = create_ternary('AlInSb', 'Al', AlSb, 'In', InSb,
                       {
                        '_bowing_Eg_Gamma' : 0.43, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.25, #eV    vurgaftman_band_2001
                        })
GaInSb = create_ternary('GaInSb', 'Ga', GaSb, 'In', InSb,
                       {
                        '_bowing_Eg_Gamma' : 0.415, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.33, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.4, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.1, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.0092, #m_e    vurgaftman_band_2001
                        '_bowing_meff_LH_DOS' : 0.011, #m_e    vurgaftman_band_2001
                        '_bowing_F' : -6.84, #vurgaftman_band_2001
                        })

GaAlSb = create_reversed_ternary('GaAlSb', AlGaSb)
InAlSb = create_reversed_ternary('InAlSb', AlInSb)
InGaSb = create_reversed_ternary('InGaSb', GaInSb)

# Nitride Phosphides
AlNP = create_ternary('AlNP', 'N', AlN, 'P', AlP,
                       {
                        })
GaNP = create_ternary('GaNP', 'N', GaN, 'P', GaP,
                       {
                        '_bowing_Eg_Gamma' : 3.9, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 10, #eV    vurgaftman_band_2001
                        })
InNP = create_ternary('InNP', 'N', InN, 'P', InP,
                       {
                        '_bowing_Eg_Gamma' : 15, #eV    vurgaftman_band_2001
                        })

AlPN = create_reversed_ternary('AlPN', AlNP)
GaPN = create_reversed_ternary('GaPN', GaNP)
InPN = create_reversed_ternary('InPN', InNP)

# Nitride Arsenides
AlNAs = create_ternary('AlNAs', 'N', AlN, 'As', AlAs,
                       {
                        })
def GaNAs_init(self):
    self._bowing_Eg_Gamma = 120.4 - 100*self._x #eV    vurgaftman_band_2001
GaNAs = create_ternary('GaNAs', 'N', GaN, 'As', GaAs,
                       {
                        '_init' : GaNAs_init,
                        })
InNAs = create_ternary('InNAs', 'N', InN, 'As', InAs,
                       {
                        '_bowing_Eg_Gamma' : 4.22, #eV    vurgaftman_band_2001
                        })

AlAsN = create_reversed_ternary('AlAsN', AlNAs)
GaAsN = create_reversed_ternary('GaAsN', GaNAs)
InAsN = create_reversed_ternary('InAsN', InNAs)

# Phosphide Arsenides
AlPAs = create_ternary('AlPAs', 'P', AlP, 'As', AlAs,
                       {
                        '_bowing_Eg_Gamma' : 0.22, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.22, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.22, #eV    vurgaftman_band_2001
                        })
GaPAs = create_ternary('GaPAs', 'P', GaP, 'As', GaAs,
                       {
                        '_bowing_Eg_Gamma' : 0.19, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.24, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.16, #eV    vurgaftman_band_2001
                        })
InPAs = create_ternary('InPAs', 'P', InP, 'As', InAs,
                       {
                        '_bowing_Eg_Gamma' : 0.1, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.27, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.27, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.16, #eV    vurgaftman_band_2001
                        })

AlAsP = create_reversed_ternary('AlAsP', AlPAs)
GaAsP = create_reversed_ternary('GaAsP', GaPAs)
InAsP = create_reversed_ternary('InAsP', InPAs)

# Phosphide Antimonides
AlPSb = create_ternary('AlPSb', 'P', AlP, 'Sb', AlSb,
                       {
                        '_bowing_Eg_Gamma' : 2.7, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 2.7, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 2.7, #eV    vurgaftman_band_2001
                        })
GaPSb = create_ternary('GaPSb', 'P', GaP, 'Sb', GaSb,
                       {
                        '_bowing_Eg_Gamma' : 2.7, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 2.7, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 2.7, #eV    vurgaftman_band_2001
                        })
InPSb = create_ternary('InPSb', 'P', InP, 'Sb', InSb,
                       {
                        '_bowing_Eg_Gamma' : 1.9, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 1.9, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 1.9, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.75, #eV    vurgaftman_band_2001
                        })

AlSbP = create_reversed_ternary('AlSbP', AlPSb)
GaSbP = create_reversed_ternary('GaSbP', GaPSb)
InSbP = create_reversed_ternary('InSbP', InPSb)

# Arsenide Antimonides
AlAsSb = create_ternary('AlAsSb', 'As', AlAs, 'Sb', AlSb,
                       {
                        '_bowing_Eg_Gamma' : 0.8, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.28, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.28, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.15, #eV    vurgaftman_band_2001
                        '_bowing_VBO' : -1.71, #eV    vurgaftman_band_2001
                        })
GaAsSb = create_ternary('GaAsSb', 'As', GaAs, 'Sb', GaSb,
                       {
                        '_bowing_Eg_Gamma' : 1.43, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 1.2, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 1.2, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 0.6, #eV    vurgaftman_band_2001
                        '_bowing_VBO' : -1.06, #eV    vurgaftman_band_2001
                        })
InAsSb = create_ternary('InAsSb', 'As', InAs, 'Sb', InSb,
                       {
                        '_bowing_Eg_Gamma' : 0.67, #eV    vurgaftman_band_2001
                        '_bowing_Eg_X' : 0.6, #eV    vurgaftman_band_2001
                        '_bowing_Eg_L' : 0.6, #eV    vurgaftman_band_2001
                        '_bowing_Delta_SO' : 1.2, #eV    vurgaftman_band_2001
                        '_bowing_meff_e_Gamma' : 0.035, #m_e    vurgaftman_band_2001
                        })

AlSbAs = create_reversed_ternary('AlSbAs', AlAsSb)
GaSbAs = create_reversed_ternary('GaSbAs', GaAsSb)
InSbAs = create_reversed_ternary('InSbAs', InAsSb)

ternaries = [AlGaN,  AlInN,  GaInN,
             AlGaP,  AlInP,  GaInP,
             AlGaAs, AlInAs, GaInAs,
             AlGaSb, AlInSb, GaInSb,
             AlNP,   GaNP,   InNP,
             AlNAs,  GaNAs,  InNAs,
             AlPAs,  GaPAs,  InPAs,
             AlPSb,  GaPSb,  InPSb,
             AlAsSb, GaAsSb, InAsSb]

reversed = [GaAlN,  InAlN,  InGaN,
            GaAlP,  InAlP,  InGaP,
            GaAlAs, InAlAs, InGaAs,
            GaAlSb, InAlSb, InGaSb,
            AlPN,   GaPN,   InPN,
            AlAsN,  GaAsN,  InAsN,
            AlAsP,  GaAsP,  InAsP,
            AlSbP,  GaSbP,  InSbP,
            AlSbAs, GaSbAs, InSbAs]
