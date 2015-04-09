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

from .iii_v_zinc_blende_ternary import IIIVZincBlendeTernary
from .iii_v_zinc_blende_binaries import (AlN, GaN, InN, AlP, GaP,
    InP, AlAs, GaAs, InAs, AlSb, GaSb, InSb)
from .parameter import ValueParameter, FunctionParameter, MethodParameter
from .references import lin_2002, vurgaftman_2001, klipstein_2014


AlGaN = IIIVZincBlendeTernary(
    name='AlGaN',
    elements=('Al', 'Ga', 'N'),
    binaries=(AlN, GaN),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 0.76, 'eV', references=[lin_2002]),
        ValueParameter('Eg_X_bowing', 0.3, 'eV', references=[lin_2002]),
    ])

AlInN = IIIVZincBlendeTernary(
    name='AlInN',
    elements=('Al', 'In', 'N'),
    binaries=(AlN, InN),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 2.73, 'eV', references=[lin_2002]),
        ValueParameter('Eg_X_bowing', 3.62, 'eV', references=[lin_2002]),
    ])

GaInN = IIIVZincBlendeTernary(
    name='GaInN',
    elements=('Ga', 'In', 'N'),
    binaries=(GaN, InN),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 1.38, 'eV', references=[lin_2002]),
        ValueParameter('Eg_X_bowing', 1.67, 'eV', references=[lin_2002]),
    ])

AlGaP = IIIVZincBlendeTernary(
    name='AlGaP',
    elements=('Al', 'Ga', 'P'),
    binaries=(AlP, GaP),
    parameters=[
        ValueParameter('Eg_X_bowing', 0.13, 'eV', references=[vurgaftman_2001]),
    ])

AlInP = IIIVZincBlendeTernary(
    name='AlInP',
    elements=('Al', 'In', 'P'),
    binaries=(AlP, InP),
    parameters=[
        ValueParameter('Delta_SO_bowing', -0.48, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.38, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', -0.19, 'eV', references=[vurgaftman_2001]),
        #TODO: estimate F_bowing to get meff_e_Gamma_bowing = 0.22
    ])

GaInP = IIIVZincBlendeTernary(
    name='GaInP',
    elements=('Ga', 'In', 'P'),
    binaries=(GaP, InP),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 0.65, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 1.03, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('F_bowing', 0.78, 'dimensionless', references=[vurgaftman_2001]),
        #TODO: estimate F_bowing to get meff_e_Gamma_bowing = 0.051
    ])

AlGaAs = IIIVZincBlendeTernary(
    name='AlGaAs',
    elements=('Al', 'Ga', 'As'),
    binaries=(AlAs, GaAs),
    parameters=[
        ValueParameter('Eg_X_bowing', 0.055, 'eV', references=[vurgaftman_2001]),
    ])
def AlGaAs_Eg_Gamma_bowing(**kwargs):
    x = kwargs['x']
    return -0.127 + 1.310 * x
AlGaAs.add_parameter(FunctionParameter('Eg_Gamma_bowing',
                                       AlGaAs_Eg_Gamma_bowing, units='eV',
                                       references=[vurgaftman_2001]))

AlInAs = IIIVZincBlendeTernary(
    name='AlInAs',
    elements=('Al', 'In', 'As'),
    binaries=(AlAs, InAs),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.15, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep_bowing', -4.81, 'eV', references=[vurgaftman_2001]),
        ValueParameter('F_bowing', -4.44, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('VBO_bowing', -0.64, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_c_bowing', -1.4, 'eV', references=[vurgaftman_2001]),
        #TODO: estimate F_bowing to get meff_e_Gamma_bowing = 0.049
    ])

GaInAs = IIIVZincBlendeTernary(
    name='GaInAs',
    elements=('Ga', 'In', 'As'),
    binaries=(GaAs, InAs),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.15, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.477, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.33, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 1.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep_bowing', -1.48, 'eV', references=[vurgaftman_2001]),
        ValueParameter('F_bowing', 1.77, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('VBO_bowing', -0.38, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_c_bowing', 2.61, 'eV', references=[vurgaftman_2001]),
        ValueParameter('meff_hh_100_bowing', -0.145, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_lh_100_bowing', 0.0202, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('luttinger32_bowing', 0.481, 'm_e', references=[vurgaftman_2001]),
        #TODO: estimate F_bowing to get meff_e_Gamma_bowing = 0.0091
    ])

AlGaSb = IIIVZincBlendeTernary(
    name='AlGaSb',
    elements=('Al', 'Ga', 'Sb'),
    binaries=(AlSb, GaSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.3, 'eV', references=[vurgaftman_2001]),
    ])
def AlGaSb_Eg_Gamma_bowing(**kwargs):
    x = kwargs['x']
    return -0.044 + 1.22 * x
AlGaSb.add_parameter(FunctionParameter('Eg_Gamma_bowing',
                                       AlGaSb_Eg_Gamma_bowing, units='eV',
                                       references=[vurgaftman_2001]))

AlInSb = IIIVZincBlendeTernary(
    name='AlInSb',
    elements=('Al', 'In', 'Sb'),
    binaries=(AlSb, InSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.25, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.43, 'eV', references=[vurgaftman_2001]),
    ])

GaInSb = IIIVZincBlendeTernary(
    name='GaInSb',
    elements=('Ga', 'In', 'Sb'),
    binaries=(GaSb, InSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.1, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.415, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.33, 'eV', references=[vurgaftman_2001]),
        ValueParameter('F_bowing', -6.84, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_lh_100_bowing', 0.011, 'm_e', references=[vurgaftman_2001]),
        #TODO: estimate F_bowing to get meff_e_Gamma_bowing = 0.0092
    ])

AlNP = IIIVZincBlendeTernary(
    name='AlNP',
    elements=('Al', 'N', 'P'),
    binaries=(AlN, AlP),
    parameters=[
    ])

GaNP = IIIVZincBlendeTernary(
    name='GaNP',
    elements=('Ga', 'N', 'P'),
    binaries=(GaN, GaP),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 3.9, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 10., 'eV', references=[vurgaftman_2001]),
    ])

