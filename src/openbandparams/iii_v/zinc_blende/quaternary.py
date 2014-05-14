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
from openbandparams.iii_v.quaternary import (Quaternary1, Quaternary2,
                                             Quaternary3)
from openbandparams.iii_v.zinc_blende.binary import *
from openbandparams.iii_v.zinc_blende.ternary import *



# Type 1: AB_{x}C_{y}D_{1-x-y}
# binary1 = AB
# binary2 = AC
# binary3 = AD
# ternary1 = ABC
# ternary2 = ABD
# ternary3 = ACD

class AlNPAs(Quaternary1):
    name = 'AlNPAs'
    elements = ('Al', 'N', 'P', 'As')
    binaries = (AlN, AlP, AlAs)
    ternaries = (AlNP, AlNAs, AlPAs)
    element1 = 'Al'
    element2 = 'N'
    element3 = 'P'
    element4 = 'As'
    binary1 = AlN
    binary2 = AlP
    binary3 = AlAs
    ternary1 = AlNP
    ternary2 = AlNAs
    ternary3 = AlPAs

#class AlNPSb(Quaternary1):
#    name = 'AlNPSb'
#    elements = ('Al', 'N', 'P', 'Sb')
#    binaries = (AlN, AlP, AlSb)
#    ternaries = (AlNP, AlNSb, AlPSb)
#    element1 = 'Al'
#    element2 = 'N'
#    element3 = 'P'
#    element4 = 'Sb'
#    binary1 = AlN
#    binary2 = AlP
#    binary3 = AlSb
#    ternary1 = AlNP
#    ternary2 = AlNSb
#    ternary3 = AlPSb

#class AlNAsSb(Quaternary1):
#    name = 'AlNAsSb'
#    elements = ('Al', 'N', 'As', 'Sb')
#    binaries = (AlN, AlAs, AlSb)
#    ternaries = (AlNAs, AlNSb, AlAsSb)
#    element1 = 'Al'
#    element2 = 'N'
#    element3 = 'As'
#    element4 = 'Sb'
#    binary1 = AlN
#    binary2 = AlAs
#    binary3 = AlSb
#    ternary1 = AlNAs
#    ternary2 = AlNSb
#    ternary3 = AlAsSb

class AlPAsSb(Quaternary1):
    name = 'AlPAsSb'
    elements = ('Al', 'P', 'As', 'Sb')
    binaries = (AlP, AlAs, AlSb)
    ternaries = (AlPAs, AlPSb, AlAsSb)
    element1 = 'Al'
    element2 = 'P'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = AlP
    binary2 = AlAs
    binary3 = AlSb
    ternary1 = AlPAs
    ternary2 = AlPSb
    ternary3 = AlAsSb

class GaNPAs(Quaternary1):
    name = 'GaNPAs'
    elements = ('Ga', 'N', 'P', 'As')
    binaries = (GaN, GaP, GaAs)
    ternaries = (GaNP, GaNAs, GaPAs)
    element1 = 'Ga'
    element2 = 'N'
    element3 = 'P'
    element4 = 'As'
    binary1 = GaN
    binary2 = GaP
    binary3 = GaAs
    ternary1 = GaNP
    ternary2 = GaNAs
    ternary3 = GaPAs

#class GaNPSb(Quaternary1):
#    name = 'GaNPSb'
#    elements = ('Ga', 'N', 'P', 'Sb')
#    binaries = (GaN, GaP, GaSb)
#    ternaries = (GaNP, GaNSb, GaPSb)
#    element1 = 'Ga'
#    element2 = 'N'
#    element3 = 'P'
#    element4 = 'Sb'
#    binary1 = GaN
#    binary2 = GaP
#    binary3 = GaSb
#    ternary1 = GaNP
#    ternary2 = GaNSb
#    ternary3 = GaPSb

#class GaNAsSb(Quaternary1):
#    name = 'GaNAsSb'
#    elements = ('Ga', 'N', 'As', 'Sb')
#    binaries = (GaN, GaAs, GaSb)
#    ternaries = (GaNAs, GaNSb, GaAsSb)
#    element1 = 'Ga'
#    element2 = 'N'
#    element3 = 'As'
#    element4 = 'Sb'
#    binary1 = GaN
#    binary2 = GaAs
#    binary3 = GaSb
#    ternary1 = GaNAs
#    ternary2 = GaNSb
#    ternary3 = GaAsSb

