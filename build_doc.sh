#!/bin/sh

sphinx-apidoc -f -o doc src/openbandparams/
cd doc
make html
