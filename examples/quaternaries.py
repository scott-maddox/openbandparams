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

# Some identities
assert GaInPAs(x=0, y=0) == GaInPAs(Ga=0, P=0)
assert GaInPAs(x=0, y=0) == GaInPAs(x=0, P=0)
assert GaInPAs(x=0, y=0) == GaInPAs(Ga=0, y=0)
assert GaInPAs(x=0, y=0) == GaInPAs(Ga=0, As=1)
assert GaInPAs(x=0, y=0) == GaInPAs(In=1, As=1)
assert eval(repr(GaInPAs(Ga=0, P=0))) == GaInPAs(x=0, P=0)

# Some inequalities
assert GaInPAs(x=0, y=0) != GaInPSb(x=0, y=0)

# Some examples
print 'GaInPAs lattice matched to InP:', GaInPAs(Ga=0.1, a=InP.a(), T=300)
print 'GaInPAs lattice matched to InP:', GaInPAs(As=0.1, a=InP.a(), T=300)

print 'AlPAsSb(x=.1, y=.3):', AlPAsSb(x=.1, y=.3)
print 'AlPAsSb(P=.1, y=.3):', AlPAsSb(P=.1, y=.3)
print 'AlPAsSb(P=.1, As=.3):', AlPAsSb(P=.1, As=.3)
print 'AlPAsSb(As=.3, Sb=.6):', AlPAsSb(As=.3, Sb=.6)
print 'AlPAsSb(P=.1, Sb=.6):', AlPAsSb(P=.1, Sb=.6)
print repr(AlPAsSb(P=0, As=0))
print 'AlPAsSb lattice matched to InP:', AlPAsSb(P=0, As=0)
print 'AlPAsSb lattice matched to InP:', AlPAsSb(P=0.1, a=InP.a(), T=300)
print 'AlPAsSb lattice matched to InP:', AlPAsSb(As=0.1, a=InP.a(), T=300)
print 'AlPAsSb lattice matched to InP:', AlPAsSb(Sb=0.5, a=InP.a(), T=300)