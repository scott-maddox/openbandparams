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
# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from openbandparams import (iii_v_zinc_blende_quaternaries, GaAs, AlAs, GaSb,
                            AlGaInAs, AlPAsSb, AlGaAsSb, GaPAsSb, AlGaInSb,
                            AlGaPAs, AlInAsSb)
from openbandparams import *
import unittest


class TestIIIVZincBlendeQuaternary(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(AlGaInAs), 'AlGaInAs')
        for quaternary in iii_v_zinc_blende_quaternaries:
            self.assertEqual(str(quaternary), quaternary.name)

    def test_repr(self):
        self.assertEqual(eval(repr(AlGaInAs(x=0, y=0))),
                         AlGaInAs(x=0, y=0))
        for quaternary in iii_v_zinc_blende_quaternaries:
            self.assertEqual(eval(repr(quaternary)), quaternary)
            self.assertEqual(eval(repr(quaternary(x=0, y=0))),
                             quaternary(x=0, y=0))
            self.assertEqual(eval(repr(quaternary(x=0, y=0.1))),
                             quaternary(x=0, y=0.1))
            self.assertEqual(eval(repr(quaternary(x=0.1, y=0))),
                             quaternary(x=0.1, y=0))
            self.assertEqual(eval(repr(quaternary(x=0.1, y=0.1))),
                             quaternary(x=0.1, y=0.1))

    def test_quaternary1_latex(self):
        self.assertEqual(AlPAsSb.latex(), 'AlP_{x}As_{y}Sb_{1-x-y}')
        self.assertEqual(AlPAsSb(x=0, y=0).latex(),
                         'AlP_{0}As_{0}Sb_{1}')

    def test_quaternary2_latex(self):
        self.assertEqual(AlGaInAs.latex(), 'Al_{x}Ga_{y}In_{1-x-y}As')
        self.assertEqual(AlGaInAs(x=0, y=0).latex(),
                         'Al_{0}Ga_{0}In_{1}As')

    def test_quaternary3_latex(self):
        self.assertEqual(AlGaAsSb.latex(), 'Al_{x}Ga_{1-x}As_{y}Sb_{1-y}')
        self.assertEqual(AlGaAsSb(x=0, y=0).latex(),
                         'Al_{0}Ga_{1}As_{0}Sb_{1}')

    def test_quaternary1_eq(self):
        self.assertEqual(AlPAsSb, AlPAsSb)
        self.assertNotEqual(AlPAsSb, GaPAsSb)
        self.assertEqual(AlPAsSb(x=0, y=0), AlPAsSb(x=0, y=0))
        self.assertEqual(AlPAsSb(x=0, y=0), AlPAsSb(P=0, y=0))
        self.assertEqual(AlPAsSb(x=0, y=0), AlPAsSb(x=0, As=0))
        self.assertEqual(AlPAsSb(x=0, y=0), AlPAsSb(P=0, As=0))
        self.assertEqual(AlPAsSb(x=0, y=0), AlPAsSb(P=0, Sb=1))

    def test_quaternary2_eq(self):
        self.assertEqual(AlGaInAs, AlGaInAs)
        self.assertNotEqual(AlGaInAs, AlGaInSb)
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(x=0, y=0))
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(Al=0, y=0))
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(x=0, Ga=0))
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(Al=0, Ga=0))
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(Al=0, In=1))

    def test_quaternary3_eq(self):
        self.assertEqual(AlGaAsSb, AlGaAsSb)
        self.assertNotEqual(AlGaAsSb, AlGaPAs)
        self.assertEqual(AlGaAsSb(x=0, y=0), AlGaAsSb(x=0, y=0))
        self.assertEqual(AlGaAsSb(x=0, y=0), AlGaAsSb(Al=0, y=0))
        self.assertEqual(AlGaAsSb(x=0, y=0), AlGaAsSb(x=0, As=0))
        self.assertEqual(AlGaAsSb(x=0, y=0), AlGaAsSb(Al=0, As=0))

    def test_quaternary1_lattice_matching(self):
        self.assertEqual(AlGaInAs(x=0, y=0), AlGaInAs(x=0, y=0))

    def test_quaternary1_missing_kwarg(self):
        with self.assertRaises(TypeError):
            AlPAsSb.Eg()
        with self.assertRaises(TypeError):
            AlPAsSb.Eg(x=0)
        with self.assertRaises(TypeError):
            AlPAsSb.Eg(y=0)
        with self.assertRaises(TypeError):
            AlPAsSb.Eg(a=6.)
        with self.assertRaises(TypeError):
            AlPAsSb.Eg(a=6., T=300)

    def test_quaternary2_missing_kwarg(self):
        with self.assertRaises(TypeError):
            AlGaInAs.Eg()
        with self.assertRaises(TypeError):
            AlGaInAs.Eg(x=0)
        with self.assertRaises(TypeError):
            AlGaInAs.Eg(y=0)
        with self.assertRaises(TypeError):
            AlGaInAs.Eg(a=6.)
        with self.assertRaises(TypeError):
            AlGaInAs.Eg(a=6., T=300)

    def test_quaternary3_missing_kwarg(self):
        with self.assertRaises(TypeError):
            AlGaAsSb.Eg()
        with self.assertRaises(TypeError):
            AlGaAsSb.Eg(x=0)
        with self.assertRaises(TypeError):
            AlGaAsSb.Eg(y=0)
        with self.assertRaises(TypeError):
            AlGaAsSb.Eg(a=6.)
        with self.assertRaises(TypeError):
            AlGaAsSb.Eg(a=6., T=300)

    def test_Eg(self):
        self.assertEqual(AlGaPAs(x=0, y=0).Eg(), GaAs.Eg())
        self.assertEqual(AlGaPAs(x=1, y=0).Eg(), AlAs.Eg())

    def test_non_instanced_lattice_matching(self):
        Eg1 = AlInAsSb(Al=0, a=GaSb.a()).Eg()
        Eg2 = AlInAsSb(Al=0, a=GaSb.a(), T=300.).Eg()
        self.assertEqual(Eg1, Eg2)

if __name__ == '__main__':
    unittest.main()
