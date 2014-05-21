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

from openbandparams.iii_v.quaternary import (Quaternary1, Quaternary2,
    Quaternary3)
from openbandparams.iii_v.zinc_blende.binary import (AlN, AlP, AlAs, AlSb,
    GaN, GaP, GaAs, GaSb, InN, InP, InAs, InSb)
from openbandparams.iii_v.zinc_blende.ternary import (AlNP, AlNAs, AlPAs,
    AlPSb, AlAsSb, GaNP, GaNAs, GaPAs, GaPSb, GaAsSb, InNP, InNAs, InPAs,
    InPSb, InAsSb, AlGaN, AlInN, GaInN, AlGaP, AlInP, GaInP, AlGaAs, AlInAs,
    GaInAs, AlGaSb, AlInSb, GaInSb)


# Type 1: AB_{x}C_{y}D_{1-x-y}
# binaryies = (AB, AC, AD)
# ternaries = (ABC, ABD ,ACD)

class AlNPAs(Quaternary1):
    name = 'AlNPAs'
    elements = ('Al', 'N', 'P', 'As')
    binaries = (AlN, AlP, AlAs)
    ternaries = (AlNP, AlNAs, AlPAs)


# class AlNPSb(Quaternary1):
#    name = 'AlNPSb'
#    elements = ('Al', 'N', 'P', 'Sb')
#    binaries = (AlN, AlP, AlSb)
#    ternaries = (AlNP, AlNSb, AlPSb)


# class AlNAsSb(Quaternary1):
#    name = 'AlNAsSb'
#    elements = ('Al', 'N', 'As', 'Sb')
#    binaries = (AlN, AlAs, AlSb)
#    ternaries = (AlNAs, AlNSb, AlAsSb)


class AlPAsSb(Quaternary1):
    name = 'AlPAsSb'
    elements = ('Al', 'P', 'As', 'Sb')
    binaries = (AlP, AlAs, AlSb)
    ternaries = (AlPAs, AlPSb, AlAsSb)


class GaNPAs(Quaternary1):
    name = 'GaNPAs'
    elements = ('Ga', 'N', 'P', 'As')
    binaries = (GaN, GaP, GaAs)
    ternaries = (GaNP, GaNAs, GaPAs)


# class GaNPSb(Quaternary1):
#    name = 'GaNPSb'
#    elements = ('Ga', 'N', 'P', 'Sb')
#    binaries = (GaN, GaP, GaSb)
#    ternaries = (GaNP, GaNSb, GaPSb)


# class GaNAsSb(Quaternary1):
#    name = 'GaNAsSb'
#    elements = ('Ga', 'N', 'As', 'Sb')
#    binaries = (GaN, GaAs, GaSb)
#    ternaries = (GaNAs, GaNSb, GaAsSb)


class GaPAsSb(Quaternary1):
    name = 'GaPAsSb'
    elements = ('Ga', 'P', 'As', 'Sb')
    binaries = (GaP, GaAs, GaSb)
    ternaries = (GaPAs, GaPSb, GaAsSb)


class InNPAs(Quaternary1):
    name = 'InNPAs'
    elements = ('In', 'N', 'P', 'As')
    binaries = (InN, InP, InAs)
    ternaries = (InNP, InNAs, InPAs)


# class InNPSb(Quaternary1):
#    name = 'InNPSb'
#    elements = ('In', 'N', 'P', 'Sb')
#    binaries = (InN, InP, InSb)
#    ternaries = (InNP, InNSb, InPSb)


# class InNAsSb(Quaternary1):
#    name = 'InNAsSb'
#    elements = ('In', 'N', 'As', 'Sb')
#    binaries = (InN, InAs, InSb)
#    ternaries = (InNAs, InNSb, InAsSb)


class InPAsSb(Quaternary1):
    name = 'InPAsSb'
    elements = ('In', 'P', 'As', 'Sb')
    binaries = (InP, InAs, InSb)
    ternaries = (InPAs, InPSb, InAsSb)


# Type 2: A_{x}B_{y}C_{1-x-y}D
# binaries = (AD, BD, CD)
# ternaries = (ABD, ACD, BCD)

class AlGaInN(Quaternary2):
    name = 'AlGaInN'
    elements = ('Al', 'Ga', 'In', 'N')
    binaries = (AlN, GaN, InN)
    ternaries = (AlGaN, AlInN, GaInN)


class AlGaInP(Quaternary2):
    name = 'AlGaInP'
    elements = ('Al', 'Ga', 'In', 'P')
    binaries = (AlP, GaP, InP)
    ternaries = (AlGaP, AlInP, GaInP)


class AlGaInAs(Quaternary2):
    name = 'AlGaInAs'
    elements = ('Al', 'Ga', 'In', 'As')
    binaries = (AlAs, GaAs, InAs)
    ternaries = (AlGaAs, AlInAs, GaInAs)


class AlGaInSb(Quaternary2):
    name = 'AlGaInSb'
    elements = ('Al', 'Ga', 'In', 'Sb')
    binaries = (AlSb, GaSb, InSb)
    ternaries = (AlGaSb, AlInSb, GaInSb)


# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# binaries = (AC, AD, BC, BD)
# ternaries = (ABC, ABD, ACD, BCD)

class AlGaNP(Quaternary3):
    name = 'AlGaNP'
    elements = ('Al', 'Ga', 'N', 'P')
    binaries = (AlN, AlP, GaN, GaP)
    ternaries = (AlGaN, AlGaP, AlNP, GaNP)


