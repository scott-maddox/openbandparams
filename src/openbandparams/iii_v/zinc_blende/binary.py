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

from math import tanh
from openbandparams.iii_v.binary import Binary


# Each Binary is a class instead of an instance because GaP has a different
# Eg_Gamma temperature dependence. I could have only had GaP be a subclass,
# but for consistency i just made them all subclasses.

class AlN(Binary):
    name = 'AlN'
    elements = ('Al', 'N')
    _a_300K = 4.38  # Ang    vurgaftman_band_2001
    _da_dT = 0  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 4.9  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 600  # K    vurgaftman_band_2001
    _Eg_X_0 = 6  # eV    vurgaftman_band_2001
    _alpha_X = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_X = 600  # K    vurgaftman_band_2001
    _Eg_L_0 = 9.3  # eV    vurgaftman_band_2001
    _alpha_L = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_L = 600  # K    vurgaftman_band_2001
    _Delta_SO = 0.019  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.25  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 0.53  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.31  # m_e    vurgaftman_band_2001
    _Luttinger1 = 1.92  # vurgaftman_band_2001
    _Luttinger2 = 0.47  # vurgaftman_band_2001
    _Luttinger3 = 0.85  # vurgaftman_band_2001
    _meff_SO = 0.47  # m_e    vurgaftman_band_2001
    _Ep = 27.1  # eV    vurgaftman_band_2001
    _F = 0.76  # vurgaftman_band_2001
    _VBO = -3.44  # eV    vurgaftman_band_2001
    _a_c = -6  # eV    vurgaftman_band_2001
    _a_v = -3.4  # eV    vurgaftman_band_2001
    _b = -1.9  # eV    vurgaftman_band_2001
    _d = -10  # eV    vurgaftman_band_2001
    _c_11 = 304  # GPa    vurgaftman_band_2001
    _c_12 = 160  # GPa    vurgaftman_band_2001
    _c_44 = 193  # GPa    vurgaftman_band_2001


class GaN(Binary):
    name = 'GaN'
    elements = ('Ga', 'N')
    _a_300K = 4.5  # Ang    vurgaftman_band_2001
    _da_dT = 0  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 3.299  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 600  # K    vurgaftman_band_2001
    _Eg_X_0 = 4.52  # eV    vurgaftman_band_2001
    _alpha_X = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_X = 600  # K    vurgaftman_band_2001
    _Eg_L_0 = 5.59  # eV    vurgaftman_band_2001
    _alpha_L = 0.000593  # eV/K    vurgaftman_band_2001
    _beta_L = 600  # K    vurgaftman_band_2001
    _Delta_SO = 0.017  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.15  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 0.5  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.3  # m_e    vurgaftman_band_2001
    _Luttinger1 = 2.67  # vurgaftman_band_2001
    _Luttinger2 = 0.75  # vurgaftman_band_2001
    _Luttinger3 = 1.1  # vurgaftman_band_2001
    _meff_SO = 0.29  # m_e    vurgaftman_band_2001
    _Ep = 25  # eV    vurgaftman_band_2001
    _F = -0.92  # vurgaftman_band_2001
    _VBO = -2.64  # eV    vurgaftman_band_2001
    _a_c = -2.2  # eV    vurgaftman_band_2001
    _a_v = -5.2  # eV    vurgaftman_band_2001
    _b = -2.2  # eV    vurgaftman_band_2001
    _d = -3.4  # eV    vurgaftman_band_2001
    _c_11 = 293  # GPa    vurgaftman_band_2001
    _c_12 = 159  # GPa    vurgaftman_band_2001
    _c_44 = 155  # GPa    vurgaftman_band_2001


class InN(Binary):
    name = 'InN'
    elements = ('In', 'N')
    _a_300K = 4.98  # Ang    vurgaftman_band_2001
    _da_dT = 0  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 1.94  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000245  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 624  # K    vurgaftman_band_2001
    _Eg_X_0 = 2.51  # eV    vurgaftman_band_2001
    _alpha_X = 0.000245  # eV/K    vurgaftman_band_2001
    _beta_X = 624  # K    vurgaftman_band_2001
    _Eg_L_0 = 5.82  # eV    vurgaftman_band_2001
    _alpha_L = 0.000245  # eV/K    vurgaftman_band_2001
    _beta_L = 624  # K    vurgaftman_band_2001
    _Delta_SO = 0.006  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.12  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 0.48  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.27  # m_e    vurgaftman_band_2001
    _Luttinger1 = 3.72  # vurgaftman_band_2001
    _Luttinger2 = 1.26  # vurgaftman_band_2001
    _Luttinger3 = 1.63  # vurgaftman_band_2001
    _meff_SO = 0.3  # m_e    vurgaftman_band_2001
    _Ep = 25  # eV    vurgaftman_band_2001
    _F = -0.92  # vurgaftman_band_2001
    _VBO = -2.38  # eV    vurgaftman_band_2001
    _a_c = -1.85  # eV    vurgaftman_band_2001
    _a_v = -1.5  # eV    vurgaftman_band_2001
    _b = -1.2  # eV    vurgaftman_band_2001
    _d = -9.3  # eV    vurgaftman_band_2001
    _c_11 = 187  # GPa    vurgaftman_band_2001
    _c_12 = 125  # GPa    vurgaftman_band_2001
    _c_44 = 86  # GPa    vurgaftman_band_2001


