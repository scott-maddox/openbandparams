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
from openbandparams import base_material
from openbandparams.base_material import BaseType
from openbandparams.utils import classinstancemethod


class Base(base_material.Base):
    '''
    The Base class for all iii_v alloys.
    
    Any methods in here will be inherited by the Binary, Ternary, and
    Quaternary classes, and all of their subclasses. These functions
    are called from the alloy itself, rather than mixing the calls
    from the composing alloys.
    '''

    name = 'iii_v.Base'

    @classinstancemethod
    def Eg(self, cls, **kwargs):
        '''
        Returns the bandgap, Eg, in electron Volts at a given
        temperature, T, in Kelvin (default: 300 K).
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return min(obj.Eg_Gamma(**kwargs), obj.Eg_X(**kwargs),
                   obj.Eg_L(**kwargs))

    @classinstancemethod
    def meff_hh_100(self, cls, **kwargs):
        '''
        Returns the heavy hole band effective mass in the [100] direction,
        meff_hh_100, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 1. / (obj.Luttinger1(**kwargs) - 2 * obj.Luttinger2(**kwargs))

    @classinstancemethod
    def meff_hh_110(self, cls, **kwargs):
        '''
        Returns the heavy hole band effective mass in the [110] direction,
        meff_hh_110, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 2. / (2 * obj.Luttinger1(**kwargs) - obj.Luttinger2(**kwargs)
                - 3 * obj.Luttinger3(**kwargs))

    @classinstancemethod
    def meff_hh_111(self, cls, **kwargs):
        '''
        Returns the heavy hole band effective mass in the [111] direction,
        meff_hh_111, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 1. / (obj.Luttinger1(**kwargs) - 2 * obj.Luttinger3(**kwargs))

    @classinstancemethod
    def meff_lh_100(self, cls, **kwargs):
        '''
        Returns the light hole band effective mass in the [100] direction,
        meff_lh_100, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 1. / (obj.Luttinger1(**kwargs) + 2 * obj.Luttinger2(**kwargs))

    @classinstancemethod
    def meff_lh_110(self, cls, **kwargs):
        '''
        Returns the light hole band effective mass in the [110] direction,
        meff_lh_110, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 2. / (2 * obj.Luttinger1(**kwargs) + obj.Luttinger2(**kwargs)
                + 3 * obj.Luttinger3(**kwargs))

    @classinstancemethod
    def meff_lh_111(self, cls, **kwargs):
        '''
        Returns the light hole band effective mass in the [111] direction,
        meff_lh_111, in units of electron mass.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return 1. / (obj.Luttinger1(**kwargs) + 2 * obj.Luttinger3(**kwargs))

    @classinstancemethod
    def _get_eps_xx(self, cls, **kwargs):
        if 'a0' in kwargs:
            if self is not None:
                obj = self
            else:
                obj = cls
            return obj.biaxial_strained_eps_xx(**kwargs)
        elif 'eps_xx' in kwargs:
            return kwargs['eps_xx']
        else:
            raise ValueError('Missing required keyword argument'
                             ' `eps_xx` or `a0`')

    @classinstancemethod
    def biaxial_strained_eps_xx(self, cls, **kwargs):
        '''
        Returns the in-plane strain, `eps_xx`, induced by growing
        on a substrate with the given lattice constant, `a0`, assuming no
        lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if 'a0' in kwargs:
            if self is not None:
                obj = self
            else:
                obj = cls
            return 1 - obj.a(**kwargs) / kwargs['a0']
        else:
            raise ValueError('Missing required keyword argument `a0`')

    @classinstancemethod
    def biaxial_strained_a0(self, cls, **kwargs):
        '''
        Returns the substrate lattice constant, `a0`, required to induce the
        given in-plane strain, `eps_xx`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        eps_xx = obj._get_eps_xx(**kwargs)
        return obj.a(**kwargs) / (1 - eps_xx)

    @classinstancemethod
    def biaxial_strained_eps_zz(self, cls, **kwargs):
        '''
        Returns the out-of-plane strain induced by the given in-plane
        strain, `eps_xx`, or by growth on a substrate with the given lattice
        constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        eps_xx = obj._get_eps_xx(**kwargs)
        return -2 * obj.c_12(**kwargs) / obj.c_11(**kwargs) * eps_xx

    @classinstancemethod
    def biaxial_strained_dE_c(self, cls, **kwargs):
        '''
        Returns the conduction band-edge shift, in eV, induced by the
        given in-plane strain, `eps_xx`, or by growth on a substrate with
        the given lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        eps_xx = obj._get_eps_xx(**kwargs)
        return obj.a_c(**kwargs) * (2 * eps_xx +
                            obj.biaxial_strained_eps_zz(**kwargs))

    @classinstancemethod
    def biaxial_strained_P_eps(self, cls, **kwargs):
        '''
        Returns the hydrostatic component of the valance band-edge shift,
        in eV, induced by the given in-plane strain, `eps_xx`, or by growth
        on a substrate with the given lattice constant, `a0`, assuming no
        lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        eps_xx = obj._get_eps_xx(**kwargs)
        return obj.a_v(**kwargs) * (2 * eps_xx +
                            obj.biaxial_strained_eps_zz(**kwargs))

    @classinstancemethod
    def biaxial_strained_Q_eps(self, cls, **kwargs):
        '''
        Returns the uniaxial component of the valance band-edge shift,
        in eV, induced by the given in-plane strain, `eps_xx`, or by growth
        on a substrate with the given lattice constant, `a0`, assuming no
        lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        eps_xx = obj._get_eps_xx(**kwargs)
        return obj.b(**kwargs) * (obj.biaxial_strained_eps_zz(**kwargs)
                                  - eps_xx)

    @classinstancemethod
    def biaxial_strained_dE_hh(self, cls, **kwargs):
        '''
        Returns the heavy-hole band-edge shift, in eV, induced by the given
        in-plane strain, `eps_xx`, or by growth on a substrate with the given
        lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return -(obj.biaxial_strained_P_eps(**kwargs)
                 + obj.biaxial_strained_Q_eps(**kwargs))

    @classinstancemethod
    def biaxial_strained_dE_lh(self, cls, **kwargs):
        '''
        Returns the light-hole band-edge shift, in eV, induced by the given
        in-plane strain, `eps_xx`, or by growth on a substrate with the given
        lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (-obj.biaxial_strained_P_eps(**kwargs)
                + obj.biaxial_strained_Q_eps(**kwargs))

    @classinstancemethod
    def biaxial_strained_E_c(self, cls, **kwargs):
        '''
        Returns the conduction band-edge offset, in eV, at the given
        in-plane strain, `eps_xx`, or for growth on a substrate with the given
        lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (obj.VBO(**kwargs) + obj.Eg(**kwargs)
                + obj.biaxial_strained_dE_c(**kwargs))

    @classinstancemethod
    def biaxial_strained_E_hh(self, cls, **kwargs):
        '''
        Returns the heavy-hole band-edge offset, in eV, at the given
        in-plane strain, `eps_xx`, or for growth on a substrate with the given
        lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (obj.VBO(**kwargs)
                + obj.biaxial_strained_dE_hh(**kwargs))

    @classinstancemethod
    def biaxial_strained_E_lh(self, cls, **kwargs):
        '''
        Returns the light-hole band-edge offset, in eV, at the given
        in-plane strain, `eps_xx`, or for growth on a substrate with the given
        lattice constant, `a0`, assuming no lattice relaxation.

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (obj.VBO(**kwargs)
                + obj.biaxial_strained_dE_lh(**kwargs))

    @classinstancemethod
    def biaxial_strained_E_c_hh(self, cls, **kwargs):
        '''
        Returns the separation between the conduction band-edge and the
        heavy-hole band-edge, in eV, at the given in-plane strain, `eps_xx`,
        or for growth on a substrate with the given lattice constant, `a0`,
        assuming no lattice relaxation, and at temperature, `T`, in
        Kelvin (default: 300 K).

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (obj.Eg(**kwargs)
                + obj.biaxial_strained_dE_c(**kwargs)
                - obj.biaxial_strained_dE_hh(**kwargs))

    @classinstancemethod
    def biaxial_strained_E_c_lh(self, cls, **kwargs):
        '''
        Returns the separation between the conduction band-edge and the
        light-hole band-edge, in eV, at the given in-plane strain, `eps_xx`,
        or for growth on a substrate with the given lattice constant, `a0`,
        assuming no lattice relaxation, and at temperature, `T`, in
        Kelvin (default: 300 K).

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return (obj.Eg(**kwargs)
                + obj.biaxial_strained_dE_c(**kwargs)
                - obj.biaxial_strained_dE_lh(**kwargs))

    @classinstancemethod
    def biaxial_strained_Eg(self, cls, **kwargs):
        '''
        Returns the minimum separation between the conduction band-edge and the
        valance band-edge, in eV, at the given in-plane strain, `eps_xx`,
        or for growth on a substrate with the given lattice constant, `a0`,
        assuming no lattice relaxation, and at temperature, `T`, in
        Kelvin (default: 300 K).

        This assumes growth in the [100] direction.

        Note: `eps_xx` should be negative for compressive in-plane strain, and
        positive for tensile in-plane strain.
        '''
        if self is not None:
            obj = self
        else:
            obj = cls
        return min(obj.biaxial_strained_E_c_hh(**kwargs),
                   obj.biaxial_strained_E_c_lh(**kwargs))