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
DOC_DIR = os.path.join(SCRIPT_DIR, 'doc')
DOC_EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'doc/examples')
BUILD_EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'doc/_build_examples')

if not os.path.exists(DOC_EXAMPLES_DIR):
    os.mkdir(DOC_EXAMPLES_DIR)
if not os.path.exists(BUILD_EXAMPLES_DIR):
    os.mkdir(BUILD_EXAMPLES_DIR)

# change to the src dir so that python imports the current openbandparams
# version
os.chdir(os.path.join(SCRIPT_DIR, 'src'))

print ''
print 'Building examples...'
examples = [f for f in os.listdir(EXAMPLES_DIR) if
            (f.endswith('.py') and not f.startswith('_'))]

# save a list of the examples
with open(os.path.join(BUILD_EXAMPLES_DIR,'examples.txt'), 'w') as f:
    for example in examples:
        f.write(example+'\n')

for example in examples:
    # build the result filename
    root, ext = os.path.splitext(example)
    if example.lower().startswith('plot'):
        result_type = 'image'
        result = root+'.png'
    else:
        result_type = 'literalinclude'
        result = root+'.txt' 

    # output an rst file for each example
    rst_path = os.path.join(DOC_EXAMPLES_DIR, root+'.rst')
    with open(rst_path, 'w') as f:
        title = root.replace('_', ' ')
        underline = '='*len(root)
        f.write('''{title}
{underline}

Source:

.. literalinclude:: ../../src/openbandparams/examples/{example}

Result:

.. {result_type}:: ../_build_examples/{result}
'''.format(title=title, underline=underline, result_type=result_type,
           example=example, result=result))
    
    # get the absolute paths
    example_path = os.path.join(EXAMPLES_DIR, example)
    result_path = os.path.join(BUILD_EXAMPLES_DIR, result)   
    
    # check if changes have been made to the example script
    if (os.path.exists(result_path) and
        os.path.getmtime(example_path) < os.path.getmtime(result_path)):
        # no changes -- skip running it
        continue
    
    # get the relative paths (for printing)
    example_relpath = os.path.relpath(example_path, CWD)
    result_relpath = os.path.relpath(result_path, CWD)
    
    # run the script and save the result
    print '  Running "{}"\n    Saving result to "{}"'.format(
                                        example_relpath, result_relpath)
    if result_type == 'image':
        subprocess.check_call(['python', example_path, result_path])
    elif result_type == 'literalinclude':
        with open(result_path, 'w') as f:
            subprocess.check_call(['python', example_path], stdout=f)
    else:
        raise RuntimeError('Unknown result_type: {}'.format(result_type))

print 'Done building examples.'
print ''

os.chdir('../doc')
subprocess.check_call(['make', 'html'])
