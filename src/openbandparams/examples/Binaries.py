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

print 'Binary:', GaAs
# Print an unformatted temperature dependent parameters
print 'GaAs bandgap (at T = 300 K): ', GaAs.Eg(), 'eV'
print ''

# Print some formatted temperature dependent parameters
print 'GaAs bandgap (at T = 300 K):  %.3f eV' % GaAs.Eg()
print 'GaAs Gamma-valley gap (at T = 300 K):  %.3f eV' % GaAs.Eg_Gamma()
print 'GaAs X-valley gap (at T = 300 K):  %.3f eV' % GaAs.Eg_X()
print 'GaAs bandgap (at T = 0 K):  %.3f eV' % GaAs.Eg(T=0)
print 'InAs bandgap (at T = 300 K):  %.3f eV' % InAs.Eg()
print ''

# Print a temperature independent parameter
print ('InAs electron effective mass in'
       ' the Gamma-valley:  %.3f eV' % InAs.meff_e_Gamma())
print ''

# Print a table of material lattice parameters and bandgaps
import string
print ' Material | Lattice Param. [Ang] | Bandgap [eV]'
print '------------------------------------------------'
for mat in binaries:
    print string.rjust(str(mat), 7),
    print '  | ', string.rjust('%.3f' % mat.a(), 12), ' ' * 4,
    print '  |    %.3f' % mat.Eg()
