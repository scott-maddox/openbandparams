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

from .iii_v_zinc_blende_quaternary import IIIVZincBlendeQuaternary
from .iii_v_zinc_blende_ternaries import (AlGaN, AlInN, GaInN,
                                          AlGaP, AlInP, GaInP,
                                          AlGaAs, AlInAs, GaInAs,
                                          AlGaSb, AlInSb, GaInSb,
                                          AlNP, GaNP, InNP,
                                          AlNAs, GaNAs, InNAs,
                                          AlPAs, GaPAs, InPAs,
                                          AlPSb, GaPSb, InPSb,
                                          AlAsSb, GaAsSb, InAsSb)


# Type 1: AB_{x}C_{y}D_{1-x-y}
# binaries = (AB, AC, AD)
# ternaries = (ABC, ABD ,ACD)

AlNPAs = IIIVZincBlendeQuaternary(
    name='AlNPAs',
    elements=('Al', 'N', 'P', 'As'),
    ternaries=(AlNP, AlNAs, AlPAs))


# AlNPSb = IIIVZincBlendeQuaternary(
#    name='AlNPSb',
#    elements=('Al', 'N', 'P', 'Sb'),
#    ternaries=(AlNP, AlNSb, AlPSb))


# AlNAsSb = IIIVZincBlendeQuaternary(
#    name='AlNAsSb',
#    elements=('Al', 'N', 'As', 'Sb'),
#    ternaries=(AlNAs, AlNSb, AlAsSb))


AlPAsSb = IIIVZincBlendeQuaternary(
    name='AlPAsSb',
    elements=('Al', 'P', 'As', 'Sb'),
    ternaries=(AlPAs, AlPSb, AlAsSb))


GaNPAs = IIIVZincBlendeQuaternary(
    name='GaNPAs',
    elements=('Ga', 'N', 'P', 'As'),
    ternaries=(GaNP, GaNAs, GaPAs))


# GaNPSb = IIIVZincBlendeQuaternary(
#    name='GaNPSb',
#    elements=('Ga', 'N', 'P', 'Sb'),
#    ternaries=(GaNP, GaNSb, GaPSb))


# GaNAsSb = IIIVZincBlendeQuaternary(
#    name='GaNAsSb',
#    elements=('Ga', 'N', 'As', 'Sb'),
#    ternaries=(GaNAs, GaNSb, GaAsSb))


GaPAsSb = IIIVZincBlendeQuaternary(
    name='GaPAsSb',
    elements=('Ga', 'P', 'As', 'Sb'),
    ternaries=(GaPAs, GaPSb, GaAsSb))


InNPAs = IIIVZincBlendeQuaternary(
    name='InNPAs',
    elements=('In', 'N', 'P', 'As'),
    ternaries=(InNP, InNAs, InPAs))


# InNPSb = IIIVZincBlendeQuaternary(
#    name='InNPSb',
#    elements=('In', 'N', 'P', 'Sb'),
#    ternaries=(InNP, InNSb, InPSb))


# InNAsSb = IIIVZincBlendeQuaternary(
#    name='InNAsSb',
#    elements=('In', 'N', 'As', 'Sb'),
#    ternaries=(InNAs, InNSb, InAsSb))


InPAsSb = IIIVZincBlendeQuaternary(
    name='InPAsSb',
    elements=('In', 'P', 'As', 'Sb'),
    ternaries=(InPAs, InPSb, InAsSb))


# Type 2: A_{x}B_{y}C_{1-x-y}D
# ternaries = (ABD, ACD, BCD)

AlGaInN = IIIVZincBlendeQuaternary(
    name='AlGaInN',
    elements=('Al', 'Ga', 'In', 'N'),
    ternaries=(AlGaN, AlInN, GaInN))


AlGaInP = IIIVZincBlendeQuaternary(
    name='AlGaInP',
    elements=('Al', 'Ga', 'In', 'P'),
    ternaries=(AlGaP, AlInP, GaInP))


AlGaInAs = IIIVZincBlendeQuaternary(
    name='AlGaInAs',
    elements=('Al', 'Ga', 'In', 'As'),
    ternaries=(AlGaAs, AlInAs, GaInAs))


AlGaInSb = IIIVZincBlendeQuaternary(
    name='AlGaInSb',
    elements=('Al', 'Ga', 'In', 'Sb'),
    ternaries=(AlGaSb, AlInSb, GaInSb))


# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# ternaries = (ABC, ABD, ACD, BCD)

