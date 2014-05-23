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

from openbandparams.iii_v.zinc_blende.binary import GaAs, AlAs
from openbandparams.iii_v.zinc_blende.ternary import (AlGaAs, GaAsSb, AlPAs,
                                                      GaInAs)
from openbandparams.iii_v.zinc_blende.ternary import *
import unittest


class TestIIIVZincBlendeTernary(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(AlGaAs), 'AlGaAs')
        self.assertEqual(str(GaAsSb), 'GaAsSb')

    def test_repr(self):
        for ternary in ternaries:
            self.assertEqual(eval(repr(ternary)), ternary)
            self.assertEqual(eval(repr(ternary(x=0))), ternary(x=0))
            self.assertEqual(eval(repr(ternary(x=1))), ternary(x=1))
            self.assertEqual(eval(repr(ternary(x=0.1))), ternary(x=0.1))

    def test_LaTeX(self):
        self.assertEqual(AlGaAs.LaTeX(), 'Al_{x}Ga_{1-x}As')
        self.assertEqual(AlGaAs(x=0.1).LaTeX(), 'Al_{0.1}Ga_{0.9}As')
        self.assertEqual(AlGaAs(Al=0.1).LaTeX(), 'Al_{0.1}Ga_{0.9}As')
        self.assertEqual(AlGaAs(Ga=0.9).LaTeX(), 'Al_{0.1}Ga_{0.9}As')
        self.assertEqual(AlPAs.LaTeX(), 'AlP_{x}As_{1-x}')
        self.assertEqual(AlPAs(x=0.1).LaTeX(), 'AlP_{0.1}As_{0.9}')
        self.assertEqual(AlPAs(P=0.1).LaTeX(), 'AlP_{0.1}As_{0.9}')
        self.assertEqual(AlPAs(As=0.9).LaTeX(), 'AlP_{0.1}As_{0.9}')

    def test_eq(self):
        self.assertEqual(AlGaAs, AlGaAs)
        self.assertNotEqual(AlGaAs, GaInAs)
        self.assertEqual(AlGaAs(x=0), AlGaAs(Al=0))
        self.assertEqual(AlGaAs(x=0), AlGaAs(Ga=1))
        self.assertEqual(AlGaAs(Al=0), AlGaAs(Ga=1))
        self.assertEqual(AlPAs(x=0), AlPAs(P=0))
        self.assertEqual(AlPAs(x=0), AlPAs(As=1))
        self.assertEqual(AlPAs(P=0), AlPAs(As=1))

    def test_missing_x(self):
        with self.assertRaises(TypeError):
            AlGaAs.Eg()

    def test_Eg(self):
        self.assertEqual(AlGaAs.Eg(x=0), GaAs.Eg())
        self.assertEqual(AlGaAs(x=0).Eg(), GaAs.Eg())
        self.assertEqual(AlGaAs.Eg(x=1), AlAs.Eg())
        self.assertEqual(AlGaAs(x=1).Eg(), AlAs.Eg())

if __name__ == '__main__':
    unittest.main()
