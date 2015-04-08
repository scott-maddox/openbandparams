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

unstrained = GaInAs(In=0.3)
print 'unstrained Eg', unstrained.Eg()
strained = unstrained.strained_001(GaAs)  # specify substrate
# strained = unstrained.strained_001(0.02)  # specify out-of-plane strain
print '  strained Eg', strained.Eg()
print
# Print a table of material parameters
rows = []
num_cols = 3
rows.append(['Parameter', 'Unstrained', 'Strained'])
rows.append(['latex', unstrained.latex(), strained.latex()])
for parameter in ['strain_out_of_plane', 'strain_in_plane',
                  'CBO_strain_shift',
                  'VBO_hh_strain_shift', 'VBO_lh_strain_shift']:
    s = getattr(strained, parameter)()
    rows.append([parameter, '', '{:g}'.format(s)])
for parameter in ['CBO', 'VBO', 'Eg']:
    u = getattr(unstrained, parameter)()
    s = getattr(strained, parameter)()
    rows.append([parameter, '{:g}'.format(u), '{:g}'.format(s)])
col_widths = [max([len(row[col]) for row in rows]) for col in xrange(num_cols)]
import string
# print header
print ' | '.join([string.ljust(rows[0][col],col_widths[col]) for col in xrange(num_cols)])
print '-'*(sum(col_widths)+len(' | ')*(num_cols-1))
for row in rows[1:]:
    print ' | '.join([string.ljust(row[col],col_widths[col]) for col in xrange(num_cols)])