class GaPAsSb(Quaternary1):
    name = 'GaPAsSb'
    elements = ('Ga', 'P', 'As', 'Sb')
    binaries = (GaP, GaAs, GaSb)
    ternaries = (GaPAs, GaPSb, GaAsSb)
    element1 = 'Ga'
    element2 = 'P'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = GaP
    binary2 = GaAs
    binary3 = GaSb
    ternary1 = GaPAs
    ternary2 = GaPSb
    ternary3 = GaAsSb

class InNPAs(Quaternary1):
    name = 'InNPAs'
    elements = ('In', 'N', 'P', 'As')
    binaries = (InN, InP, InAs)
    ternaries = (InNP, InNAs, InPAs)
    element1 = 'In'
    element2 = 'N'
    element3 = 'P'
    element4 = 'As'
    binary1 = InN
    binary2 = InP
    binary3 = InAs
    ternary1 = InNP
    ternary2 = InNAs
    ternary3 = InPAs

#class InNPSb(Quaternary1):
#    name = 'InNPSb'
#    elements = ('In', 'N', 'P', 'Sb')
#    binaries = (InN, InP, InSb)
#    ternaries = (InNP, InNSb, InPSb)
#    element1 = 'In'
#    element2 = 'N'
#    element3 = 'P'
#    element4 = 'Sb'
#    binary1 = InN
#    binary2 = InP
#    binary3 = InSb
#    ternary1 = InNP
#    ternary2 = InNSb
#    ternary3 = InPSb

#class InNAsSb(Quaternary1):
#    name = 'InNAsSb'
#    elements = ('In', 'N', 'As', 'Sb')
#    binaries = (InN, InAs, InSb)
#    ternaries = (InNAs, InNSb, InAsSb)
#    element1 = 'In'
#    element2 = 'N'
#    element3 = 'As'
#    element4 = 'Sb'
#    binary1 = InN
#    binary2 = InAs
#    binary3 = InSb
#    ternary1 = InNAs
#    ternary2 = InNSb
#    ternary3 = InAsSb

class InPAsSb(Quaternary1):
    name = 'InPAsSb'
    elements = ('In', 'P', 'As', 'Sb')
    binaries = (InP, InAs, InSb)
    ternaries = (InPAs, InPSb, InAsSb)
    element1 = 'In'
    element2 = 'P'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = InP
    binary2 = InAs
    binary3 = InSb
    ternary1 = InPAs
    ternary2 = InPSb
    ternary3 = InAsSb

# Type 2: A_{x}B_{y}C_{1-x-y}D
# binary1 = AD
# binary2 = BD
# binary3 = CD
# ternary1 = ABD
# ternary2 = ACD
# ternary3 = BCD

class AlGaInN(Quaternary2):
    name = 'AlGaInN'
    elements = ('Al', 'Ga', 'In', 'N')
    binaries = (AlN, GaN, InN)
    ternaries = (AlGaN, AlInN, GaInN)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'In'
    element4 = 'N'
    binary1 = AlN
    binary2 = GaN
    binary3 = InN
    ternary1 = AlGaN
    ternary2 = AlInN
    ternary3 = GaInN

class AlGaInP(Quaternary2):
    name = 'AlGaInP'
    elements = ('Al', 'Ga', 'In', 'P')
    binaries = (AlP, GaP, InP)
    ternaries = (AlGaP, AlInP, GaInP)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'In'
    element4 = 'P'
    binary1 = AlP
    binary2 = GaP
    binary3 = InP
    ternary1 = AlGaP
    ternary2 = AlInP
    ternary3 = GaInP

class AlGaInAs(Quaternary2):
    name = 'AlGaInAs'
    elements = ('Al', 'Ga', 'In', 'As')
    binaries = (AlAs, GaAs, InAs)
    ternaries = (AlGaAs, AlInAs, GaInAs)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'In'
    element4 = 'As'
    binary1 = AlAs
    binary2 = GaAs
    binary3 = InAs
    ternary1 = AlGaAs
    ternary2 = AlInAs
    ternary3 = GaInAs

