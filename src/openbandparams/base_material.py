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


class BaseType(type):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Base(object):

    name = 'Base'
    elements = tuple([])

    @classmethod
    def elementFraction(cls, element):
        raise NotImplementedError()

    @classmethod
    def _get_T(cls, kwargs):
        '''
        Returns kwargs['T'], kwargs['temp'], kwargs['temperature'], or 300.
        '''
        for k in ['T', 'temp', 'temperature']:
            if k in kwargs:
                return kwargs[k]
        else:
            return 300  # K


class AlloyBase(Base):
    name = 'AlloyBase'
