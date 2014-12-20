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
# Make sure we import the local openbandparams version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from openbandparams import *

# Print an unformatted temperature dependent parameters
print 'GaAs bandgap (at T = 300 K): ', GaAs.Eg(), 'eV'
print ''

# Print some temperature dependent parameters
print 'GaAs bandgap (at T = 300 K):  %.3f eV' % GaAs.Eg()
print 'GaAs Gamma-valley gap (at T = 300 K):  %.3f eV' % GaAs.Eg_Gamma()
print 'GaAs X-valley gap (at T = 300 K):  %.3f eV' % GaAs.Eg_X()
print 'GaAs bandgap (at T = 0 K):  %.3f eV' % GaAs.Eg(T=0)
print 'InAs bandgap (at T = 300 K):  %.3f eV' % InAs.Eg()
print ''

# Print some temperature independent parameter
print ('GaAs electron effective mass in'
       ' the Gamma-valley:  %.3f m0' % GaAs.meff_e_Gamma())
print ''
print ('GaAs electron effective mass in the X-valley '
       'in the longitudinal direction:  %.3f m0' % GaAs.meff_e_X_long())
print ('GaAs electron effective mass in the X-valley '
       'in the transverse direction:  %.3f m0' % GaAs.meff_e_X_trans())
print ('GaAs electron density-of-states effective mass in'
       ' the X-valley:  %.3f m0' % GaAs.meff_e_X_DOS())
print ''
print ('GaAs electron effective mass in the L-valley '
       'in the longitudinal direction:  %.3f m0' % GaAs.meff_e_L_long())
print ('GaAs electron effective mass in the L-valley '
       'in the transverse direction:  %.3f m0' % GaAs.meff_e_L_trans())
print ('GaAs electron density-of-states effective mass in'
       ' the L-valley:  %.3f m0' % GaAs.meff_e_L_DOS())
print ''
print ('GaAs heavy-hole effective mass '
       'in the [100] direction:  %.3f m0' % GaAs.meff_hh_100())
print ('GaAs heavy-hole effective mass '
       'in the [110] direction:  %.3f m0' % GaAs.meff_hh_110())
print ('GaAs heavy-hole effective mass '
       'in the [111] direction:  %.3f m0' % GaAs.meff_hh_111())
print ''
print ('GaAs light-hole effective mass '
       'in the [100] direction:  %.3f m0' % GaAs.meff_lh_100())
print ('GaAs light-hole effective mass '
       'in the [110] direction:  %.3f m0' % GaAs.meff_lh_110())
print ('GaAs light-hole effective mass '
       'in the [111] direction:  %.3f m0' % GaAs.meff_lh_111())
print ''
print ('GaAs split-off band effective mass:'
       '  %.3f m0' % GaAs.meff_SO())
print ''

# Print a table of material lattice parameters and bandgaps
import string
print ' Material | Lattice Param. [Ang] | Bandgap [eV]'
print '------------------------------------------------'
for mat in binaries:
    print string.rjust(str(mat), 7),
    print '  | ', string.rjust('%.3f' % mat.a(), 12), ' ' * 4,
    print '  |    %.3f' % mat.Eg()