class AlGaInSb(Quaternary2):
    name = 'AlGaInSb'
    elements = ('Al', 'Ga', 'In', 'Sb')
    binaries = (AlSb, GaSb, InSb)
    ternaries = (AlGaSb, AlInSb, GaInSb)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'In'
    element4 = 'Sb'
    binary1 = AlSb
    binary2 = GaSb
    binary3 = InSb
    ternary1 = AlGaSb
    ternary2 = AlInSb
    ternary3 = GaInSb

# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# binary1 = AC
# binary2 = AD
# binary3 = BC
# binary4 = BD
# ternary1 = ABC
# ternary2 = ABD
# ternary3 = ACD
# ternary4 = BCD

class AlGaNP(Quaternary3):
    name = 'AlGaNP'
    elements = ('Al', 'Ga', 'N', 'P')
    binaries = (AlN, AlP, GaN, GaP)
    ternaries = (AlGaN, AlGaP, AlNP, GaNP)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'N'
    element4 = 'P'
    binary1 = AlN
    binary2 = AlP
    binary3 = GaN
    binary4 = GaP
    ternary1 = AlGaN
    ternary2 = AlGaP
    ternary3 = AlNP
    ternary4 = GaNP

class AlGaNAs(Quaternary3):
    name = 'AlGaNAs'
    elements = ('Al', 'Ga', 'N', 'As')
    binaries = (AlN, AlAs, GaN, GaAs)
    ternaries = (AlGaN, AlGaAs, AlNAs, GaNAs)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'N'
    element4 = 'As'
    binary1 = AlN
    binary2 = AlAs
    binary3 = GaN
    binary4 = GaAs
    ternary1 = AlGaN
    ternary2 = AlGaAs
    ternary3 = AlNAs
    ternary4 = GaNAs

#class AlGaNSb(Quaternary3):
#    name = 'AlGaNSb'
#    elements = ('Al', 'Ga', 'N', 'Sb')
#    binaries = (AlN, AlSb, GaN, GaSb)
#    ternaries = (AlGaN, AlGaSb, AlNSb, GaNSb)
#    element1 = 'Al'
#    element2 = 'Ga'
#    element3 = 'N'
#    element4 = 'Sb'
#    binary1 = AlN
#    binary2 = AlSb
#    binary3 = GaN
#    binary4 = GaSb
#    ternary1 = AlGaN
#    ternary2 = AlGaSb
#    ternary3 = AlNSb
#    ternary4 = GaNSb

class AlGaPAs(Quaternary3):
    name = 'AlGaPAs'
    elements = ('Al', 'Ga', 'P', 'As')
    binaries = (AlP, AlAs, GaP, GaAs)
    ternaries = (AlGaP, AlGaAs, AlPAs, GaPAs)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'P'
    element4 = 'As'
    binary1 = AlP
    binary2 = AlAs
    binary3 = GaP
    binary4 = GaAs
    ternary1 = AlGaP
    ternary2 = AlGaAs
    ternary3 = AlPAs
    ternary4 = GaPAs

class AlGaPSb(Quaternary3):
    name = 'AlGaPSb'
    elements = ('Al', 'Ga', 'P', 'Sb')
    binaries = (AlP, AlSb, GaP, GaSb)
    ternaries = (AlGaP, AlGaSb, AlPSb, GaPSb)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'P'
    element4 = 'Sb'
    binary1 = AlP
    binary2 = AlSb
    binary3 = GaP
    binary4 = GaSb
    ternary1 = AlGaP
    ternary2 = AlGaSb
    ternary3 = AlPSb
    ternary4 = GaPSb

class AlGaAsSb(Quaternary3):
    name = 'AlGaAsSb'
    elements = ('Al', 'Ga', 'As', 'Sb')
    binaries = (AlAs, AlSb, GaAs, GaSb)
    ternaries = (AlGaAs, AlGaSb, AlAsSb, GaAsSb)
    element1 = 'Al'
    element2 = 'Ga'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = AlAs
    binary2 = AlSb
    binary3 = GaAs
    binary4 = GaSb
    ternary1 = AlGaAs
    ternary2 = AlGaSb
    ternary3 = AlAsSb
    ternary4 = GaAsSb

