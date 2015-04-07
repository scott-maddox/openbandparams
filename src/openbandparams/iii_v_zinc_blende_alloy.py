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
from .iii_v_alloy import IIIVAlloy
from .parameter import method_parameter
from .references import vurgaftman_2001, kane_1956
from .equations import varshni
from math import sqrt


class IIIVZincBlendeAlloy(IIIVAlloy):
    '''
    The base class for all III-V zinc blende alloys.
    '''

    @method_parameter(dependencies=['a_300K', 'thermal_expansion'],
                      units='angstrom')
    def a(self, **kwargs):
        '''
        Returns the lattice parameter, a, in Angstroms at a given
        temperature, `T`, in Kelvin (default: 300 K).
        '''
        T = kwargs.get('T', 300.)
        return (self.a_300K(**kwargs) +
                self.thermal_expansion(**kwargs) * (T - 300.))
        
    @method_parameter(dependencies=['Eg_Gamma_0', 'alpha_Gamma', 'beta_Gamma'],
                      units='eV')
    def Eg_Gamma(self, **kwargs):
        Eg_0 = self.Eg_Gamma_0(**kwargs)
        alpha = self.alpha_Gamma(**kwargs)
        beta = self.beta_Gamma(**kwargs)
        T = kwargs.get('T', 300.)
        return varshni(Eg_0, alpha, beta, T)
        
    @method_parameter(dependencies=['Eg_L_0', 'alpha_L', 'beta_L'],
                      units='eV')
    def Eg_L(self, **kwargs):
        Eg_0 = self.Eg_L_0(**kwargs)
        alpha = self.alpha_L(**kwargs)
        beta = self.beta_L(**kwargs)
        T = kwargs.get('T', 300.)
        return varshni(Eg_0, alpha, beta, T)
        
    @method_parameter(dependencies=['Eg_X_0', 'alpha_X', 'beta_X'],
                      units='eV')
    def Eg_X(self, **kwargs):
        Eg_0 = self.Eg_X_0(**kwargs)
        alpha = self.alpha_X(**kwargs)
        beta = self.beta_X(**kwargs)
        T = kwargs.get('T', 300.)
        return varshni(Eg_0, alpha, beta, T)
        
    @method_parameter(dependencies=['Eg_Gamma', 'Eg_L', 'Eg_X'], units='eV',
                      aliases=['bandgap'])
    def Eg(self, **kwargs):
        '''
        Returns the bandgap, Eg, in eV at a given
        temperature, T, in K (default=300.).
        '''
        return min(self.Eg_Gamma(**kwargs),
                   self.Eg_L(**kwargs),
                   self.Eg_X(**kwargs))
    
    @method_parameter(dependencies=['Eg', 'VBO'], units='eV')
    def electron_affinity(self, **kwargs):
        return 4.66-self.Eg(**kwargs)-self.VBO(**kwargs)
    
    @method_parameter(dependencies=['Eg_Gamma', 'meff_e_Gamma'],
                      units='dimensionless', references=[kane_1956])
    def nonparabolicity(self, **kwargs):
        '''
        Returns the Kane band nonparabolicity parameter for the Gamma-valley.
        '''
        Eg = self.Eg_Gamma(**kwargs)
        meff = self.meff_e_Gamma(**kwargs)
        return 1/Eg * (1 - meff)**2
    
    @method_parameter(dependencies=['Eg_Gamma_0', 'Delta_SO', 'Ep',
                                    'meff_e_Gamma_0'],
                      units='dimensionless', references=[vurgaftman_2001])
    def F(self, **kwargs):
        '''
        Returns the Kane remote-band parameter, `F`, calculated from
        `Eg_Gamma_0`, `Delta_SO`, `Ep`, and `meff_e_Gamma_0`.
        '''
        Eg = self.Eg_Gamma_0(**kwargs)
        Delta_SO = self.Delta_SO(**kwargs)
        Ep = self.Ep(**kwargs)
        meff = self.meff_e_Gamma_0(**kwargs)
        return (1./meff-1-(Ep*(Eg+2.*Delta_SO/3.))/(Eg*(Eg+Delta_SO)))/2
    
    @method_parameter(dependencies=['Eg_Gamma', 'Delta_SO', 'Ep', 'F'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_Gamma(self, **kwargs):
        '''
        Returns the electron effective mass in the Gamma-valley
        calculated from Eg_Gamma(T), Delta_SO, Ep and F.
        
        Interpolation of Eg_Gamma(T), Delta_SO, Ep and F, and
        then calculation of meff_e_Gamma is recommended for alloys.
        '''
        Eg = self.Eg_Gamma(**kwargs)
        Delta_SO = self.Delta_SO(**kwargs)
        Ep = self.Ep(**kwargs)
        F = self.F(**kwargs)
        return 1./((1.+2.*F)+(Ep*(Eg+2.*Delta_SO/3.))/(Eg*(Eg+Delta_SO)))
    
    @method_parameter(dependencies=['luttinger1', 'Eg_Gamma', 'Delta_SO', 'Ep'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_SO(self, **kwargs):
        '''
        Returns the electron effective mass in the Gamma-valley
        calculated from Eg_Gamma(T), Delta_SO, Ep and F.
        
        Interpolation of Eg_Gamma(T), Delta_SO, Ep and F, and
        then calculation of meff_e_Gamma is recommended for alloys.
        '''
        Eg = self.Eg_Gamma(**kwargs)
        Delta_SO = self.Delta_SO(**kwargs)
        Ep = self.Ep(**kwargs)
        luttinger1 = self.luttinger1(**kwargs)
        return 1./(luttinger1 - (Ep*Delta_SO)/(3*Eg*(Eg+Delta_SO)))
    
    @method_parameter(dependencies=['luttinger2', 'luttinger3'],
                      units='dimensionless')
    def luttinger32(self, **kwargs):
        '''
        Returns the difference between the third and second Luttinger
        parameters, i.e. `luttinger3 - luttinger2`.
        
        Linear interpolation of luttinger32 is the recommended way to
        estimate the valance band warping in alloys.
        '''
        return 1. / (self.luttinger1(**kwargs) - 2 * self.luttinger2(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger2'], units='m_e')
    def meff_hh_100(self, **kwargs):
        '''
        Returns the heavy-hole band effective mass in the [100] direction,
        meff_hh_100, in units of electron mass.
        '''
        return 1. / (self.luttinger1(**kwargs) - 2 * self.luttinger2(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger2', 'luttinger3'],
                      units='m_e')
    def meff_hh_110(self, **kwargs):
        '''
        Returns the heavy-hole band effective mass in the [110] direction,
        meff_hh_110, in units of electron mass.
        '''
        return 2. / (2 * self.luttinger1(**kwargs) - self.luttinger2(**kwargs)
                - 3 * self.luttinger3(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger3'], units='m_e')
    def meff_hh_111(self, **kwargs):
        '''
        Returns the heavy-hole band effective mass in the [111] direction,
        meff_hh_111, in units of electron mass.
        '''
        return 1. / (self.luttinger1(**kwargs) - 2 * self.luttinger3(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger2'], units='m_e')
    def meff_lh_100(self, **kwargs):
        '''
        Returns the light-hole band effective mass in the [100] direction,
        meff_lh_100, in units of electron mass.
        '''
        return 1. / (self.luttinger1(**kwargs) + 2 * self.luttinger2(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger2', 'luttinger3'],
                      units='m_e')
    def meff_lh_110(self, **kwargs):
        '''
        Returns the light-hole band effective mass in the [110] direction,
        meff_lh_110, in units of electron mass.
        '''
        return 2. / (2 * self.luttinger1(**kwargs) + self.luttinger2(**kwargs)
                + 3 * self.luttinger3(**kwargs))
    
    @method_parameter(dependencies=['luttinger1', 'luttinger3'], units='m_e')
    def meff_lh_111(self, **kwargs):
        '''
        Returns the light-hole band effective mass in the [111] direction,
        meff_lh_111, in units of electron mass.
        '''
        return 1. / (self.luttinger1(**kwargs) + 2 * self.luttinger3(**kwargs))

#     def _get_eps_xx(self, **kwargs):
#         if 'a0' in kwargs:
#             if self is not None:
#                 self = self
#             else:
#                 self = cls
#             return self.biaxial_strained_eps_xx(**kwargs)
#         elif 'eps_xx' in kwargs:
#             return kwargs['eps_xx']
#         else:
#             raise ValueError('Missing required keyword argument'
#                              ' `eps_xx` or `a0`')
#
#     def biaxial_strained_eps_xx(self, **kwargs):
#         '''
#         Returns the in-plane strain, `eps_xx`, induced by growing
#         on a substrate with the given lattice constant, `a0`, assuming no
#         lattice relaxation.
# 
#         This assumes growth in the [100] direction.
# 
#         Note: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         if 'a0' in kwargs:
#             return 1 - self.a(**kwargs) / kwargs['a0']
#         else:
#             raise ValueError('Missing required keyword argument `a0`')
# 
#     def biaxial_strained_a0(self, **kwargs):
#         '''
#         Returns the substrate lattice constant, `a0`, required to induce the
#         given in-plane strain, `eps_xx`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         eps_xx = self._get_eps_xx(**kwargs)
#         return self.a(**kwargs) / (1 - eps_xx)
# 
#     def biaxial_strained_eps_zz(self, **kwargs):
#         '''
#         Returns the out-of-plane strain induced by the given in-plane
#         strain, `eps_xx`, or by growth on a substrate with the given lattice
#         constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         eps_xx = self._get_eps_xx(**kwargs)
#         return -2 * self.c_12(**kwargs) / self.c_11(**kwargs) * eps_xx
# 
#     def biaxial_strained_dE_c(self, **kwargs):
#         '''
#         Returns the conduction band-edge shift, in eV, induced by the
#         given in-plane strain, `eps_xx`, or by growth on a substrate with
#         the given lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         eps_xx = self._get_eps_xx(**kwargs)
#         return self.a_c(**kwargs) * (2 * eps_xx +
#                             self.biaxial_strained_eps_zz(**kwargs))
# 
#     def biaxial_strained_P_eps(self, **kwargs):
#         '''
#         Returns the hydrostatic component of the valance band-edge shift,
#         in eV, induced by the given in-plane strain, `eps_xx`, or by growth
#         on a substrate with the given lattice constant, `a0`, assuming no
#         lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         eps_xx = self._get_eps_xx(**kwargs)
#         return self.a_v(**kwargs) * (2 * eps_xx +
#                             self.biaxial_strained_eps_zz(**kwargs))
# 
#     def biaxial_strained_Q_eps(self, **kwargs):
#         '''
#         Returns the uniaxial component of the valance band-edge shift,
#         in eV, induced by the given in-plane strain, `eps_xx`, or by growth
#         on a substrate with the given lattice constant, `a0`, assuming no
#         lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         eps_xx = self._get_eps_xx(**kwargs)
#         return self.b(**kwargs) * (self.biaxial_strained_eps_zz(**kwargs)
#                                   - eps_xx)
# 
#     def biaxial_strained_dE_hh(self, **kwargs):
#         '''
#         Returns the heavy-hole band-edge shift, in eV, induced by the given
#         in-plane strain, `eps_xx`, or by growth on a substrate with the given
#         lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return -(self.biaxial_strained_P_eps(**kwargs)
#                  + self.biaxial_strained_Q_eps(**kwargs))
# 
#     def biaxial_strained_dE_lh(self, **kwargs):
#         '''
#         Returns the light-hole band-edge shift, in eV, induced by the given
#         in-plane strain, `eps_xx`, or by growth on a substrate with the given
#         lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (-self.biaxial_strained_P_eps(**kwargs)
#                 + self.biaxial_strained_Q_eps(**kwargs))
# 
#     def biaxial_strained_E_c(self, **kwargs):
#         '''
#         Returns the conduction band-edge offset, in eV, at the given
#         in-plane strain, `eps_xx`, or for growth on a substrate with the given
#         lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (self.VBO(**kwargs) + self.Eg(**kwargs)
#                 + self.biaxial_strained_dE_c(**kwargs))
# 
#     def biaxial_strained_E_hh(self, **kwargs):
#         '''
#         Returns the heavy-hole band-edge offset, in eV, at the given
#         in-plane strain, `eps_xx`, or for growth on a substrate with the given
#         lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (self.VBO(**kwargs)
#                 + self.biaxial_strained_dE_hh(**kwargs))
# 
#     def biaxial_strained_E_lh(self, **kwargs):
#         '''
#         Returns the light-hole band-edge offset, in eV, at the given
#         in-plane strain, `eps_xx`, or for growth on a substrate with the given
#         lattice constant, `a0`, assuming no lattice relaxation.
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (self.VBO(**kwargs)
#                 + self.biaxial_strained_dE_lh(**kwargs))
# 
#     def biaxial_strained_E_c_hh(self, **kwargs):
#         '''
#         Returns the separation between the conduction band-edge and the
#         heavy-hole band-edge, in eV, at the given in-plane strain, `eps_xx`,
#         or for growth on a substrate with the given lattice constant, `a0`,
#         assuming no lattice relaxation, and at temperature, `T`, in
#         Kelvin (default: 300 K).
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (self.Eg(**kwargs)
#                 + self.biaxial_strained_dE_c(**kwargs)
#                 - self.biaxial_strained_dE_hh(**kwargs))
# 
#     def biaxial_strained_E_c_lh(self, **kwargs):
#         '''
#         Returns the separation between the conduction band-edge and the
#         light-hole band-edge, in eV, at the given in-plane strain, `eps_xx`,
#         or for growth on a substrate with the given lattice constant, `a0`,
#         assuming no lattice relaxation, and at temperature, `T`, in
#         Kelvin (default: 300 K).
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return (self.Eg(**kwargs)
#                 + self.biaxial_strained_dE_c(**kwargs)
#                 - self.biaxial_strained_dE_lh(**kwargs))
# 
#     def biaxial_strained_Eg(self, **kwargs):
#         '''
#         Returns the minimum separation between the conduction band-edge and the
#         valance band-edge, in eV, at the given in-plane strain, `eps_xx`,
#         or for growth on a substrate with the given lattice constant, `a0`,
#         assuming no lattice relaxation, and at temperature, `T`, in
#         Kelvin (default: 300 K).
# 
#         This assumes growth in the [100] direction.
#         
#         Note 1: Specifying `eps_xx` results in less overhead than
#         specifying `a0`.
# 
#         Note 2: `eps_xx` should be negative for compressive in-plane strain, and
#         positive for tensile in-plane strain.
#         '''
#         return min(self.biaxial_strained_E_c_hh(**kwargs),
#                    self.biaxial_strained_E_c_lh(**kwargs))