class AlGaNAs(Quaternary3):
    name = 'AlGaNAs'
    elements = ('Al', 'Ga', 'N', 'As')
    binaries = (AlN, AlAs, GaN, GaAs)
    ternaries = (AlGaN, AlGaAs, AlNAs, GaNAs)


# class AlGaNSb(Quaternary3):
#    name = 'AlGaNSb'
#    elements = ('Al', 'Ga', 'N', 'Sb')
#    binaries = (AlN, AlSb, GaN, GaSb)
#    ternaries = (AlGaN, AlGaSb, AlNSb, GaNSb)


class AlGaPAs(Quaternary3):
    name = 'AlGaPAs'
    elements = ('Al', 'Ga', 'P', 'As')
    binaries = (AlP, AlAs, GaP, GaAs)
    ternaries = (AlGaP, AlGaAs, AlPAs, GaPAs)


class AlGaPSb(Quaternary3):
    name = 'AlGaPSb'
    elements = ('Al', 'Ga', 'P', 'Sb')
    binaries = (AlP, AlSb, GaP, GaSb)
    ternaries = (AlGaP, AlGaSb, AlPSb, GaPSb)


class AlGaAsSb(Quaternary3):
    name = 'AlGaAsSb'
    elements = ('Al', 'Ga', 'As', 'Sb')
    binaries = (AlAs, AlSb, GaAs, GaSb)
    ternaries = (AlGaAs, AlGaSb, AlAsSb, GaAsSb)


class AlInNP(Quaternary3):
    name = 'AlInNP'
    elements = ('Al', 'In', 'N', 'P')
    binaries = (AlN, AlP, InN, InP)
    ternaries = (AlInN, AlInP, AlNP, InNP)


class AlInNAs(Quaternary3):
    name = 'AlInNAs'
    elements = ('Al', 'In', 'N', 'As')
    binaries = (AlN, AlAs, InN, InAs)
    ternaries = (AlInN, AlInAs, AlNAs, InNAs)


# class AlInNSb(Quaternary3):
#    name = 'AlInNSb'
#    elements = ('Al', 'In', 'N', 'Sb')
#    binaries = (AlN, AlSb, InN, InSb)
#    ternaries = (AlInN, AlInSb, AlNSb, InNSb)


class AlInPAs(Quaternary3):
    name = 'AlInPAs'
    elements = ('Al', 'In', 'P', 'As')
    binaries = (AlP, AlAs, InP, InAs)
    ternaries = (AlInP, AlInAs, AlPAs, InPAs)


class AlInPSb(Quaternary3):
    name = 'AlInPSb'
    elements = ('Al', 'In', 'P', 'Sb')
    binaries = (AlP, AlSb, InP, InSb)
    ternaries = (AlInP, AlInSb, AlPSb, InPSb)


class AlInAsSb(Quaternary3):
    name = 'AlInAsSb'
    elements = ('Al', 'In', 'As', 'Sb')
    binaries = (AlAs, AlSb, InAs, InSb)
    ternaries = (AlInAs, AlInSb, AlAsSb, InAsSb)


class GaInNP(Quaternary3):
    name = 'GaInNP'
    elements = ('Ga', 'In', 'N', 'P')
    binaries = (GaN, GaP, InN, InP)
    ternaries = (GaInN, GaInP, GaNP, InNP)


class GaInNAs(Quaternary3):
    name = 'GaInNAs'
    elements = ('Ga', 'In', 'N', 'As')
    binaries = (GaN, GaAs, InN, InAs)
    ternaries = (GaInN, GaInAs, GaNAs, InNAs)


# class GaInNSb(Quaternary3):
#    name = 'GaInNSb'
#    elements = ('Ga', 'In', 'N', 'Sb')
#    binaries = (GaN, GaSb, InN, InSb)
#    ternaries = (GaInN, GaInSb, GaNSb, InNSb)


class GaInPAs(Quaternary3):
    name = 'GaInPAs'
    elements = ('Ga', 'In', 'P', 'As')
    binaries = (GaP, GaAs, InP, InAs)
    ternaries = (GaInP, GaInAs, GaPAs, InPAs)


class GaInPSb(Quaternary3):
    name = 'GaInPSb'
    elements = ('Ga', 'In', 'P', 'Sb')
    binaries = (GaP, GaSb, InP, InSb)
    ternaries = (GaInP, GaInSb, GaPSb, InPSb)


class GaInAsSb(Quaternary3):
    name = 'GaInAsSb'
    elements = ('Ga', 'In', 'As', 'Sb')
    binaries = (GaAs, GaSb, InAs, InSb)
    ternaries = (GaInAs, GaInSb, GaAsSb, InAsSb)

quaternaries = [  # Type 1: AB_{x}C_{y}D_{1-x-y}
                AlNPAs,  # AlNPSb, AlNAsSb,
                AlPAsSb,
                GaNPAs,  # GaNPSb, GaNAsSb,
                GaPAsSb,
                InNPAs,  # InNPSb, InNAsSb,
                InPAsSb,
                # Type 2: B_{x}C_{y}D_{1-x-y}A
                AlGaInN, AlGaInP, AlGaInAs, AlGaInSb,
                # Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
                AlGaNP, AlInNP, GaInNP,
                AlGaNAs, AlInNAs, GaInNAs,
                AlGaPAs, AlInPAs, GaInPAs,
                AlGaPSb, AlInPSb, GaInPSb,
                AlGaAsSb, AlInAsSb, GaInAsSb]

__all__ = ['quaternaries']
__all__ += [quaternary.name for quaternary in quaternaries]
