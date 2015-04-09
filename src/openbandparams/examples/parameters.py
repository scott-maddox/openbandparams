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
# Make sure we import the local openbandparams version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from openbandparams import *
import string

# Print a parameter's description and units
print GaAs.Eg.description, ',', GaAs.Eg.units
print

# Print all parameters of all III-V zinc blende alloys
params = {}
for binary in iii_v_zinc_blende_binaries:
    for param in binary.get_unique_parameters():
        if param.name not in params:
            params[param.name] = param
names = [n for n,p in sorted(params.items())]
descriptions = [p.description for n,p in sorted(params.items())]
max_name_width = max([len(name) for name in names])
max_desc_width = max([len(desc) for desc in descriptions])
print '{} | {}'.format(string.ljust('Parameter', max_name_width),'Description')
print '-'*(max_name_width+max_desc_width+3)
for name, desc in zip(names, descriptions):
    print '{} | {}'.format(string.ljust(name, max_name_width),desc)