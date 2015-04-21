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

from .parameter import Parameter, MethodParameter

__all__ = ['Alloy']


class Alloy(object):

    def __init__(self, name, elements, parameters=None):
        self.name = name
        self.elements = elements
        self._parameters = {}
        self._aliases = {}
        if parameters is not None:
            for parameter in parameters:
                self.set_parameter(parameter)

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.name == other.name and
                self.elements == other.elements,
                self._parameters == other._parameters)
    
    def __getattribute__(self, name):
        if name in ['_parameters', '_aliases']:
            return super(Alloy, self).__getattribute__(name)
        if name in self._parameters:
            return self._parameters[name]
        elif name in self._aliases:
            return self._parameters[self._aliases[name]]
        
        try:
            item = super(Alloy, self).__getattribute__(name)
        except AttributeError as e:
            msg = e.message.replace('object',
                                    "object '{}'".format(self.name))
            raise AttributeError(msg)
        if isinstance(item, MethodParameter):
            # make sure MethodParameters defined with the class
            # are bound to this Alloy
            return item.bind(alloy=self)
        else:
            return item

    def __str__(self):
        return self.name
    
#     def __repr__(self):
#         return self.name
    
    def latex(self):
        '''
        Returns a LaTeX representation of the alloy.
        '''
        raise NotImplementedError()

    def element_fraction(self, element):
        '''
        Returns the atomic fraction of the given ``element``.
        '''
        raise NotImplementedError()

    def _add_parameter(self, parameter):
        '''
        Force adds a `Parameter` object to the instance.
        '''
        if isinstance(parameter, MethodParameter):
            # create a bound instance of the MethodParameter
            parameter = parameter.bind(alloy=self)
        self._parameters[parameter.name] = parameter
        for alias in parameter.aliases:
            self._aliases[alias] = parameter
    
    def add_parameter(self, parameter, overload=False):
        '''
        Adds a `Parameter` object to the instance.
        
        If a `Parameter` with the same name or alias has already been added
        and `overload` is False (the default), a `ValueError` is thrown.
        
        If a class member or method with the same name or alias is already
        defined, a `ValueError` is thrown, regardless of the value of overload.
        '''
        if not isinstance(parameter, Parameter):
            raise TypeError('`parameter` must be an instance of `Parameter`')

        if hasattr(self, parameter.name):
            item = getattr(self, parameter.name)
            if not isinstance(item, Parameter):
                raise ValueError('"{}" is already a class member or method.'
                                 ''.format(parameter.name))
            elif not overload:
                raise ValueError('Parameter "{}" has already been added'
                                 ' and overload is False.'
                                 ''.format(parameter.name))
        if parameter.name in self._parameters and not overload:
            raise ValueError('Parameter "{}" has already been added'
                             ' and overload is False.'
                             ''.format(parameter.name))
        for alias in parameter.aliases:
            if alias in self._aliases and not overload:
                raise ValueError('Alias "{}" has already been added'
                                 ' and overload is False.'
                                 ''.format(parameter.name))
        self._add_parameter(parameter)
    
    def set_parameter(self, parameter):
        '''
        Same as calling ``add_parameter`` with ``overload=True``
        '''
        self.add_parameter(parameter, overload=True)
    
    def has_parameter(self, name):
        '''
        Returns True if the named parameter is present, or False, otherwise.
        '''
        return self.get_parameter(name, default=None) is not None
    
    def get_parameter(self, name, default=None):
        '''
        Returns the named parameter if present, or the value of `default`,
        otherwise.
        '''
        if hasattr(self, name):
            item = getattr(self, name)
            if isinstance(item, Parameter):
                return item
        return default
    
    def get_unique_parameters(self):
        '''
        Returns a list of the unique parameters (no duplicates).
        '''
        # start with parameters in the `_parameters` dictionary
        parameters = self._parameters.values()
        # add parameters defined with the class
        for name in dir(self):
            item = getattr(self, name)
            if isinstance(item, Parameter):
                if item.name not in self._parameters:
                    parameters.append(item)
        return parameters