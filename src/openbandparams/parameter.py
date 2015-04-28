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

__all__ = ['Parameter', 'ValueParameter',
           'FunctionParameter', 'method_parameter']


class Parameter(object):
    def __init__(self, name, units, aliases=[], references=[]):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        units : string
            units
        aliases : list of strings (default=[])
            list of alternate names
        references : list of Reference objects (default=[])
            literature references
        '''
        self.name = name
        self.description = descriptions.get(name, '')
        self.units = units
        self.aliases = aliases
        self._references = references
    
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()

    def get_references(self):
        return self._references


class ValueParameter(Parameter):
    def __init__(self, name, value, units,
                 aliases=[], references=[]):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        value : object
            value of the parameter
        units : string
            units
        aliases : list of strings (default=[])
            list of alternate names
        references : list of Reference objects (default=[])
            literature references
        '''
        super(ValueParameter, self).__init__(name=name,
                                             units=units,
                                             aliases=aliases,
                                             references=references)
        self.value = value
    
    def __call__(self, *args, **kwargs):
        return self.value


class FunctionParameter(Parameter):
    def __init__(self, name, function, units,
                 aliases=[], references=[]):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        function : callable function
            function that returns the value of the parameter
        units : string
            units
        aliases : list of strings (default=[])
            list of alternate names
        references : list of Reference objects (default=[])
            literature references
        '''
        super(FunctionParameter, self).__init__(name=name,
                                                units=units,
                                                aliases=aliases,
                                                references=references)
        self.function = function
    
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


class MethodParameter(Parameter):
    def __init__(self, name, method, dependencies, units,
                 aliases=[], references=[]):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        method : callable method (default=None)
            method that accepts the alloy object as the first parameter, and
            returns the value of the parameter
        dependencies : list of strings (default=None)
            list of parameter names that this parameter depends on
        units : string
            units
        aliases : list of strings (default=[])
            list of alternate names
        references : list of Reference objects (default=[])
            literature references
        '''
        super(MethodParameter, self).__init__(name=name,
                                              units=units,
                                              aliases=aliases,
                                              references=references)
        self.alloy = None
        self.method = method
        self.dependencies = dependencies
    
    def bind(self, alloy):
        '''
        Shallow copies this MethodParameter, and binds it to an alloy.
        This is required before calling.
        '''
        param = MethodParameter(self.name, self.method, self.dependencies,
                                self.units, self.aliases, self._references)
        param.alloy = alloy
        return param
    
    def __call__(self, *args, **kwargs):
        if self.alloy is None:
            raise TypeError('MethodParameter must be bound to an Alloy'
                            ' with `bind` before calling.')
        return self.method(self.alloy, *args, **kwargs)
    
    def get_references(self):
        if self.alloy is None:
            return self._references
        else:
            params = [self]
            refs = []
            refs.extend(self._references)
            for d in self.dependencies:
                p = self.alloy.get_parameter(d, default=None)
                if p is not None and p not in params:
                    params.append(p)
                    for ref in p.get_references():
                        if ref not in refs:
                            refs.append(ref)
            if hasattr(self.alloy, 'binaries'):
                for alloy in getattr(self.alloy, 'binaries'):
                    for d in self.dependencies:
                        p = alloy.get_parameter(d, default=None)
                        if p is not None and p not in params:
                            params.append(p)
                            for ref in p.get_references():
                                if ref not in refs:
                                    refs.append(ref)
            if hasattr(self.alloy, 'ternaries'):
                for alloy in getattr(self.alloy, 'ternaries'):
                    for d in self.dependencies:
                        p = alloy.get_parameter(d, default=None)
                        params.append(p)
                        if p is not None and p not in params:
                            for ref in p.get_references():
                                if ref not in refs:
                                    refs.append(ref)
            return refs


def method_parameter(dependencies, units,
                     aliases=[], references=[]):
    def decorator(method):
        '''
        Instead of returning a function like most decorators, this returns
        a MethodParameter, which AlloyType moves to the `class_parameters`
        dictionary. At instantiation, the `class_parameters` are added
        to the `parameters` dictionary, unless a `Parameter` with the same
        name has already been added.
        '''
        name = method.func_name
        return MethodParameter(name, method, dependencies, units,
                               aliases, references)
    return decorator