class AlP(Binary):
    name = 'AlP'
    elements = ('Al', 'P')
    _a_300K = 5.4672  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000292  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 3.63  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.0005771  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 372  # K    vurgaftman_band_2001
    _Eg_X_0 = 2.52  # eV    vurgaftman_band_2001
    _alpha_X = 0.000318  # eV/K    vurgaftman_band_2001
    _beta_X = 588  # K    vurgaftman_band_2001
    _Eg_L_0 = 3.57  # eV    vurgaftman_band_2001
    _alpha_L = 0.000318  # eV/K    vurgaftman_band_2001
    _beta_L = 588  # K    vurgaftman_band_2001
    _Delta_SO = 0.07  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.22  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 2.68  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.155  # m_e    vurgaftman_band_2001
    _Luttinger1 = 3.35  # vurgaftman_band_2001
    _Luttinger2 = 0.71  # vurgaftman_band_2001
    _Luttinger3 = 1.23  # vurgaftman_band_2001
    _meff_SO = 0.3  # m_e    vurgaftman_band_2001
    _Ep = 17.7  # eV    vurgaftman_band_2001
    _F = -0.65  # vurgaftman_band_2001
    _VBO = -1.74  # eV    vurgaftman_band_2001
    _a_c = -5.7  # eV    vurgaftman_band_2001
    _a_v = -3  # eV    vurgaftman_band_2001
    _b = -1.5  # eV    vurgaftman_band_2001
    _d = -4.6  # eV    vurgaftman_band_2001
    _c_11 = 1330  # GPa    vurgaftman_band_2001
    _c_12 = 630  # GPa    vurgaftman_band_2001
    _c_44 = 615  # GPa    vurgaftman_band_2001


class GaP(Binary):
    name = 'GaP'
    elements = ('Ga', 'P')
    _a_300K = 5.4505  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000292  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 2.886  # eV    vurgaftman_band_2001
    _Eg_X_0 = 2.35  # eV    vurgaftman_band_2001
    _alpha_X = 0.0005771  # eV/K    vurgaftman_band_2001
    _beta_X = 372  # K    vurgaftman_band_2001
    _Eg_L_0 = 2.72  # eV    vurgaftman_band_2001
    _alpha_L = 0.0005771  # eV/K    vurgaftman_band_2001
    _beta_L = 372  # K    vurgaftman_band_2001
    _Delta_SO = 0.08  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.13  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 1.2  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.15  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 2  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.253  # m_e    vurgaftman_band_2001
    _Luttinger1 = 4.05  # vurgaftman_band_2001
    _Luttinger2 = 0.49  # vurgaftman_band_2001
    _Luttinger3 = 2.93  # vurgaftman_band_2001
    _meff_SO = 0.25  # m_e    vurgaftman_band_2001
    _Ep = 31.4  # eV    vurgaftman_band_2001
    _F = -2.04  # vurgaftman_band_2001
    _VBO = -1.27  # eV    vurgaftman_band_2001
    _a_c = -8.2  # eV    vurgaftman_band_2001
    _a_v = -1.7  # eV    vurgaftman_band_2001
    _b = -1.6  # eV    vurgaftman_band_2001
    _d = -4.6  # eV    vurgaftman_band_2001
    _c_11 = 1405  # GPa    vurgaftman_band_2001
    _c_12 = 620.3  # GPa    vurgaftman_band_2001
    _c_44 = 703.3  # GPa    vurgaftman_band_2001

    @classmethod
    def Eg_Gamma(cls, **kwargs):
        '''
        Returns the Gamma-valley bandgap, Eg_Gamma, in electron Volts at a
        given temperature, T, in Kelvin (default: 300 K).

        GaP has a unique Gamma-gap temperature dependence.
        '''
        T = cls._get_T(kwargs)
        # vurgaftman_band_2001
        return cls._Eg_Gamma_0 + 0.1081 * (1 - 1. / tanh(164. / T))  # eV


