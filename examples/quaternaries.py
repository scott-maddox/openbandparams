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

from openbandparams.iii_v.zinc_blende.binary import *
from openbandparams.iii_v.zinc_blende.quaternary import *
quat = GaInPAs(Ga=0.1, a=InP.a(), T=300)
print 'GaInPAs lattice matched to InP:'
print 'Ga fraction: ', quat.elementFraction('Ga')
print 'P fraction: ', quat.elementFraction('P')
quat = GaInPAs(As=0.1, a=InP.a(), T=300)
print 'GaInPAs lattice matched to InP:'
print 'Ga fraction: ', quat.elementFraction('Ga')
print 'P fraction: ', quat.elementFraction('P')