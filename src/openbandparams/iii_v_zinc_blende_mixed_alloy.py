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

from .iii_v_zinc_blende_alloy import IIIVZincBlendeAlloy
from .parameter import method_parameter
from .references import vurgaftman_2001

class IIIVZincBlendeMixedAlloy(IIIVZincBlendeAlloy):
    '''
    The base class for all III-V zinc blende mixed alloys, i.e. ternaries,
    quaternaries, quinaries, etc.
    '''

    def __call__(self, **kwargs):
        '''
        Used to specify the alloy composition.
        '''
        raise NotImplementedError()
    
    def _interpolate(self, name, kwargs):
        raise NotImplementedError()
        
    @method_parameter(dependencies=['Delta_SO'],
                      units='eV')
    def Delta_SO(self, **kwargs):
        return self._interpolate('Delta_SO', kwargs)
        
    @method_parameter(dependencies=['Eg_Gamma'],
                      units='eV')
    def Eg_Gamma(self, **kwargs):
        return self._interpolate('Eg_Gamma', kwargs)
        
    @method_parameter(dependencies=['Eg_L'],
                      units='eV')
    def Eg_L(self, **kwargs):
        return self._interpolate('Eg_L', kwargs)
        
    @method_parameter(dependencies=['Eg_X'],
                      units='eV')
    def Eg_X(self, **kwargs):
        return self._interpolate('Eg_X', kwargs)
    
    @method_parameter(dependencies=['Ep'],
                      units='eV', references=[vurgaftman_2001])
    def Ep(self, **kwargs):
        '''
        Linear interpolation is recommended for alloys.
        '''
        return self._interpolate('Ep', kwargs)
    
    @method_parameter(dependencies=['F'],
                      units='dimensionless', references=[vurgaftman_2001])
    def F(self, **kwargs):
        '''
        Linear interpolation is recommended for alloys.
        '''
        return self._interpolate('F', kwargs)
    
    @method_parameter(dependencies=['VBO'],
                      units='eV')
    def VBO(self, **kwargs):
        return self._interpolate('VBO', kwargs)

    @method_parameter(dependencies=['a_300K'],
                      units='angstrom')
    def a_300K(self, **kwargs):
        '''
        Returns the lattice parameter, a, in Angstroms at 300 K.
        '''
        return self._interpolate('a_300K', kwargs)
    
    @method_parameter(dependencies=['a_c'],
                      units='eV')
    def a_c(self, **kwargs):
        return self._interpolate('a_c', kwargs)
    
    @method_parameter(dependencies=['a_v'],
                      units='eV')
    def a_v(self, **kwargs):
        return self._interpolate('a_v', kwargs)
    
    @method_parameter(dependencies=['b'],
                      units='eV')
    def b(self, **kwargs):
        return self._interpolate('b', kwargs)
    
    @method_parameter(dependencies=['c11'],
                      units='eV')
    def c11(self, **kwargs):
        return self._interpolate('c11', kwargs)
    
    @method_parameter(dependencies=['c12'],
                      units='eV')
    def c12(self, **kwargs):
        return self._interpolate('c12', kwargs)
    
    @method_parameter(dependencies=['c44'],
                      units='eV')
    def c44(self, **kwargs):
        return self._interpolate('c44', kwargs)
    
    @method_parameter(dependencies=['d'],
                      units='eV')
    def d(self, **kwargs):
        return self._interpolate('d', kwargs)
    
    @method_parameter(dependencies=['dielectric'],
                      units='dimensionless')
    def dielectric(self, **kwargs):
        return self._interpolate('dielectric', kwargs)
    
    @method_parameter(dependencies=['dielectric_high_frequency'],
                      units='dimensionless')
    def dielectric_high_frequency(self, **kwargs):
        return self._interpolate('dielectric_high_frequency', kwargs)
    
    @method_parameter(dependencies=['meff_hh_100', 'meff_lh_100'],
                      units='dimensionless')
    def luttinger1(self, **kwargs):
        return ((1. / self.meff_lh_100(**kwargs) +
                 1. / self.meff_hh_100(**kwargs)  ) / 2.)
    
    @method_parameter(dependencies=['meff_hh_100', 'meff_lh_100'],
                      units='dimensionless')
    def luttinger2(self, **kwargs):
        return ((1. / self.meff_lh_100(**kwargs) -
                 1. / self.meff_hh_100(**kwargs)  ) / 4.)
    
    @method_parameter(dependencies=['luttinger2', 'luttinger32'],
                      units='dimensionless')
    def luttinger3(self, **kwargs):
        return self.luttinger32(**kwargs) + self.luttinger2(**kwargs)
    
    @method_parameter(dependencies=['luttinger32'],
                      units='dimensionless')
    def luttinger32(self, **kwargs):
        '''
        Returns the difference between the third and second Luttinger
        parameters, i.e. `luttinger3 - luttinger2`.
        
        Linear interpolation of luttinger32 is the recommended way to
        estimate the valance band warping in alloys.
        '''
        return self._interpolate('luttinger32', kwargs)
    
    @method_parameter(dependencies=['meff_e_L_DOS'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_L_DOS(self, **kwargs):
        '''
        Linear interpolation of meff_e_L_DOS is recommended for alloys.
        '''
        return self._interpolate('meff_e_L_DOS', kwargs)
    
    @method_parameter(dependencies=['meff_e_L_long'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_L_long(self, **kwargs):
        '''
        Linear interpolation of meff_e_L_long is recommended for alloys.
        '''
        return self._interpolate('meff_e_L_long', kwargs)
    
    @method_parameter(dependencies=['meff_e_L_trans'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_L_trans(self, **kwargs):
        '''
        Linear interpolation of meff_e_L_trans is recommended for alloys.
        '''
        return self._interpolate('meff_e_L_trans', kwargs)
    
    @method_parameter(dependencies=['meff_e_X_DOS'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_X_DOS(self, **kwargs):
        '''
        Linear interpolation of meff_e_X_DOS is recommended for alloys.
        '''
        return self._interpolate('meff_e_X_DOS', kwargs)
    
    @method_parameter(dependencies=['meff_e_X_long'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_X_long(self, **kwargs):
        '''
        Linear interpolation of meff_e_X_long is recommended for alloys.
        '''
        return self._interpolate('meff_e_X_long', kwargs)
    
    @method_parameter(dependencies=['meff_e_X_trans'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_e_X_trans(self, **kwargs):
        '''
        Linear interpolation of meff_e_X_trans is recommended for alloys.
        '''
        return self._interpolate('meff_e_X_trans', kwargs)
    
    @method_parameter(dependencies=['meff_hh_100'], units='m_e')
    def meff_hh_100(self, **kwargs):
        '''
        Returns the light-hole band effective mass in the [100] direction,
        meff_hh_100, in units of electron mass.

        Linear interpolation of meff_hh_100 is recommended for alloys.
        '''
        return self._interpolate('meff_hh_100', kwargs)
    
    @method_parameter(dependencies=['meff_lh_100'], units='m_e')
    def meff_lh_100(self, **kwargs):
        '''
        Returns the heavy-hole band effective mass in the [100] direction,
        meff_hh_100, in units of electron mass.

        Linear interpolation of meff_lh_100 is recommended for alloys.
        '''
        return self._interpolate('meff_lh_100', kwargs)
    
    @method_parameter(dependencies=['meff_SO'],
                      units='m_e', references=[vurgaftman_2001])
    def meff_SO(self, **kwargs):
        '''
        Linear interpolation of meff_SO is recommended for alloys.
        '''
        return self._interpolate('meff_SO', kwargs)

    @method_parameter(dependencies=['thermal_expansion'],
                      units='angstrom/K')
    def thermal_expansion(self, **kwargs):
        '''
        Returns the thermal expansion coefficient.
        '''
        return self._interpolate('thermal_expansion', kwargs)