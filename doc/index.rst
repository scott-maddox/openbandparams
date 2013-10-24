.. openbandparams documentation master file, created by
   sphinx-quickstart on Tue Oct 22 23:42:33 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to openbandparams's documentation!
==========================================

The main goal of this project is to provide easy access to semiconductor band parameters for calculations and simulations. Basic functionality should require only the standard python distribution. More advanced functions may require additional third-party packages, such as numpy or scipy.

Useful and relavent algorithms will also be provided for tasks such as interpolating the parameters for alloys, calculating the intrinsic carrier concentration, calculating the carrier concentration for a given Fermi energy, calculating the Fermi energy at a given carrier concentration, and so on. Since some of these calculations can be fairly involved, particularly if simplifying approximations are not made, ease of use must be balanced with speed of execution. In those cases where ease of use is poor, several examples for usage will be provided.

Example scripts will also be provided for generating common plots such as bandgap vs. lattice constant, band alignments vs. lattice constant, conduction band minima vs. alloy composition, and so on.

The source code and example usage scripts are available from the `Github repository`_, and additional documentation is available in the :ref:`modindex`.

.. _Github repository: http://github.com/scott-maddox/openbandparams

Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