AlGaNP = IIIVZincBlendeQuaternary(
    name='AlGaNP',
    elements=('Al', 'Ga', 'N', 'P'),
    ternaries=(AlGaN, AlGaP, AlNP, GaNP))


AlGaNAs = IIIVZincBlendeQuaternary(
    name='AlGaNAs',
    elements=('Al', 'Ga', 'N', 'As'),
    ternaries=(AlGaN, AlGaAs, AlNAs, GaNAs))


# AlGaNSb = IIIVZincBlendeQuaternary(
#    name='AlGaNSb',
#    elements=('Al', 'Ga', 'N', 'Sb'),
#    ternaries=(AlGaN, AlGaSb, AlNSb, GaNSb))


AlGaPAs = IIIVZincBlendeQuaternary(
    name='AlGaPAs',
    elements=('Al', 'Ga', 'P', 'As'),
    ternaries=(AlGaP, AlGaAs, AlPAs, GaPAs))


AlGaPSb = IIIVZincBlendeQuaternary(
    name='AlGaPSb',
    elements=('Al', 'Ga', 'P', 'Sb'),
    ternaries=(AlGaP, AlGaSb, AlPSb, GaPSb))


AlGaAsSb = IIIVZincBlendeQuaternary(
    name='AlGaAsSb',
    elements=('Al', 'Ga', 'As', 'Sb'),
    ternaries=(AlGaAs, AlGaSb, AlAsSb, GaAsSb))


AlInNP = IIIVZincBlendeQuaternary(
    name='AlInNP',
    elements=('Al', 'In', 'N', 'P'),
    ternaries=(AlInN, AlInP, AlNP, InNP))


AlInNAs = IIIVZincBlendeQuaternary(
    name='AlInNAs',
    elements=('Al', 'In', 'N', 'As'),
    ternaries=(AlInN, AlInAs, AlNAs, InNAs))


# AlInNSb = IIIVZincBlendeQuaternary(
#    name='AlInNSb',
#    elements=('Al', 'In', 'N', 'Sb'),
#    ternaries=(AlInN, AlInSb, AlNSb, InNSb))


AlInPAs = IIIVZincBlendeQuaternary(
    name='AlInPAs',
    elements=('Al', 'In', 'P', 'As'),
    ternaries=(AlInP, AlInAs, AlPAs, InPAs))


AlInPSb = IIIVZincBlendeQuaternary(
    name='AlInPSb',
    elements=('Al', 'In', 'P', 'Sb'),
    ternaries=(AlInP, AlInSb, AlPSb, InPSb))


AlInAsSb = IIIVZincBlendeQuaternary(
    name='AlInAsSb',
    elements=('Al', 'In', 'As', 'Sb'),
    ternaries=(AlInAs, AlInSb, AlAsSb, InAsSb))


GaInNP = IIIVZincBlendeQuaternary(
    name='GaInNP',
    elements=('Ga', 'In', 'N', 'P'),
    ternaries=(GaInN, GaInP, GaNP, InNP))


GaInNAs = IIIVZincBlendeQuaternary(
    name='GaInNAs',
    elements=('Ga', 'In', 'N', 'As'),
    ternaries=(GaInN, GaInAs, GaNAs, InNAs))


# GaInNSb = IIIVZincBlendeQuaternary(
#    name='GaInNSb',
#    elements=('Ga', 'In', 'N', 'Sb'),
#    ternaries=(GaInN, GaInSb, GaNSb, InNSb))


GaInPAs = IIIVZincBlendeQuaternary(
    name='GaInPAs',
    elements=('Ga', 'In', 'P', 'As'),
    ternaries=(GaInP, GaInAs, GaPAs, InPAs))


GaInPSb = IIIVZincBlendeQuaternary(
    name='GaInPSb',
    elements=('Ga', 'In', 'P', 'Sb'),
    ternaries=(GaInP, GaInSb, GaPSb, InPSb))


GaInAsSb = IIIVZincBlendeQuaternary(
    name='GaInAsSb',
    elements=('Ga', 'In', 'As', 'Sb'),
    ternaries=(GaInAs, GaInSb, GaAsSb, InAsSb))

iii_v_zinc_blende_quaternaries = [  # Type 1: AB_{x}C_{y}D_{1-x-y}
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

__all__ = ['iii_v_zinc_blende_quaternaries']
__all__ += [quaternary.name for quaternary in iii_v_zinc_blende_quaternaries]
