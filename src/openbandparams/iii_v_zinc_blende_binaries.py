#
#   Copyright (c) 2013-2015, Scott J Maddox
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

from math import tanh
from .references import vurgaftman_2001, adachi_1987, adachi_1982
from .parameter import ValueParameter, MethodParameter
from .iii_v_zinc_blende_binary import IIIVZincBlendeBinary


AlN = IIIVZincBlendeBinary(
    name='AlN',
    elements=('Al', 'N'),
    parameters=[
        ValueParameter('Delta_SO', 0.019, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 4.9, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 9.3, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 6., 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 27.1, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -3.44, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 4.38, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -6., 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -3.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.9, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 304., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 160., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 193., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -10., 'eV', references=[vurgaftman_2001]),
        ValueParameter('luttinger1', 1.92, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 0.47, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 0.85, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.25, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 0.53, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.31, 'm_e', references=[vurgaftman_2001]),
    ])

GaN = IIIVZincBlendeBinary(
    name='GaN',
    elements=('Ga', 'N'),
    parameters=[
        ValueParameter('Delta_SO', 0.017, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 3.299, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 5.59, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 4.52, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 25, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -2.64, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 4.5, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -2.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -5.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 5.93e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -2.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 600., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 293., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 159., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 155., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -3.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('luttinger1', 2.67, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 0.75, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 1.1, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.15, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 0.5, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.3, 'm_e', references=[vurgaftman_2001]),
    ])

InN = IIIVZincBlendeBinary(
    name='InN',
    elements=('In', 'N'),
    parameters=[
        ValueParameter('Delta_SO', 0.006, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 1.94, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 5.82, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 2.51, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 25., 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -2.38, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 4.98, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -1.85, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -1.5, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 2.45e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 2.45e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 2.45e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 624., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 624., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 624., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 187., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 125., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 86., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -9.3, 'eV', references=[vurgaftman_2001]),
        ValueParameter('luttinger1', 3.72, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 1.26, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 1.63, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.12, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 0.48, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.27, 'm_e', references=[vurgaftman_2001]),
    ])

AlP = IIIVZincBlendeBinary(
    name='AlP',
    elements=('Al', 'P'),
    parameters=[
        ValueParameter('Delta_SO', 0.07, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 3.63, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 3.57, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 2.52, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 17.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -1.74, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 5.4672, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -5.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -3., 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 5.771e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 3.18e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 3.18e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.5, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 372., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 588., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 588., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 1330., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 630., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 615., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('luttinger1', 3.35, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 0.71, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 1.23, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.22, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 2.68, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.155, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.92e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

GaP = IIIVZincBlendeBinary(
    name='GaP',
    elements=('Ga', 'P'),
    parameters=[
        ValueParameter('Delta_SO', 0.08, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 2.886, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 2.72, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 2.35, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 31.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -1.27, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 5.4505, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -8.2, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -1.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 5.771e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 5.771e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 372., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 372., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 1405., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 620.3, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 703.3, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 11.0, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 8.5, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 4.05, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 0.49, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 2.93, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.13, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 1.2, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.15, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 2., 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.253, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.92e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])
def GaP_Eg_Gamma(self, **kwargs):
    '''
    Returns the Gamma-valley bandgap, Eg_Gamma, in electron Volts at a
    given temperature, T, in Kelvin (default: 300 K).

    GaP has a unique Gamma-gap temperature dependence.
    '''
    T = kwargs.get('T', 300.)
    if T < 1e-4:
        return self.Eg_Gamma_0()
    return self.Eg_Gamma_0() + 0.1081 * (1 - 1. / tanh(164. / T))  # eV
GaP.add_parameter(MethodParameter('Eg_Gamma', GaP_Eg_Gamma,
                                  dependencies=['Eg_Gamma_0'],
                                  units='eV',
                                  references=[vurgaftman_2001]),
                  overload=True)


InP = IIIVZincBlendeBinary(
    name='InP',
    elements=('In', 'P'),
    parameters=[
        ValueParameter('Delta_SO', 0.108, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 1.4236, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 2.014, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 2.384, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 20.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -0.94, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 5.8697, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -6., 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -0.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 3.63e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 3.63e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 3.7e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -2., 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 162., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 162., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 0., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 1011., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 561., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 456., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -5., 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 12.3, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 9.6, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 5.08, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 1.6, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 2.1, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.0795, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_DOS', 0.47, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_DOS', 0.88, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.79e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

AlAs = IIIVZincBlendeBinary(
    name='AlAs',
    elements=('Al', 'As'),
    parameters=[
        ValueParameter('Delta_SO', 0.28, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 3.099, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 2.46, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 2.24, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 21.1, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -1.33, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 5.6611, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -5.64, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -2.47, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 8.85e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 6.05e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 7e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -2.3, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 530., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 204., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 530., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 1250., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 534., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 542., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -3.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 10.0, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 8.2, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 3.76, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 0.82, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 1.42, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.15, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 1.32, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.15, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 0.97, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.22, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.9e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

GaAs = IIIVZincBlendeBinary(
    name='GaAs',
    elements=('Ga', 'As'),
    parameters=[
        ValueParameter('Delta_SO', 0.341, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 1.519, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 1.815, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 1.981, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 28.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -0.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 5.65325, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -7.17, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -1.16, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 5.405e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 6.05e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 4.6e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -2., 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 204., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 204., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 204., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 1221., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 566., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 600., 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 13.0, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 11.15, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 6.98, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 2.06, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 2.93, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.067, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_DOS', 0.56, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 1.9, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.0754, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_DOS', 0.85, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 1.3, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.23, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 3.88e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

InAs = IIIVZincBlendeBinary(
    name='InAs',
    elements=('In', 'As'),
    parameters=[
        ValueParameter('Delta_SO', 0.39, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 0.417, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 1.133, 'eV', references=[vurgaftman_2001]),
#         ValueParameter('Eg_L_0', 1.53, 'eV', references=[kim_2010]),
        ValueParameter('Eg_X_0', 1.433, 'eV', references=[vurgaftman_2001]),
#         ValueParameter('Eg_X_0', 1.9, 'eV', references=[drube_1987]),
        ValueParameter('Ep', 21.5, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -0.59, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 6.0583, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -5.08, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -1., 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 2.76e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 2.76e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 2.76e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 93., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 93., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 93., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 832.9, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 452.6, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 395.9, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -3.6, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 14.5, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 12.3, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 20., 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 8.5, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 9.2, 'dimensionless', references=[vurgaftman_2001]),
#         ValueParameter('meff_SO_0', 0.14, 'm_e', references=[vurgaftman_2001]), # not consistent
        ValueParameter('meff_e_Gamma_0', 0.026, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_DOS', 0.29, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 0.64, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.05, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_DOS', 0.64, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 1.13, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.16, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.74e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

AlSb = IIIVZincBlendeBinary(
    name='AlSb',
    elements=('Al', 'Sb'),
    parameters=[
        ValueParameter('Delta_SO', 0.676, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 2.386, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 2.329, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 1.696, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 18.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -0.41, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 6.1355, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -4.5, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -1.4, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 4.2e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 3.9e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 5.8e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -1.35, 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 140., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 140., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 140., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 876.9, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 434.1, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 407.6, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.3, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 11.5, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 9.95, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 5.18, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 1.19, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 1.97, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.14, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 1.64, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.23, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 1.357, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.123, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 2.6e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

GaSb = IIIVZincBlendeBinary(
    name='GaSb',
    elements=('Ga', 'Sb'),
    parameters=[
        ValueParameter('Delta_SO', 0.76, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 0.812, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 0.875, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_X_0', 1.141, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Ep', 27., 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', -0.03, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 6.0959, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -7.5, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -0.8, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 4.17e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 5.97e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_X', 4.75e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('b', -2., 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 140., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 140., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_X', 94., 'K', references=[vurgaftman_2001]),
        ValueParameter('c11', 884.2, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 402.6, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 432.2, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 15.7, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 14.5, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 13.4, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 4.7, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 6., 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.039, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_long', 1.3, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_trans', 0.1, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_long', 1.51, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_trans', 0.22, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('thermal_expansion', 4.72e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

InSb = IIIVZincBlendeBinary(
    name='InSb',
    elements=('In', 'Sb'),
    parameters=[
        ValueParameter('Delta_SO', 0.81, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_Gamma_0', 0.235, 'eV', references=[vurgaftman_2001]),
        ValueParameter('Eg_L_0', 0.991, 'eV', references=[adachi_1987]), # adjusted to 0K
        ValueParameter('Eg_X_0', 1.691, 'eV', references=[adachi_1987]), # adjusted to 0K
        ValueParameter('Ep', 23.3, 'eV', references=[vurgaftman_2001]),
        ValueParameter('VBO', 0., 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_300K', 6.4794, 'angstrom', references=[vurgaftman_2001]),
        ValueParameter('a_c', -6.94, 'eV', references=[vurgaftman_2001]),
        ValueParameter('a_v', -0.36, 'eV', references=[vurgaftman_2001]),
        ValueParameter('alpha_Gamma', 3.2e-4, 'eV/K', references=[vurgaftman_2001]),
        ValueParameter('alpha_L', 3.2e-4, 'eV/K', references=[vurgaftman_2001]), # assumed same as Gamma
        ValueParameter('alpha_X', 3.2e-4, 'eV/K', references=[vurgaftman_2001]), # assumed same as Gamma
        ValueParameter('b', -2., 'eV', references=[vurgaftman_2001]),
        ValueParameter('beta_Gamma', 170., 'K', references=[vurgaftman_2001]),
        ValueParameter('beta_L', 170., 'K', references=[vurgaftman_2001]), # assumed same as Gamma
        ValueParameter('beta_X', 170., 'K', references=[vurgaftman_2001]), # assumed same as Gamma
        ValueParameter('c11', 684.7, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c12', 373.5, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('c44', 311.1, 'GPa', references=[vurgaftman_2001]),
        ValueParameter('d', -4.7, 'eV', references=[vurgaftman_2001]),
        ValueParameter('dielectric', 17.8, 'dimensionless', references=[adachi_1982]),
        ValueParameter('dielectric_high_frequency', 15.8, 'dimensionless', references=[adachi_1982]),
        ValueParameter('luttinger1', 34.8, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger2', 15.5, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('luttinger3', 16.5, 'dimensionless', references=[vurgaftman_2001]),
        ValueParameter('meff_e_Gamma_0', 0.0135, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_L_DOS', 0.25, 'm_e', references=[vurgaftman_2001]),
        ValueParameter('meff_e_X_DOS', 0.5, 'm_e'), # guess
        ValueParameter('thermal_expansion', 3.48e-5, 'angstrom/K', references=[vurgaftman_2001]),
    ])

iii_v_zinc_blende_binaries = [AlN, GaN, InN,
                              AlP, GaP, InP,
                              AlAs, GaAs, InAs,
                              AlSb, GaSb, InSb]

__all__ = ['iii_v_zinc_blende_binaries']
__all__ += [binary.name for binary in iii_v_zinc_blende_binaries]
