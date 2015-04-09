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
# Make sure we import the local openbandparams version
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from openbandparams import *

AlInAs_InP = AlInAs(a=InP.a())
GaInAs_InP = GaInAs(a=InP.a())

AlGaInAs_InP = IIIVZincBlendeTernary(
    name='AlGaInAs/InP',
    elements=('Al', 'Ga', 'InAs'),
    binaries=(AlInAs_InP, GaInAs_InP),
    parameters=[])

instance1 = AlGaInAs_InP(Al=0.5)
print instance1.latex()
print 'instance1.Eg =', instance1.Eg()

# Change a parameter in the GaInAs_InP instance, which propogates to all
# AlGaInAs_InP instances, due to lazy evaluation.
GaInAs_InP.set_parameter(ValueParameter('Eg_Gamma', 1., 'eV'))
print 'instance1.Eg =', instance1.Eg()

# Change a bowing parameter in the AlGaInAs_InP instance.
instance1.set_parameter(ValueParameter('Eg_Gamma_bowing', 1., 'eV'))
print 'instance1.Eg =', instance1.Eg()

# Other instances of AlGaInAs_InP are not affected.
instance2 = AlGaInAs_InP(Al=0.5)
print 'instance2.Eg =', instance2.Eg()

# However, we can adopt the altered parameter in a new instance, by
# instancing off of the altered instance. This is possible due to
# shallow copying on instancing.
instance1_copy = instance1(Al=0.5)
print 'instance1_copy.Eg =', instance1_copy.Eg()

# Once split, they each have their own list of parameters, though.
instance1.set_parameter(ValueParameter('Eg_Gamma_bowing', 2., 'eV'))
print 'instance1.Eg =', instance1.Eg()
print 'instance1_copy.Eg =', instance1_copy.Eg()

# Changing a parameter in AlGaInAs_InP, directly, alters all future instances,
# but not existing instances.
AlGaInAs_InP.set_parameter(ValueParameter('Eg_Gamma_bowing', 3., 'eV'))
print 'instance1.Eg =', instance1.Eg()
print 'instance2.Eg =', instance2.Eg()
instance3 = AlGaInAs_InP(Al=0.5)
print 'instance3.Eg =', instance3.Eg()
instance4 = AlGaInAs_InP(Al=0.5)
print 'instance4.Eg =', instance4.Eg()