.. openbandparams documentation master file, created by
   sphinx-quickstart on Tue Oct 22 23:42:33 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to openbandparams's documentation!
==========================================

This is the first public release of openbandparams.

The main goal of this project is to provide easy access to semiconductor band parameters for calculations and simulations. Basic functionality requires only the standard python distribution.

Example scripts are provided for basic usage and for generating common plots such as bandgap vs. lattice constant, bandgap vs. alloy composition.

Included parameters:
    - lattice constant
    - thermal expansion coefficient
    - bandgap energies (direct and indirect)
    - Varshni parameters
    - split-off energies
    - effective masses
    - Luttinger parameters
    - Kane parameters (Ep and F)
    - Valance band offsets
    - band deformation potentials
    - elastic constant
    - alloy bowing parameters

Included materials:
    - III-V's
        - Zinc Blendes
            - Binaries
                - AlN, GaN, InN,
                  AlP, GaP, InP,
                  AlAs, GaAs, InAs,
                  AlSb, GaSb, InSb
            - Ternaries
                - AlGaN,  AlInN,  GaInN,
                  AlGaP,  AlInP,  GaInP,
                  AlGaAs, AlInAs, GaInAs,
                  AlGaSb, AlInSb, GaInSb,
                  AlNP,   GaNP,   InNP,
                  AlNAs,  GaNAs,  InNAs,
                  AlPAs,  GaPAs,  InPAs,
                  AlPSb,  GaPSb,  InPSb,
                  AlAsSb, GaAsSb, InAsSb,
                  GaAlN,  InAlN,  InGaN,
                  GaAlP,  InAlP,  InGaP,
                  GaAlAs, InAlAs, InGaAs,
                  GaAlSb, InAlSb, InGaSb,
                  AlPN,   GaPN,   InPN,
                  AlAsN,  GaAsN,  InAsN,
                  AlAsP,  GaAsP,  InAsP,
                  AlSbP,  GaSbP,  InSbP,
                  AlSbAs, GaSbAs, InSbAs

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

