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
import logging; log = logging.getLogger(__name__)

# third party imports

# local imports
from openbandparams.iii_v.ternary import *
from openbandparams.iii_v.zinc_blende.binary import *

# Each ternary below is dynamically created as a new class or type.
# An instance of the class must be created, and the alloy fraction passed in,
# before it can be used. See `simple_example_2.py` for examples.

# Nitrides
class AlGaN(Ternary1):
    name = 'AlGaN'
    elements = ('Al', 'Ga', 'N')
    binaries = (AlN, GaN)
    _bowing_Eg_Gamma = 0.76, #eV    lin_band_2002
    _bowing_Eg_X = 0.3, #eV    lin_band_2002
    
class AlInN(Ternary1):
    name = 'AlInN'
    elements = ('Al', 'In', 'N')
    binaries = (AlN, InN)
    _bowing_Eg_Gamma = 2.73, #eV    lin_band_2002
    _bowing_Eg_X = 3.62, #eV    lin_band_2002
    
class GaInN(Ternary1):
    name = 'GaInN'
    elements = ('Ga', 'In', 'N')
    binaries = (GaN, InN)
    _bowing_Eg_Gamma = 1.38, #eV    lin_band_2002
    _bowing_Eg_X = 1.67, #eV    lin_band_2002

#GaAlN = create_reversed_ternary('GaAlN', AlGaN)
#InAlN = create_reversed_ternary('InAlN', AlInN)
#InGaN = create_reversed_ternary('InGaN', GaInN)

# Phosphides
class AlGaP(Ternary1):
    name = 'AlGaP'
    elements = ('Al', 'Ga', 'P')
    binaries = (AlP, GaP)
    _bowing_Eg_X = 0.13 #eV    vurgaftman_band_2001

class AlInP(Ternary1):
    name = 'AlInP'
    elements = ('Al', 'In', 'P')
    binaries = (AlP, InP)
    _bowing_Eg_Gamma = -0.48 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.38 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = -0.19 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.22 #m_e    vurgaftman_band_2001

class GaInP(Ternary1):
    name = 'GaInP'
    elements = ('Ga', 'In', 'P')
    binaries = (GaP, InP)
    _bowing_Eg_Gamma = 0.65 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.2 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 1.03 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.051 #m_e    vurgaftman_band_2001
    _bowing_F = 0.78 #vurgaftman_band_2001

#GaAlP = create_reversed_ternary('GaAlP', AlGaP)
#InAlP = create_reversed_ternary('InAlP', AlInP)
#InGaP = create_reversed_ternary('InGaP', GaInP)

# Arsenides
class AlGaAs(Ternary1):
    name = 'AlGaAs'
    elements = ('Al', 'Ga', 'As')
    binaries = (AlAs, GaAs)
    _bowing_Eg_X = 0.055 #eV    vurgaftman_band_2001
    
    @classmethod
    def _bowing_Eg_Gamma(cls, x):
        return 1.31*x - 0.127 #eV    vurgaftman_band_2001

class AlInAs(Ternary1):
    name = 'AlInAs'
    elements = ('Al', 'In', 'As')
    binaries = (AlAs, InAs)
    _bowing_Eg_Gamma = 0.7 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.15 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.049 #m_e    vurgaftman_band_2001
    _bowing_Ep = -4.81 #eV    vurgaftman_band_2001
    _bowing_F = -4.44 #vurgaftman_band_2001
    _bowing_VBO = -0.64 #eV    vurgaftman_band_2001
    _bowing_a_c = -1.4 #eV    vurgaftman_band_2001

class GaInAs(Ternary1):
    name = 'GaInAs'
    elements = ('Ga', 'In', 'As')
    binaries = (GaAs, InAs)
    _bowing_Eg_Gamma = 0.477 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 1.4 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.33 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.15 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.0091 #m_e    vurgaftman_band_2001
    _bowing_meff_HH_DOS = -0.145 #m_e    vurgaftman_band_2001
    _bowing_meff_LH_DOS = 0.0202 #m_e    vurgaftman_band_2001
    _bowing_Ep = -1.48 #eV    vurgaftman_band_2001
    _bowing_F = 1.77 #vurgaftman_band_2001
    _bowing_VBO = -0.38 #eV    vurgaftman_band_2001
    _bowing_a_c = 2.61 #eV    vurgaftman_band_2001

