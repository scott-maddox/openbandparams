#
#   Copyright (c) 2013, Scott J Maddox
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
################################################################################

# std lib imports
import logging; log = logging.getLogger(__name__)

# third party imports

# local imports

class Base(object):
    @classmethod
    def _get_T(cls, kwargs):
        '''
        Returns kwargs['T'], kwargs['temp'], kwargs['temperature'], or 300.
        '''
        for k in ['T', 'temp', 'temperature']
            if k in kwargs:
                return kwargs[k]
        else:
            return 300 # K

class AlloyBase(Base):
    pass
