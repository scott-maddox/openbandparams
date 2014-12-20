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


quaternary = GaInAsSb
T = 300

# initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('$%s/GaSb$ from 0 to -3%% strain' % (quaternary.LaTeX()))
plt.xlabel('Unstrained Lattice Parameter at %g K ($\AA$)' % T)
plt.ylabel('Strained Band Offset at %g K (eV)' % T)

# plot the binaries
xs = []
ys = []
labels = []
for b in [GaSb, InAs, InSb]:
    xs.append(b.a(T=T))
    ys.append(b.VBO(T=T))
    labels.append(b.name)
ax.plot(xs, ys, 'bo')

# label the binaries
for x, y, label in zip(xs, ys, labels):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')

# plot the binaries
xs = []
ys = []
labels = []
for b in [GaSb, InAs, InSb]:
    xs.append(b.a(T=T))
    ys.append(b.VBO() + b.Eg_Gamma(T=T))
    labels.append(b.name)
ax.plot(xs, ys, 'ro')

# label the binaries
for x, y, label in zip(xs, ys, labels):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')

# plot the quaternary
indices = numpy.arange(100)
fractions = numpy.linspace(0, 1, 100)
x = numpy.empty(100, dtype=numpy.float)
E_c = numpy.empty(100, dtype=numpy.float)
E_hh = numpy.empty(100, dtype=numpy.float)
first = True
for xfrac in numpy.linspace(0, 1, 10):
    for i, yfrac in zip(indices, fractions):
        instance = quaternary(x=xfrac, y=yfrac)
        x[i] = instance.a(T=T)
        eps_xx = quaternary.biaxial_strained_eps_xx(x=xfrac, y=yfrac,
                                                    a0=GaSb.a(), T=T)
        if eps_xx < -0.03 or eps_xx > 0:
            E_c[i] = numpy.nan
            E_hh[i] = numpy.nan
        else:
            E_c[i] = quaternary.biaxial_strained_E_c(x=xfrac, y=yfrac,
                                                     a0=GaSb.a(), T=T)
            E_hh[i] = quaternary.biaxial_strained_E_hh(x=xfrac, y=yfrac,
                                                       a0=GaSb.a(), T=T)
    if first:
        ax.plot(x, E_c, 'r-', label='E_c')
        ax.plot(x, E_hh, 'b-', label='E_hh')
        first = False
    else:
        ax.plot(x, E_c, 'r-')
        ax.plot(x, E_hh, 'b-')
for yfrac in numpy.linspace(0, 1, 10):
    for i, xfrac in zip(indices, fractions):
        instance = quaternary(x=xfrac, y=yfrac)
        x[i] = instance.a(T=T)
        eps_xx = quaternary.biaxial_strained_eps_xx(x=xfrac, y=yfrac,
                                                    a0=GaSb.a(), T=T)
        if eps_xx < -0.03 or eps_xx > 0:
            E_c[i] = numpy.nan
            E_hh[i] = numpy.nan
        else:
            E_c[i] = quaternary.biaxial_strained_E_c(x=xfrac, y=yfrac,
                                                     a0=GaSb.a(), T=T)
            E_hh[i] = quaternary.biaxial_strained_E_hh(x=xfrac, y=yfrac,
                                                       a0=GaSb.a(), T=T)
    ax.plot(x, E_c, 'r--')
    ax.plot(x, E_hh, 'b--')

xmin, xmax = plt.xlim()
plt.xlim(xmin - 0.05, xmax)
plt.legend(loc='best')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        plt.savefig(output_filename)
    else:
        plt.show()