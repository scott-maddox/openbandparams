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

from openbandparams import *

# Some identities and inequalities
print "Type 1 Quaternary:", AlPAsSb
assert AlPAsSb(x=0, y=0) == AlPAsSb(P=0, y=0)
assert AlPAsSb(x=0, y=0) == AlPAsSb(x=0, As=0)
assert AlPAsSb(x=0, y=0) == AlPAsSb(P=0, As=0)
assert AlPAsSb(x=0, y=0) == AlPAsSb(P=0, Sb=1)
assert AlPAsSb(x=0, y=0) != GaPAsSb(x=0, y=0)
assert AlPAsSb(x=0, y=0) != AlPAsSb(x=1, y=0)
assert AlPAsSb(x=0, y=0) != AlPAsSb(x=0, y=1)
print "Type 2 Quaternary:", AlGaInAs
assert AlGaInAs(x=0, y=0) == AlGaInAs(Al=0, y=0)
assert AlGaInAs(x=0, y=0) == AlGaInAs(x=0, Ga=0)
assert AlGaInAs(x=0, y=0) == AlGaInAs(Al=0, Ga=0)
assert AlGaInAs(x=0, y=0) == AlGaInAs(Al=0, In=1)
assert AlGaInAs(x=0, y=0) != AlGaInSb(x=0, y=0)
assert AlGaInAs(x=0, y=0) != AlGaInAs(x=1, y=0)
assert AlGaInAs(x=0, y=0) != AlGaInAs(x=0, y=1)
print "Type 3 Quaternary:", AlGaPAs
assert AlGaPAs(x=0, y=0) == AlGaPAs(Al=0, y=0)
assert AlGaPAs(x=0, y=0) == AlGaPAs(x=0, P=0)
assert AlGaPAs(x=0, y=0) == AlGaPAs(Al=0, P=0)
assert AlGaPAs(x=0, y=0) == AlGaPAs(Ga=1, P=0)
assert AlGaPAs(x=0, y=0) == AlGaPAs(Al=0, As=1)
assert AlGaPAs(x=0, y=0) == AlGaPAs(Ga=1, As=1)
assert AlGaPAs(x=0, y=0) != AlGaPSb(x=0, y=0)
assert AlGaPAs(x=0, y=0) != AlGaPAs(x=1, y=0)
assert AlGaPAs(x=0, y=0) != AlGaPAs(x=0, y=1)

print ""
print repr(GaInPAs(x=0, y=0)), "-->", GaInPAs(x=0, y=0)
print repr(AlPAsSb(x=0, y=0)), "-->", AlPAsSb(x=0, y=0)
assert eval(repr(GaInPAs(Ga=0, P=0))) == GaInPAs(x=0, P=0)
print ''
print "Some GaInPAs alloys lattice matched to InP:"
print GaInPAs(Ga=0.1, a=InP.a(), T=300)
print GaInPAs(As=0.1, a=InP.a(), T=300)
print ''
print "Some AlPAsSb alloys lattice matched to InP (at room temperature):"
print AlPAsSb(P=0.1, a=InP.a(), T=300)
print AlPAsSb(As=0.1, a=InP.a(), T=300)
print AlPAsSb(Sb=0.5, a=InP.a(), T=300)