class InP(Binary):
    name = 'InP'
    elements = ('In', 'P')
    _a_300K = 5.8697  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000279  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 1.4236  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000363  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 162  # K    vurgaftman_band_2001
    _Eg_X_0 = 2.384  # eV    vurgaftman_band_2001
    _alpha_X = 0.00037  # eV/K    vurgaftman_band_2001
    _beta_X = 0  # K    vurgaftman_band_2001
    _Eg_L_0 = 2.014  # eV    vurgaftman_band_2001
    _alpha_L = 0.000363  # eV/K    vurgaftman_band_2001
    _beta_L = 162  # K    vurgaftman_band_2001
    _Delta_SO = 0.108  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.0795  # m_e    vurgaftman_band_2001
    _meff_e_L_DOS = 0.47  # m_e    vurgaftman_band_2001
    _meff_e_X_DOS = 0.88  # m_e    vurgaftman_band_2001
    _Luttinger1 = 5.08  # vurgaftman_band_2001
    _Luttinger2 = 1.6  # vurgaftman_band_2001
    _Luttinger3 = 2.1  # vurgaftman_band_2001
    _meff_SO = 0.21  # m_e    vurgaftman_band_2001
    _Ep = 20.7  # eV    vurgaftman_band_2001
    _F = -1.31  # vurgaftman_band_2001
    _VBO = -0.94  # eV    vurgaftman_band_2001
    _a_c = -6  # eV    vurgaftman_band_2001
    _a_v = -0.6  # eV    vurgaftman_band_2001
    _b = -2  # eV    vurgaftman_band_2001
    _d = -5  # eV    vurgaftman_band_2001
    _c_11 = 1011  # GPa    vurgaftman_band_2001
    _c_12 = 561  # GPa    vurgaftman_band_2001
    _c_44 = 456  # GPa    vurgaftman_band_2001


class AlAs(Binary):
    name = 'AlAs'
    elements = ('Al', 'As')
    _a_300K = 5.6611  # Ang    vurgaftman_band_2001
    _da_dT = 0.000029  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 3.099  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000885  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 530  # K    vurgaftman_band_2001
    _Eg_X_0 = 2.24  # eV    vurgaftman_band_2001
    _alpha_X = 0.0007  # eV/K    vurgaftman_band_2001
    _beta_X = 530  # K    vurgaftman_band_2001
    _Eg_L_0 = 2.46  # eV    vurgaftman_band_2001
    _alpha_L = 0.000605  # eV/K    vurgaftman_band_2001
    _beta_L = 204  # K    vurgaftman_band_2001
    _Delta_SO = 0.28  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.15  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 1.32  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.15  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 0.97  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.22  # m_e    vurgaftman_band_2001
    _Luttinger1 = 3.76  # vurgaftman_band_2001
    _Luttinger2 = 0.82  # vurgaftman_band_2001
    _Luttinger3 = 1.42  # vurgaftman_band_2001
    _meff_SO = 0.28  # m_e    vurgaftman_band_2001
    _Ep = 21.1  # eV    vurgaftman_band_2001
    _F = -0.48  # vurgaftman_band_2001
    _VBO = -1.33  # eV    vurgaftman_band_2001
    _a_c = -5.64  # eV    vurgaftman_band_2001
    _a_v = -2.47  # eV    vurgaftman_band_2001
    _b = -2.3  # eV    vurgaftman_band_2001
    _d = -3.4  # eV    vurgaftman_band_2001
    _c_11 = 1250  # GPa    vurgaftman_band_2001
    _c_12 = 534  # GPa    vurgaftman_band_2001
    _c_44 = 542  # GPa    vurgaftman_band_2001