class AlInNP(Quaternary3):
    name = 'AlInNP'
    elements = ('Al', 'In', 'N', 'P')
    binaries = (AlN, AlP, InN, InP)
    ternaries = (AlInN, AlInP, AlNP, InNP)
    element1 = 'Al'
    element2 = 'In'
    element3 = 'N'
    element4 = 'P'
    binary1 = AlN
    binary2 = AlP
    binary3 = InN
    binary4 = InP
    ternary1 = AlInN
    ternary2 = AlInP
    ternary3 = AlNP
    ternary4 = InNP

class AlInNAs(Quaternary3):
    name = 'AlInNAs'
    elements = ('Al', 'In', 'N', 'As')
    binaries = (AlN, AlAs, InN, InAs)
    ternaries = (AlInN, AlInAs, AlNAs, InNAs)
    element1 = 'Al'
    element2 = 'In'
    element3 = 'N'
    element4 = 'As'
    binary1 = AlN
    binary2 = AlAs
    binary3 = InN
    binary4 = InAs
    ternary1 = AlInN
    ternary2 = AlInAs
    ternary3 = AlNAs
    ternary4 = InNAs

#class AlInNSb(Quaternary3):
#    name = 'AlInNSb'
#    elements = ('Al', 'In', 'N', 'Sb')
#    binaries = (AlN, AlSb, InN, InSb)
#    ternaries = (AlInN, AlInSb, AlNSb, InNSb)
#    element1 = 'Al'
#    element2 = 'In'
#    element3 = 'N'
#    element4 = 'Sb'
#    binary1 = AlN
#    binary2 = AlSb
#    binary3 = InN
#    binary4 = InSb
#    ternary1 = AlInN
#    ternary2 = AlInSb
#    ternary3 = AlNSb
#    ternary4 = InNSb

class AlInPAs(Quaternary3):
    name = 'AlInPAs'
    elements = ('Al', 'In', 'P', 'As')
    binaries = (AlP, AlAs, InP, InAs)
    ternaries = (AlInP, AlInAs, AlPAs, InPAs)
    element1 = 'Al'
    element2 = 'In'
    element3 = 'P'
    element4 = 'As'
    binary1 = AlP
    binary2 = AlAs
    binary3 = InP
    binary4 = InAs
    ternary1 = AlInP
    ternary2 = AlInAs
    ternary3 = AlPAs
    ternary4 = InPAs

class AlInPSb(Quaternary3):
    name = 'AlInPSb'
    elements = ('Al', 'In', 'P', 'Sb')
    binaries = (AlP, AlSb, InP, InSb)
    ternaries = (AlInP, AlInSb, AlPSb, InPSb)
    element1 = 'Al'
    element2 = 'In'
    element3 = 'P'
    element4 = 'Sb'
    binary1 = AlP
    binary2 = AlSb
    binary3 = InP
    binary4 = InSb
    ternary1 = AlInP
    ternary2 = AlInSb
    ternary3 = AlPSb
    ternary4 = InPSb

class AlInAsSb(Quaternary3):
    name = 'AlInAsSb'
    elements = ('Al', 'In', 'As', 'Sb')
    binaries = (AlAs, AlSb, InAs, InSb)
    ternaries = (AlInAs, AlInSb, AlAsSb, InAsSb)
    element1 = 'Al'
    element2 = 'In'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = AlAs
    binary2 = AlSb
    binary3 = InAs
    binary4 = InSb
    ternary1 = AlInAs
    ternary2 = AlInSb
    ternary3 = AlAsSb
    ternary4 = InAsSb

class GaInNP(Quaternary3):
    name = 'GaInNP'
    elements = ('Ga', 'In', 'N', 'P')
    binaries = (GaN, GaP, InN, InP)
    ternaries = (GaInN, GaInP, GaNP, InNP)
    element1 = 'Ga'
    element2 = 'In'
    element3 = 'N'
    element4 = 'P'
    binary1 = GaN
    binary2 = GaP
    binary3 = InN
    binary4 = InP
    ternary1 = GaInN
    ternary2 = GaInP
    ternary3 = GaNP
    ternary4 = InNP

