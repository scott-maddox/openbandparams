#!/usr/bin/env python

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

import os
import os.path
import subprocess

CWD = os.getcwd()

# sphinx-apidoc -f -o doc -d 4 src/openbandparams/
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'src/openbandparams/examples')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'doc/_examples_output')

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

examples = [('binaries.py', 'binaries.txt'),
            ('ternaries.py', 'ternaries.txt'),
            ('quaternaries.py', 'quaternaries.txt'),
            ('GaPSb_on_InP.py', 'GaPSb_on_InP.txt'),
            ('plot_bandgap_vs_composition_of_quaternary3.py',
             'plot_bandgap_vs_composition_of_quaternary3.png'),]

# change to the src dir so that python imports the current openbandparams
# version
os.chdir(os.path.join(SCRIPT_DIR, 'src'))

print ''
print 'Updating example ouputs...'
for example, output in examples:
    example_path = os.path.join(EXAMPLES_DIR, example)
    output_path = os.path.join(OUTPUT_DIR, output)
    # check if changes have been made
    if (os.path.exists(output_path) and
        os.path.getmtime(example_path) < os.path.getmtime(output_path)):
        # no changes -- skip it
        continue
    example_relpath = os.path.relpath(example_path, CWD)
    output_relpath = os.path.relpath(output_path, CWD)
    with open(output_path, 'w') as f:
        print '  Running "{}"\n    Saving output to "{}"'.format(
                                            example_relpath, output_relpath)
        subprocess.check_call(['python', example_path, 'stdout'],
                              stdout=f)
print 'Done updating example ouputs.'
print ''

os.chdir('../doc')
subprocess.check_call(['make', 'html'])
