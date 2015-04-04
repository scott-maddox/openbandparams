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

class Parameter(object):
    def __init__(self, name, units=None, aliases=None, references=None):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        units : string (default=None)
            units
        aliases : list of strings (default=None)
            list of alternate names
        references : list of Reference objects (default=None)
            literature references
        '''
        self.name = name
        self.units = units
        self.aliases = aliases
        self.references = references
    
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class ValueParameter(Parameter):
    def __init__(self, name, value, units=None,
                 aliases=None, references=None):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        value : object (default=None)
            value of the parameter
        units : string (default=None)
            units
        aliases : list of strings (default=None)
            list of alternate names
        references : list of Reference objects (default=None)
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
    def __init__(self, name, function, units=None,
                 aliases=None, references=None):
        '''
        Parameters
        ----------
        name : string
            name of the parameter
        function : callable function
            function that returns the value of the parameter
        units : string (default=None)
            units
        aliases : list of strings (default=None)
            list of alternate names
        references : list of Reference objects (default=None)
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
    def __init__(self, name, method, dependencies, units=None,
                 aliases=None, references=None):
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
        units : string (default=None)
            units
        aliases : list of strings (default=None)
            list of alternate names
        references : list of Reference objects (default=None)
            literature references
        '''
        super(MethodParameter, self).__init__(name=name,
                                              units=units,
                                              aliases=aliases,
                                              references=references)
        self.method = method
        self.dependencies = dependencies
    
    def __call__(self, *args, **kwargs):
        return self.method(self, *args, **kwargs)