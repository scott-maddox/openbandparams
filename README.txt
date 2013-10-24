openbandparams
==============

open source semiconductor band parameters

Motiviation
===========

The main goal of this project is to provide easy access to semiconductor band parameters for calculations and simulations. Basic functionality should require only the standard python distribution. More advanced functions may require additional third-party packages, such as numpy or scipy.

Useful and relavent algorithms will also be provided for tasks such as interpolating the parameters for alloys, calculating the intrinsic carrier concentration, calculating the carrier concentration for a given Fermi energy, calculating the Fermi energy at a given carrier concentration, and so on. Since some of these calculations can be fairly involved, particularly if simplifying approximations are not made, ease of use must be balanced with speed of execution. In those cases where ease of use is poor, several examples for usage will be provided.

Example scripts will also be provided for generating common plots such as bandgap vs. lattice constant, band alignments vs. lattice constant, bandgap vs. alloy composition, and so on.

Installation
============

To install, simply run the following command from a terminal:

	python setup.py install

For Windows, this command should be run from a command prompt window:

	setup.py install

Additional information on installation can be found [here](http://docs.python.org/2/install/).

Developers
==========

Additional information for developers can be found in `developers.txt`.