#GaAlAs = create_reversed_ternary('GaAlAs', AlGaAs)
#InAlAs = create_reversed_ternary('InAlAs', AlInAs)
#InGaAs = create_reversed_ternary('InGaAs', GaInAs)

# Antimonides
class AlGaSb(Ternary1):
    name = 'AlGaSb'
    elements = ('Al', 'Ga', 'Sb')
    binaries = (AlSb, GaSb)
    _bowing_Delta_SO = 0.3 #eV    vurgaftman_band_2001
    
    @classmethod
    def _bowing_Eg_Gamma(cls, x):
        return 1.22*x - 0.044 #eV    vurgaftman_band_2001

class AlInSb(Ternary1):
    name = 'AlInSb'
    elements = ('Al', 'In', 'Sb')
    binaries = (AlSb, InSb)
    _bowing_Eg_Gamma = 0.43 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.25 #eV    vurgaftman_band_2001

class GaInSb(Ternary1):
    name = 'GaInSb'
    elements = ('Ga', 'In', 'Sb')
    binaries = (GaSb, InSb)
    _bowing_Eg_Gamma = 0.415 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.33 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.4 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.1 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.0092 #m_e    vurgaftman_band_2001
    _bowing_meff_LH_DOS = 0.011 #m_e    vurgaftman_band_2001
    _bowing_F = -6.84 #vurgaftman_band_2001

#GaAlSb = create_reversed_ternary('GaAlSb', AlGaSb)
#InAlSb = create_reversed_ternary('InAlSb', AlInSb)
#InGaSb = create_reversed_ternary('InGaSb', GaInSb)

# Nitride Phosphides
class AlNP(Ternary2):
    name = 'AlNP'
    elements = ('Al', 'N', 'P')
    binaries = (AlN, AlP)

class GaNP(Ternary2):
    name = 'GaNP'
    elements = ('Ga', 'N', 'P')
    binaries = (GaN, GaP)
    _bowing_Eg_Gamma = 3.9 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 10 #eV    vurgaftman_band_2001

class InNP(Ternary2):
    name = 'InNP'
    elements = ('In', 'N', 'P')
    binaries = (InN, InP)
    _bowing_Eg_Gamma = 15 #eV    vurgaftman_band_2001

#AlPN = create_reversed_ternary('AlPN', AlNP)
#GaPN = create_reversed_ternary('GaPN', GaNP)
#InPN = create_reversed_ternary('InPN', InNP)

# Nitride Arsenides
class AlNAs(Ternary2):
    name = 'AlNAs'
    elements = ('Al', 'N', 'As')
    binaries = (AlN, AlAs)

class GaNAs(Ternary2):
    name = 'GaNAs'
    elements = ('Ga', 'N', 'As')
    binaries = (GaN, GaAs)
    
    @classmethod
    def _bowing_Eg_Gamma(cls, x):
        return 120.4 - 100*x #eV    vurgaftman_band_2001

class InNAs(Ternary2):
    name = 'InNAs'
    elements = ('In', 'N', 'As')
    binaries = (InN, InAs)
    _bowing_Eg_Gamma = 4.22 #eV    vurgaftman_band_2001

#AlAsN = create_reversed_ternary('AlAsN', AlNAs)
#GaAsN = create_reversed_ternary('GaAsN', GaNAs)
#InAsN = create_reversed_ternary('InAsN', InNAs)

# Phosphide Arsenides
class AlPAs(Ternary2):
    name = 'AlPAs'
    elements = ('Al', 'P', 'As')
    binaries = (AlP, AlAs)
    _bowing_Eg_Gamma = 0.22 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.22 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.22 #eV    vurgaftman_band_2001

class GaPAs(Ternary2):
    name = 'GaPAs'
    elements = ('Ga', 'P', 'As')
    binaries = (GaP, GaAs)
    _bowing_Eg_Gamma = 0.19 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.24 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.16 #eV    vurgaftman_band_2001

class InPAs(Ternary2):
    name = 'InPAs'
    elements = ('In', 'P', 'As')
    binaries = (InP, InAs)
    _bowing_Eg_Gamma = 0.1 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.27 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.27 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.16 #eV    vurgaftman_band_2001