class GaInNAs(Quaternary3):
    name = 'GaInNAs'
    elements = ('Ga', 'In', 'N', 'As')
    binaries = (GaN, GaAs, InN, InAs)
    ternaries = (GaInN, GaInAs, GaNAs, InNAs)
    element1 = 'Ga'
    element2 = 'In'
    element3 = 'N'
    element4 = 'As'
    binary1 = GaN
    binary2 = GaAs
    binary3 = InN
    binary4 = InAs
    ternary1 = GaInN
    ternary2 = GaInAs
    ternary3 = GaNAs
    ternary4 = InNAs

#class GaInNSb(Quaternary3):
#    name = 'GaInNSb'
#    elements = ('Ga', 'In', 'N', 'Sb')
#    binaries = (GaN, GaSb, InN, InSb)
#    ternaries = (GaInN, GaInSb, GaNSb, InNSb)
#    element1 = 'Ga'
#    element2 = 'In'
#    element3 = 'N'
#    element4 = 'Sb'
#    binary1 = GaN
#    binary2 = GaSb
#    binary3 = InN
#    binary4 = InSb
#    ternary1 = GaInN
#    ternary2 = GaInSb
#    ternary3 = GaNSb
#    ternary4 = InNSb

class GaInPAs(Quaternary3):
    name = 'GaInPAs'
    elements = ('Ga', 'In', 'P', 'As')
    binaries = (GaP, GaAs, InP, InAs)
    ternaries = (GaInP, GaInAs, GaPAs, InPAs)
    element1 = 'Ga'
    element2 = 'In'
    element3 = 'P'
    element4 = 'As'
    binary1 = GaP
    binary2 = GaAs
    binary3 = InP
    binary4 = InAs
    ternary1 = GaInP
    ternary2 = GaInAs
    ternary3 = GaPAs
    ternary4 = InPAs

class GaInPSb(Quaternary3):
    name = 'GaInPSb'
    elements = ('Ga', 'In', 'P', 'Sb')
    binaries = (GaP, GaSb, InP, InSb)
    ternaries = (GaInP, GaInSb, GaPSb, InPSb)
    element1 = 'Ga'
    element2 = 'In'
    element3 = 'P'
    element4 = 'Sb'
    binary1 = GaP
    binary2 = GaSb
    binary3 = InP
    binary4 = InSb
    ternary1 = GaInP
    ternary2 = GaInSb
    ternary3 = GaPSb
    ternary4 = InPSb

class GaInAsSb(Quaternary3):
    name = 'GaInAsSb'
    elements = ('Ga', 'In', 'As', 'Sb')
    binaries = (GaAs, GaSb, InAs, InSb)
    ternaries = (GaInAs, GaInSb, GaAsSb, InAsSb)
    element1 = 'Ga'
    element2 = 'In'
    element3 = 'As'
    element4 = 'Sb'
    binary1 = GaAs
    binary2 = GaSb
    binary3 = InAs
    binary4 = InSb
    ternary1 = GaInAs
    ternary2 = GaInSb
    ternary3 = GaAsSb
    ternary4 = InAsSb

quaternaires = [# Type 1: AB_{x}C_{y}D_{1-x-y}
                AlNPAs,  #AlNPSb, AlNAsSb,
                AlPAsSb,
                GaNPAs, #GaNPSb, GaNAsSb,
                GaPAsSb,
                InNPAs, #InNPSb, InNAsSb,
                InPAsSb,
                # Type 2: B_{x}C_{y}D_{1-x-y}A
                AlGaInN, AlGaInP, AlGaInAs, AlGaInSb,
                # Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
                AlGaNP, AlInNP, GaInNP,
                AlGaNAs, AlInNAs, GaInNAs,
                AlGaPAs, AlInPAs, GaInPAs,
                AlGaPSb, AlInPSb, GaInPSb,
                AlGaAsSb, AlInAsSb, GaInAsSb]