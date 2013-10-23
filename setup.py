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

from setuptools import setup, find_packages

# read in __version__
exec(open('src/openbandparams/version.py').read())

setup(name='openbandparams',
      version=__version__, # read from version.py
      description='open source semiconductor band parameters',
      url='https://github.com/scott-maddox/openbandparams',
      author='Scott Maddox',
      author_email='smaddox@utexas.edu',
      license='AGPLv3',
      packages=['openbandparams'],
      package_dir={'openbandparams': 'src/openbandparams'},
      zip_safe=True)