#AlAsP = create_reversed_ternary('AlAsP', AlPAs)
#GaAsP = create_reversed_ternary('GaAsP', GaPAs)
#InAsP = create_reversed_ternary('InAsP', InPAs)

# Phosphide Antimonides
class AlPSb(Ternary2):
    name = 'AlPSb'
    elements = ('Al', 'P', 'Sb')
    binaries = (AlP, AlSb)
    _bowing_Eg_Gamma = 2.7 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 2.7 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 2.7 #eV    vurgaftman_band_2001

class GaPSb(Ternary2):
    name = 'GaPSb'
    elements = ('Ga', 'P', 'Sb')
    binaries = (GaP, GaSb)
    _bowing_Eg_Gamma = 2.7 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 2.7 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 2.7 #eV    vurgaftman_band_2001

class InPSb(Ternary2):
    name = 'InPSb'
    elements = ('In', 'P', 'Sb')
    binaries = (InP, InSb)
    _bowing_Eg_Gamma = 1.9 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 1.9 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 1.9 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.75 #eV    vurgaftman_band_2001

#AlSbP = create_reversed_ternary('AlSbP', AlPSb)
#GaSbP = create_reversed_ternary('GaSbP', GaPSb)
#InSbP = create_reversed_ternary('InSbP', InPSb)

# Arsenide Antimonides
class AlAsSb(Ternary2):
    name = 'AlAsSb'
    elements = ('Al', 'As', 'Sb')
    binaries = (AlAs, AlSb)
    _bowing_Eg_Gamma = 0.8 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.28 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.28 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.15 #eV    vurgaftman_band_2001
    _bowing_VBO = -1.71 #eV    vurgaftman_band_2001

class GaAsSb(Ternary2):
    name = 'GaAsSb'
    elements = ('Ga', 'As', 'Sb')
    binaries = (GaAs, GaSb)
    _bowing_Eg_Gamma = 1.43 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 1.2 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 1.2 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 0.6 #eV    vurgaftman_band_2001
    _bowing_VBO = -1.06 #eV    vurgaftman_band_2001

class InAsSb(Ternary2):
    name = 'InAsSb'
    elements = ('In', 'As', 'Sb')
    binaries = (InAs, InSb)
    _bowing_Eg_Gamma = 0.67 #eV    vurgaftman_band_2001
    _bowing_Eg_X = 0.6 #eV    vurgaftman_band_2001
    _bowing_Eg_L = 0.6 #eV    vurgaftman_band_2001
    _bowing_Delta_SO = 1.2 #eV    vurgaftman_band_2001
    _bowing_meff_e_Gamma = 0.035 #m_e    vurgaftman_band_2001

#AlSbAs = create_reversed_ternary('AlSbAs', AlAsSb)
#GaSbAs = create_reversed_ternary('GaSbAs', GaAsSb)
#InSbAs = create_reversed_ternary('InSbAs', InAsSb)

ternaries = [AlGaN,  AlInN,  GaInN,
             AlGaP,  AlInP,  GaInP,
             AlGaAs, AlInAs, GaInAs,
             AlGaSb, AlInSb, GaInSb,
             AlNP,   GaNP,   InNP,
             AlNAs,  GaNAs,  InNAs,
             AlPAs,  GaPAs,  InPAs,
             AlPSb,  GaPSb,  InPSb,
             AlAsSb, GaAsSb, InAsSb]

#alternate_ternaries = [GaAlN,  InAlN,  InGaN,
#                       GaAlP,  InAlP,  InGaP,
#                       GaAlAs, InAlAs, InGaAs,
#                       GaAlSb, InAlSb, InGaSb,
#                       AlPN,   GaPN,   InPN,
#                       AlAsN,  GaAsN,  InAsN,
#                       AlAsP,  GaAsP,  InAsP,
#                       AlSbP,  GaSbP,  InSbP,
#                       AlSbAs, GaSbAs, InSbAs]

__all__ = ['ternaries'] #, 'alternate_ternaries']
__all__ += [ternary.name for ternary in ternaries]
#__all__ += [ternary.name for ternary in alternate_ternaries]