class GaAs(Binary):
    name = 'GaAs'
    elements = ('Ga', 'As')
    _a_300K = 5.65325  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000388  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 1.519  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.0005405  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 204  # K    vurgaftman_band_2001
    _Eg_X_0 = 1.981  # eV    vurgaftman_band_2001
    _alpha_X = 0.00046  # eV/K    vurgaftman_band_2001
    _beta_X = 204  # K    vurgaftman_band_2001
    _Eg_L_0 = 1.815  # eV    vurgaftman_band_2001
    _alpha_L = 0.000605  # eV/K    vurgaftman_band_2001
    _beta_L = 204  # K    vurgaftman_band_2001
    _Delta_SO = 0.341  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.067  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 1.9  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.0754  # m_e    vurgaftman_band_2001
    _meff_e_L_DOS = 0.56  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 1.3  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.23  # m_e    vurgaftman_band_2001
    _meff_e_X_DOS = 0.85  # m_e    vurgaftman_band_2001
    _Luttinger1 = 6.98  # vurgaftman_band_2001
    _Luttinger2 = 2.06  # vurgaftman_band_2001
    _Luttinger3 = 2.93  # vurgaftman_band_2001
    _meff_SO = 0.172  # m_e    vurgaftman_band_2001
    _Ep = 28.8  # eV    vurgaftman_band_2001
    _F = -1.94  # vurgaftman_band_2001
    _VBO = -0.8  # eV    vurgaftman_band_2001
    _a_c = -7.17  # eV    vurgaftman_band_2001
    _a_v = -1.16  # eV    vurgaftman_band_2001
    _b = -2  # eV    vurgaftman_band_2001
    _d = -4.8  # eV    vurgaftman_band_2001
    _c_11 = 1221  # GPa    vurgaftman_band_2001
    _c_12 = 566  # GPa    vurgaftman_band_2001
    _c_44 = 600  # GPa    vurgaftman_band_2001


class InAs(Binary):
    name = 'InAs'
    elements = ('In', 'As')
    _a_300K = 6.0583  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000274  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 0.417  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000276  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 93  # K    vurgaftman_band_2001
    _Eg_X_0 = 1.9  # eV    williams_experimental_1986
    _alpha_X = 0.000276  # eV/K    vurgaftman_band_2001
    _beta_X = 93  # K    vurgaftman_band_2001
    _Eg_L_0 = 1.53  # eV    kim_towards_2010
    _alpha_L = 0.000276  # eV/K    vurgaftman_band_2001
    _beta_L = 93  # K    vurgaftman_band_2001
    _Delta_SO = 0.39  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.026  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 0.64  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.05  # m_e    vurgaftman_band_2001
    _meff_e_L_DOS = 0.29  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 1.13  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.16  # m_e    vurgaftman_band_2001
    _meff_e_X_DOS = 0.64  # m_e    vurgaftman_band_2001
    _Luttinger1 = 20  # vurgaftman_band_2001
    _Luttinger2 = 8.5  # vurgaftman_band_2001
    _Luttinger3 = 9.2  # vurgaftman_band_2001
    _meff_SO = 0.14  # m_e    vurgaftman_band_2001
    _Ep = 21.5  # eV    vurgaftman_band_2001
    _F = -2.9  # vurgaftman_band_2001
    _VBO = -0.59  # eV    vurgaftman_band_2001
    _a_c = -5.08  # eV    vurgaftman_band_2001
    _a_v = -1  # eV    vurgaftman_band_2001
    _b = -1.8  # eV    vurgaftman_band_2001
    _d = -3.6  # eV    vurgaftman_band_2001
    _c_11 = 832.9  # GPa    vurgaftman_band_2001
    _c_12 = 452.6  # GPa    vurgaftman_band_2001
    _c_44 = 395.9  # GPa    vurgaftman_band_2001


class AlSb(Binary):
    name = 'AlSb'
    elements = ('Al', 'Sb')
    _a_300K = 6.1355  # Ang    vurgaftman_band_2001
    _da_dT = 0.000026  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 2.386  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.00042  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 140  # K    vurgaftman_band_2001
    _Eg_X_0 = 1.696  # eV    vurgaftman_band_2001
    _alpha_X = 0.00039  # eV/K    vurgaftman_band_2001
    _beta_X = 140  # K    vurgaftman_band_2001
    _Eg_L_0 = 2.329  # eV    vurgaftman_band_2001
    _alpha_L = 0.00058  # eV/K    vurgaftman_band_2001
    _beta_L = 140  # K    vurgaftman_band_2001
    _Delta_SO = 0.676  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.14  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 1.64  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.23  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 1.357  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.123  # m_e    vurgaftman_band_2001
    _Luttinger1 = 5.18  # vurgaftman_band_2001
    _Luttinger2 = 1.19  # vurgaftman_band_2001
    _Luttinger3 = 1.97  # vurgaftman_band_2001
    _meff_SO = 0.22  # m_e    vurgaftman_band_2001
    _Ep = 18.7  # eV    vurgaftman_band_2001
    _F = -0.56  # vurgaftman_band_2001
    _VBO = -0.41  # eV    vurgaftman_band_2001
    _a_c = -4.5  # eV    vurgaftman_band_2001
    _a_v = -1.4  # eV    vurgaftman_band_2001
    _b = -1.35  # eV    vurgaftman_band_2001
    _d = -4.3  # eV    vurgaftman_band_2001
    _c_11 = 876.9  # GPa    vurgaftman_band_2001
    _c_12 = 434.1  # GPa    vurgaftman_band_2001
    _c_44 = 407.6  # GPa    vurgaftman_band_2001


