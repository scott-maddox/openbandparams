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
__all__ = ['IIIVZincBlendeBinary']

from .iii_v_zinc_blende_alloy import IIIVZincBlendeAlloy


class IIIVZincBlendeBinary(IIIVZincBlendeAlloy):
    '''
    The base class for all III-V zinc blende binary alloys.
    '''
    def __repr__(self):
        return self.name
    
    def latex(self):
        return self.name
    
    def element_fraction(self, element):
        '''
        Returns the fractional concentration of `element` with respect
        to its sublattice. In a III-V binary, the fraction is either 1 if
        `element` is present, or 0 if it is not.
        '''
        if element in self.elements:
            return 1.
        else:
            return 0.