descriptions = {
    'CBO' : 'conduction band offset energy relative to InSb VBO',
    'CBO_Gamma' : 'Gamma-valley conduction band offset energy relative to InSb VBO',
    'CBO_L' : 'L-valley conduction band offset energy relative to InSb VBO',
    'CBO_X' : 'X-valley conduction band offset energy relative to InSb VBO',
    'Delta_SO' : 'split-off energy',
    'Eg' : 'bandgap energy',
    'Eg_Gamma' : 'Gamma-valley bandgap energy',
    'Eg_Gamma_0' : 'Gamma-valley bandgap energy at 0 K',
    'Eg_L' : 'L-valley bandgap energy',
    'Eg_L_0' : 'L-valley bandgap energy at 0 K',
    'Eg_X' : 'X-valley bandgap energy',
    'Eg_X_0' : 'X-valley bandgap energy at 0 K',
    'Ep' : 'Ep interband matrix element',
    'F' : 'F Kane remote-band parameter',
    'VBO' : 'valance band offset energy relative to InSb VBO',
    'a' : 'lattice parameter',
    'a_300K' : 'lattice parameter at 300 K',
    'a_c' : 'conduction band deformation potential',
    'a_v' : 'valance band deformation potential',
    'alpha_Gamma' : 'Gamma-valley Varshni alpha parameter',
    'alpha_L' : 'L-valley Varshni alpha parameter',
    'alpha_X' : 'X-valley Varshni alpha parameter',
    'b' : 'b shear deformation potential',
    'beta_Gamma' : 'Gamma-valley Varshni beta parameter',
    'beta_L' : 'L-valley Varshni beta parameter',
    'beta_X' : 'X-valley Varshni beta parameter',
    'c11' : 'c11 elastic constant',
    'c12' : 'c12 elastic constant',
    'c44' : 'c44 elastic constant',
    'd' : 'd shear deformation potential',
    'dielectric' : 'static relative dielectric permittivity (i.e. <~ 1 THz)',
    'dielectric_high_frequency' : 'high-frequency dielectric permittivity '
                                  '(i.e. >~ 100 THz)',
    'electron_affinity' : 'electron affinity energy',
    'luttinger1' : 'first Luttinger parameter',
    'luttinger2' : 'second Luttinger parameter',
    'luttinger3' : 'third Luttinger parameter',
    'luttinger32' : 'difference between third and second Luttinger parameters '
                    '(luttinger3 - luttinger2)',
    'meff_SO' : 'split-off band effective mass',
    'meff_SO_0' : 'split-off band effective mass at 0 K',
    'meff_e_Gamma' : 'electron effective mass in the Gamma-valley',
    'meff_e_Gamma_0' : 'electron effective mass in the Gamma-valley at 0 K',
    'meff_e_L_DOS' : 'electron effective mass density of states in the L-valley',
    'meff_e_L_long' : 'electron effective mass in the longitudinal direction in the L-valley',
    'meff_e_L_trans' : 'electron effective mass in the transverse direction in the L-valley',
    'meff_e_X_DOS' : 'electron effective mass density of states in the X-valley',
    'meff_e_X_long' : 'electron effective mass in the longitudinal direction in the X-valley',
    'meff_e_X_trans' : 'electron effective mass in the transverse direction in the X-valley',
    'meff_hh_100' : 'heavy-hole effective mass in the <100> direction',
    'meff_hh_110' : 'heavy-hole effective mass in the <110> direction',
    'meff_hh_111' : 'heavy-hole effective mass in the <111> direction',
    'meff_lh_100' : 'light-hole effective mass in the <100> direction',
    'meff_lh_110' : 'light-hole effective mass in the <110> direction',
    'meff_lh_111' : 'light-hole effective mass in the <111> direction',
    'nonparabolicity' : 'Kane band nonparabolicity parameter for the Gamma-valley',
    'thermal_expansion' : 'lattice parameter thermal expansion coefficient',
    # strained
    'CBO_hydrostatic_strain_shift' : 'shift in the conduction band offset '
                                     'energy due to the hydrostatic strain '
                                     'component',
    'CBO_strain_shift' : 'total shift in the conduction band offset energy due to strain',
    'Eg_hh' : 'bandgap energy between the conduction band and the heavy-hole band',
    'Eg_lh' : 'bandgap energy between the conduction band and the light-hole band',
    'Eg_strain_shift' : 'total shift in the bandgap energy due to strain',
    'VBO_hh' : 'heavy-hole valance band offset energy',
    'VBO_lh' : 'light-hole valance band offset energy',
    'VBO_hh_strain_shift' : 'total shift in the heavy-hole valance band offset '
                            'energy due to strain',
    'VBO_lh_strain_shift' : 'total shift in the light-hole valance band offset '
                            'energy due to strain',
    'VBO_strain_shift' : 'total shift in the valance band offset energy due to strain',
    'VBO_hydrostatic_strain_shift' : 'shift in the valance band offset '
                                     'energy due to the hydrostatic strain '
                                     'component',
    'VBO_uniaxial_strain_shift' : 'shift in the valance band offset '
                                  'energy due to the uniaxial strain '
                                  'component',
    'substrate_a' : 'substrate lattice parameter',
    'strain_in_plane' : 'strain in the in-plane directions',
    'strain_out_of_plane' : 'strain in the out-of-plane direction '
                            '(the strain measured by X-ray diffraction '
                            'symmetric omega-2theta scans)',
}