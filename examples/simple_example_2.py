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

from openbandparams.iii_v.zinc_blende.ternary import *

print '# All three of these are identical:'
print '>>> AlGaAs.Eg(x=0.3)\n', AlGaAs.Eg(x=0.3)
print '>>> AlGaAs.Eg(Al=0.3)\n', AlGaAs.Eg(Al=0.3)
print '>>> AlGaAs.Eg(Ga=0.7)\n', AlGaAs.Eg(Ga=0.7)
print ''

print '# All three of these are identical, '
print '# but different than the previous three:'
print '>>> GaAlAs.Eg(x=0.3)\n', GaAlAs.Eg(x=0.3)
print '>>> GaAlAs.Eg(Al=0.7)\n', GaAlAs.Eg(Al=0.7)
print '>>> GaAlAs.Eg(Ga=0.3)\n', GaAlAs.Eg(Ga=0.3)
print ''

print '# These four are identical:'
print '>>> AlGaAs.Eg(x=0.3)\n', AlGaAs.Eg_Gamma(x=0.3)
print '>>> AlGaAs(x=0.3).Eg_Gamma()\n', AlGaAs(x=0.3).Eg_Gamma()
print '>>> GaAlAs.Eg_Gamma(x=0.7)\n', GaAlAs.Eg_Gamma(x=0.7)
print '>>> GaAlAs(x=0.7).Eg_Gamma()\n', GaAlAs(x=0.7).Eg_Gamma()
print ''

print 'Alternate forms:'
print '>>> AlGaAs.Eg(x=0.3, T=300)\n', AlGaAs.Eg(x=0.3, T=300)
print '>>> AlGaAs(x=0.3).Eg()\n', AlGaAs(x=0.3).Eg()
print '>>> AlGaAs(x=0.3).Eg(T=300)\n', AlGaAs(x=0.3).Eg(T=300)
print ''

print ('This is the preferred usage (more efficient),'
       'if you want multiple parameters from one alloy composition:')
print '>>> myAlGaAs = AlGaAs(x=0.3)'
myAlGaAs = AlGaAs(x=0.3)
print '>>> myAlGaAs.Eg()\n', myAlGaAs.Eg()
print '>>> myAlGaAs.Eg(T=300)\n', myAlGaAs.Eg(T=300)
