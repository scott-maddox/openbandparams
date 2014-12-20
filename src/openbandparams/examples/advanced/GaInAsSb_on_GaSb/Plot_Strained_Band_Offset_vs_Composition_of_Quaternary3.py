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
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from openbandparams import *

import matplotlib.pyplot as plt
import numpy

# Type 3 Quaternary
alloy = GaInAsSb

# calculate the data
T = 300  # K
N = 100
xs = numpy.linspace(0, 1, N)
ys = numpy.linspace(0, 1, N)
X, Y = numpy.meshgrid(xs, ys)
Z = numpy.empty(shape=(N, N), dtype=numpy.double)
W = numpy.empty(shape=(N, N), dtype=numpy.double)
for i in xrange(N):
    for j in xrange(N):
        eps_xx = alloy.biaxial_strained_eps_xx(x=X[i, j], y=Y[i, j],
                                               a0=GaSb.a(), T=T)
        if eps_xx < -0.03 or eps_xx > 0:
            Z[i, j] = numpy.nan
            W[i, j] = numpy.nan
        else:
            E_hh = alloy.biaxial_strained_E_hh(x=X[i, j], y=Y[i, j],
                                               a0=GaSb.a(), T=T)
            E_c = alloy.biaxial_strained_E_c(x=X[i, j], y=Y[i, j],
                                             a0=GaSb.a(), T=T)
            Z[i, j] = E_hh - GaSb.VBO()
            W[i, j] = GaSb.VBO() +GaSb.Eg(T=T) - E_c

# plot it
fig = plt.figure()
CS = plt.contour(1-X, 1-Y, Z, 14, colors='r')
plt.clabel(CS, inline=True, fontsize=10)
CS2 = plt.contour(1-X, 1-Y, W, 12, colors='g')
plt.clabel(CS2, inline=True, fontsize=10)
plt.title('$%s/GaSb$ from 0 to -3%% strain (T = %.0f K)' % (alloy.LaTeX(), T))
plt.xlabel('%s fraction' % alloy.elements[1])
plt.ylabel('%s fraction' % alloy.elements[3])
plt.plot([numpy.nan], [numpy.nan], 'g-', label='Conduction Band Offset')
plt.plot([numpy.nan], [numpy.nan], 'r-', label='Valance Band Offset')
plt.legend(loc='lower left')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        plt.savefig(output_filename)
    else:
        plt.show()