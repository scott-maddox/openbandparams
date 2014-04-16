#!/bin/sh

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


CWD="$(pwd)"
HTML_DIR="$CWD/doc/_build/html/"
TMP_DIR="/tmp/openbandparams-gh-pages/"
rm -rf $TMP_DIR
mkdir $TMP_DIR
cd $TMP_DIR
git clone https://github.com/scott-maddox/openbandparams.git
cd openbandparams
git pull origin gh-pages
rsync -av "$HTML_DIR" .
git add .
git commit -a -m "updated documentation"
git push origin HEAD:gh-pages
rm -rf "$TMP_DIR"