InNP = IIIVZincBlendeTernary(
    name='InNP',
    elements=('In', 'N', 'P'),
    binaries=(InN, InP),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 15, 'eV', references=[vurgaftman_2001]),
    ])

AlNAs = IIIVZincBlendeTernary(
    name='AlNAs',
    elements=('Al', 'N', 'As'),
    binaries=(AlN, AlAs),
    parameters=[])

GaNAs = IIIVZincBlendeTernary(
    name='GaNAs',
    elements=('Ga', 'N', 'As'),
    binaries=(GaN, GaAs),
    parameters=[])
def GaNAs_Eg_Gamma(self, **kwargs):
    linear = self._interpolate('Eg_Gamma', kwargs)
    x = self._x
    return linear + 20.4 * x**2 - 100. * x**3
GaNAs.add_parameter(MethodParameter('Eg_Gamma',
                                    GaNAs_Eg_Gamma, 
                                    dependencies=['Eg_Gamma'],
                                    units='eV',
                                    references=[vurgaftman_2001]),
                    overload=True)

InNAs = IIIVZincBlendeTernary(
    name='InNAs',
    elements=('In', 'N', 'As'),
    binaries=(InN, InAs),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 4.22, 'eV', references=[vurgaftman_2001]),
    ])

AlPAs = IIIVZincBlendeTernary(
    name='AlPAs',
    elements=('Al', 'P', 'As'),
    binaries=(AlP, AlAs),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 0.22, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.22, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.22, 'eV', references=[vurgaftman_2001]),
    ])

GaPAs = IIIVZincBlendeTernary(
    name='GaPAs',
    elements=('Ga', 'P', 'As'),
    binaries=(GaP, GaAs),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 0.19, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.16, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.24, 'eV', references=[vurgaftman_2001]),
    ])

InPAs = IIIVZincBlendeTernary(
    name='InPAs',
    elements=('In', 'P', 'As'),
    binaries=(InP, InAs),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.16, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.10, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.27, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.27, 'eV', references=[vurgaftman_2001]),
    ])

AlPSb = IIIVZincBlendeTernary(
    name='AlPSb',
    elements=('Al', 'P', 'Sb'),
    binaries=(AlP, AlSb),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
    ])

GaPSb = IIIVZincBlendeTernary(
    name='GaPSb',
    elements=('Ga', 'P', 'Sb'),
    binaries=(GaP, GaSb),
    parameters=[
        ValueParameter('Eg_Gamma_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 2.7, 'eV', references=[vurgaftman_2001]),
    ])

InPSb = IIIVZincBlendeTernary(
    name='InPSb',
    elements=('In', 'P', 'Sb'),
    binaries=(InP, InSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.75, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 1.9, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 1.9, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 1.9, 'eV', references=[vurgaftman_2001]),
    ])

AlAsSb = IIIVZincBlendeTernary(
    name='AlAsSb',
    elements=('Al', 'As', 'Sb'),
    binaries=(AlAs, AlSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.15, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.28, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.28, 'eV', references=[vurgaftman_2001]),
#         ValueParameter('VBO_bowing', -1.71, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO_bowing', -0.14, 'eV', references=[vurgaftman_2001]),
    ])

GaAsSb = IIIVZincBlendeTernary(
    name='GaAsSb',
    elements=('Ga', 'As', 'Sb'),
    binaries=(GaAs, GaSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 0.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 1.43, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 1.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 1.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO_bowing', -1.06, 'eV', references=[vurgaftman_2001]),
    ])

InAsSb = IIIVZincBlendeTernary(
    name='InAsSb',
    elements=('In', 'As', 'Sb'),
    binaries=(InAs, InSb),
    parameters=[
        ValueParameter('Delta_SO_bowing', 1.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_bowing', 0.67, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_bowing', 0.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_bowing', 0.6, 'eV', references=[vurgaftman_2001]),
        # ~60% of bowing in valance band [klipstein_2014]
        ValueParameter('VBO_bowing', -0.402, 'eV', references=[klipstein_2014]),
    ])


iii_v_zinc_blende_ternaries = [AlGaN, AlInN, GaInN,
                               AlGaP, AlInP, GaInP,
                               AlGaAs, AlInAs, GaInAs,
                               AlGaSb, AlInSb, GaInSb,
                               AlNP, GaNP, InNP,
                               AlNAs, GaNAs, InNAs,
                               AlPAs, GaPAs, InPAs,
                               AlPSb, GaPSb, InPSb,
                               AlAsSb, GaAsSb, InAsSb]

__all__ = ['iii_v_zinc_blende_ternaries']
__all__ += [ternary.name for ternary in iii_v_zinc_blende_ternaries]
