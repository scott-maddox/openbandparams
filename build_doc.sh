#!/bin/sh

sphinx-apidoc -f -o doc src/openbandparams/ -d 2
cd doc
make html
