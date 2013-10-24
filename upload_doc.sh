#!/bin/sh

CWD="$(pwd)"
HTML_DIR="$CWD/doc/_build/html/"
TMP_DIR="/tmp/openbandparams-gh-pages/"
rm -rf $TMP_DIR
mkdir $TMP_DIR
cd $TMP_DIR
git clone ssh://git@github.com/scott-maddox/openbandparams.git
cd openbandparams
git pull origin gh-pages
rsync -av "$HTML_DIR" .
git add .
git commit -a -m "updated documentation"
git push origin HEAD:gh-pages
rm -rf "$TMP_DIR"
