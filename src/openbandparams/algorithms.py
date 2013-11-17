#
#   Copyright (c) 2013, Scott J Maddox
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
##############################################################################

def sign(x):
    return cmp(x, 0)

def bisect(func, a, b, xtol=1e-12, maxiter=100):
    fa = func(a)
    if fa == 0.:
        return a
    
    fb = func(b)
    if fb == 0.:
        return b
    
    assert sign(fa) != sign(fb)
    
    for i in xrange(maxiter):
        c = (a + b) / 2.
        fc = func(c)
        if fc == 0. or abs(b - a)/2. < xtol:
            return c
        if sign(fc) == sign(func(a)):
            a = c
        else:
            b = c
    else:
        raise RuntimeError('Failed to converge after %d iterations.'%maxiter)
    