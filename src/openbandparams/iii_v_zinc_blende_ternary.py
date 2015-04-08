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
from .algorithms import bisect
from .parameter import method_parameter
from .references import vurgaftman_2001

class IIIVZincBlendeTernary(IIIVZincBlendeAlloy):
    '''
    The base class for all III-V zinc blende ternary alloys.
    '''
    def __init__(self, name, elements, binaries, parameters=None, x=None):
        if binaries[0].elements[1] == binaries[1].elements[1]:
            self._type = 1
            self._element_x = binaries[0].elements[0]
            self._element_1mx = binaries[1].elements[0]
            self._element_y = binaries[0].elements[1]
            calc_elements = (binaries[0].elements[0],
                        binaries[1].elements[0],
                        binaries[0].elements[1])
        elif binaries[0].elements[0] == binaries[1].elements[0]:
            self._type = 2
            self._element_x = binaries[0].elements[1]
            self._element_1mx = binaries[1].elements[1]
            self._element_y = binaries[0].elements[0]
            calc_elements = (binaries[0].elements[0],
                        binaries[0].elements[1],
                        binaries[1].elements[1])
        else:
            raise ValueError()
#         name = ''.join(elements)
        assert elements == calc_elements
        super(IIIVZincBlendeTernary, self).__init__(name, elements,
                                                    parameters=parameters)
        self.binaries = binaries
        if x is not None:
            self._x = float(x)
        else:
            self._x = None
    
    def _instance(self, x=None):
        return IIIVZincBlendeTernary(self.name, self.elements,
            self.binaries, parameters=self._parameters.values(), x=x)

    def __call__(self, **kwargs):
        '''
        Used to specify the alloy composition.
        '''
        if 'x' in kwargs:
            x = float(kwargs['x'])
        elif self._element_x in kwargs:
            x = float(kwargs[self._element_x])
        elif self._element_1mx in kwargs:
            x = 1. - float(kwargs[self._element_1mx])
        elif 'a' in kwargs:
            # lattice match to the given lattice constant
            a = kwargs['a']
            T = kwargs.get('T', 300.)
            # make sure the lattice constant is available
            b1a = self.binaries[0].a(T=T)
            b2a = self.binaries[1].a(T=T)
            amin = min(b1a, b2a)
            amax = max(b1a, b2a)
            if a < amin or a > amax:
                raise ValueError('a out of range [%.3f, %.3f]' % (amin, amax))
            # find the correct composition, x
            x = bisect(func=lambda x: self(x=x).a(T=T) - a, a=0, b=1)
        else:
            raise TypeError(
                "Missing required key word argument.\n" + self._get_usage())
        if not (0. <= x <= 1.):
            raise ValueError('The alloy fraction must be between 0 and 1')
        return self._instance(x=x)

    def _get_usage(self):
        return ("The  supported kwarg combinations are as follows:"
                "\n    - 'x' or '{A}' or '{B}'"
                "\n    - 'a' [and 'T']"
                "".format(A=self._element_x, B=self._element_1mx))

    def __repr__(self):
        if self._x is None:
            return '{}'.format(self.name)
        if self._type == 1:
            return '{}({}={})'.format(self.name, self.elements[0], self._x)
        elif self._type == 2:
            return '{}({}={})'.format(self.name, self.elements[1], self._x)
        else:
            raise RuntimeError()
    
    def latex(self):
        if self._type == 1:
            if self._x is None:
                return "{A}_{{x}}{B}_{{1-x}}{C}".format(A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
            else:
                return "{A}_{{{:g}}}{B}_{{{:g}}}{C}".format(self._x,
                                                            1. - self._x,
                                                            A=self.elements[0],
                                                            B=self.elements[1],
                                                            C=self.elements[2])
        elif self._type == 2:
            if self._x is None:
                return "{A}{B}_{{x}}{C}_{{1-x}}".format(A=self.elements[0],
                                                        B=self.elements[1],
                                                        C=self.elements[2])
            else:
                return "{A}{B}_{{{:g}}}{C}_{{{:g}}}".format(self._x,
                                                            1. - self._x,
                                                            A=self.elements[0],
                                                            B=self.elements[1],
                                                            C=self.elements[2])
        else:
            raise RuntimeError()

    def element_fraction(self, element):
        if self._x is None:
            raise RuntimeError('Alloy composition has not been specified.')
        if self._type == 1:
            if element == self.elements[0]:
                return self._x
            elif element == self.elements[1]:
                return (1 - self._x)
            elif element == self.elements[2]:
                return 1
            else:
                return 0
        elif self._type == 2:
            if element == self.elements[0]:
                return 1
            elif element == self.elements[1]:
                return self._x
            elif element == self.elements[2]:
                return (1 - self._x)
            else:
                return 0
        else:
            raise RuntimeError()
    
    def _get_bowing(self, name, kwargs):
        p = self.get_parameter(name+'_bowing', default=None)
        if p is None:
            return None
        return p(x=self._x, **kwargs)
    
    def _interpolate(self, name, kwargs):
        if self._x is None:
            raise RuntimeError('Alloy composition has not been specified.')
        x = self._x
        pA = self.binaries[0].get_parameter(name)
        if pA is None:
            raise AttributeError('"{}" is missing a required parameter: "{}".'
                                 ''.format(self.binaries[0].name,
                                           name))
        pB = self.binaries[1].get_parameter(name)
        if pB is None:
            raise AttributeError('"{}" is missing a required parameter: "{}".'
                                 ''.format(self.binaries[1].name,
                                           name))
        A = pA(**kwargs)
        B = pB(**kwargs)
        C = self._get_bowing(name, kwargs)
        if C is not None:
            # a bowing parameter exists - use it
            return A * x + B * (1 - x) - C * x * (1 - x)
        else:
            # otherwise, use linear interpolation
            return A * x + B * (1 - x)
        
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
    
    @method_parameter(dependencies=['meff_hh_100', 'meff_lh_100'],
                      units='dimensionless')
    def luttinger1(self, **kwargs):
        return (1. / self.meff_lh_100(**kwargs) + 1. / self.meff_hh_100(**kwargs)) / 2.
    
    @method_parameter(dependencies=['meff_hh_100', 'meff_lh_100'],
                      units='dimensionless')
    def luttinger2(self, **kwargs):
        return (1. / self.meff_lh_100(**kwargs) - 1. / self.meff_hh_100(**kwargs)) / 4.
    
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