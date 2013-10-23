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

print 'All three of these are identical:'
print '`AlGaAs(x=0.3).Eg()`: %.3f eV'%AlGaAs(x=0.3).Eg()
print '`AlGaAs(Al=0.3).Eg()`: %.3f eV'%AlGaAs(Al=0.3).Eg()
print '`AlGaAs(Ga=0.7).Eg()`: %.3f eV'%AlGaAs(Ga=0.7).Eg()
print ''

print ('All three of these are identical, '
       'but different than the previous three:')
print '`GaAlAs(x=0.3).Eg()`: %.3f eV'%GaAlAs(x=0.3).Eg()
print '`GaAlAs(Al=0.7).Eg()`: %.3f eV'%GaAlAs(Al=0.7).Eg()
print '`GaAlAs(Ga=0.3).Eg()`: %.3f eV'%GaAlAs(Ga=0.3).Eg()
print ''

print 'These two are identical:'
print '`AlGaAs(x=0.3).Eg()`: %.3f eV'%AlGaAs(x=0.3).Eg()
print '`GaAlAs(x=0.7).Eg()`: %.3f eV'%GaAlAs(x=0.7).Eg()
print ''

print ('This is the preferred usage (more efficient),'
       'if you want multiple parameters from one alloy composition:')
myInGaAs = InGaAs(x=0.2)
print '`myInGaAs = InGaAs(x=0.2)`'
print '`myInGaAs.Eg_X()`: %.3f eV'%myInGaAs.Eg_X()
print '`myInGaAs.Eg()`: %.3f eV'%myInGaAs.Eg()