class GaSb(Binary):
    name = 'GaSb'
    elements = ('Ga', 'Sb')
    _a_300K = 6.0959  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000472  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 0.812  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.000417  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 140  # K    vurgaftman_band_2001
    _Eg_X_0 = 1.141  # eV    vurgaftman_band_2001
    _alpha_X = 0.000475  # eV/K    vurgaftman_band_2001
    _beta_X = 94  # K    vurgaftman_band_2001
    _Eg_L_0 = 0.875  # eV    vurgaftman_band_2001
    _alpha_L = 0.000597  # eV/K    vurgaftman_band_2001
    _beta_L = 140  # K    vurgaftman_band_2001
    _Delta_SO = 0.76  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.039  # m_e    vurgaftman_band_2001
    _meff_e_L_long = 1.3  # m_e    vurgaftman_band_2001
    _meff_e_L_trans = 0.1  # m_e    vurgaftman_band_2001
    _meff_e_X_long = 1.51  # m_e    vurgaftman_band_2001
    _meff_e_X_trans = 0.22  # m_e    vurgaftman_band_2001
    _Luttinger1 = 13.4  # vurgaftman_band_2001
    _Luttinger2 = 4.7  # vurgaftman_band_2001
    _Luttinger3 = 6  # vurgaftman_band_2001
    _meff_SO = 0.12  # m_e    vurgaftman_band_2001
    _Ep = 27  # eV    vurgaftman_band_2001
    _F = -1.63  # vurgaftman_band_2001
    _VBO = -0.03  # eV    vurgaftman_band_2001
    _a_c = -7.5  # eV    vurgaftman_band_2001
    _a_v = -0.8  # eV    vurgaftman_band_2001
    _b = -2  # eV    vurgaftman_band_2001
    _d = -4.7  # eV    vurgaftman_band_2001
    _c_11 = 884.2  # GPa    vurgaftman_band_2001
    _c_12 = 402.6  # GPa    vurgaftman_band_2001
    _c_44 = 432.2  # GPa    vurgaftman_band_2001


class InSb(Binary):
    name = 'InSb'
    elements = ('In', 'Sb')
    _a_300K = 6.4794  # Ang    vurgaftman_band_2001
    _da_dT = 0.0000348  # Ang/K    vurgaftman_band_2001
    _Eg_Gamma_0 = 0.235  # eV    vurgaftman_band_2001
    _alpha_Gamma = 0.00032  # eV/K    vurgaftman_band_2001
    _beta_Gamma = 170  # K    vurgaftman_band_2001
    _Eg_X_0 = 1.8  # eV    williams_experimental_1986
    _alpha_X = 0.00032  # eV/K    vurgaftman_band_2001
    _beta_X = 170  # K    vurgaftman_band_2001
    _Eg_L_0 = 0.93  # eV    vurgaftman_band_2001
    _alpha_L = 0.00032  # eV/K    vurgaftman_band_2001
    _beta_L = 170  # K    vurgaftman_band_2001
    _Delta_SO = 0.81  # eV    vurgaftman_band_2001
    _meff_e_Gamma = 0.0135  # m_e    vurgaftman_band_2001
    _meff_e_L_DOS = 0.25  # m_e    vurgaftman_band_2001
    _Luttinger1 = 34.8  # vurgaftman_band_2001
    _Luttinger2 = 15.5  # vurgaftman_band_2001
    _Luttinger3 = 16.5  # vurgaftman_band_2001
    _meff_SO = 0.11  # m_e    vurgaftman_band_2001
    _Ep = 23.3  # eV    vurgaftman_band_2001
    _F = -0.23  # vurgaftman_band_2001
    _VBO = 0  # eV    vurgaftman_band_2001
    _a_c = -6.94  # eV    vurgaftman_band_2001
    _a_v = -0.36  # eV    vurgaftman_band_2001
    _b = -2  # eV    vurgaftman_band_2001
    _d = -4.7  # eV    vurgaftman_band_2001
    _c_11 = 684.7  # GPa    vurgaftman_band_2001
    _c_12 = 373.5  # GPa    vurgaftman_band_2001
    _c_44 = 311.1  # GPa    vurgaftman_band_2001

binaries = [AlN, GaN, InN,
            AlP, GaP, InP,
            AlAs, GaAs, InAs,
            AlSb, GaSb, InSb]

__all__ = ['binaries']
__all__ += [binary.name for binary in binaries]
