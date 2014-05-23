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

print '# All three of these are identical:'
print '>>> AlGaAs.Eg(x=0.3)\n', AlGaAs.Eg(x=0.3)
print '>>> AlGaAs.Eg(Al=0.3)\n', AlGaAs.Eg(Al=0.3)
print '>>> AlGaAs.Eg(Ga=0.7)\n', AlGaAs.Eg(Ga=0.7)
print ''

print '# These two are identical:'
print '>>> AlGaAs.Eg(x=0.3)\n', AlGaAs.Eg_Gamma(x=0.3)
print '>>> AlGaAs(x=0.3).Eg_Gamma()\n', AlGaAs(x=0.3).Eg_Gamma()
print ''

print 'Alternate forms:'
print '>>> AlGaAs.Eg(x=0.3, T=300)\n', AlGaAs.Eg(x=0.3, T=300)
print '>>> AlGaAs(x=0.3).Eg()\n', AlGaAs(x=0.3).Eg()
print '>>> AlGaAs(x=0.3).Eg(T=300)\n', AlGaAs(x=0.3).Eg(T=300)
print ''

print ('This is the preferred usage (more efficient),'
       'if you want multiple parameters from one alloy composition:')
print '>>> myAlGaAs = AlGaAs(x=0.3)\n',
myAlGaAs = AlGaAs(x=0.3)
print '>>> myAlGaAs.Eg()\n', myAlGaAs.Eg()
print '>>> myAlGaAs.Eg(T=300)\n', myAlGaAs.Eg(T=300)

print 'Lattice matching to a substrate (at the growth temperature):'
print '>>> a_InP = InP.a(T=800)\n',
a_InP = InP.a(T=800)
print '>>> GaInAs_on_InP = GaInAs(a=a_InP, T=800)\n',
GaInAs_on_InP = GaInAs(a=a_InP, T=800)
print '>>> InP.a(T=800)\n', InP.a(T=800)
print '>>> GaInAs_on_InP.a()\n', GaInAs_on_InP.a(T=800)
print '>>> GaInAs_on_InP.elementFraction("Ga")\n', \
       GaInAs_on_InP.elementFraction("Ga")
print '>>> GaInAs_on_InP.Eg()\n', GaInAs_on_InP.Eg()
