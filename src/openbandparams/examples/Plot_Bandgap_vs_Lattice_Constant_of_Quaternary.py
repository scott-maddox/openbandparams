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

import matplotlib.pyplot as plt
import numpy
from openbandparams import *

quaternary = GaInPAs
T = 300

# initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('Lattice Parameter at %g K ($\AA$)' % T)
plt.ylabel('Bandgap at %g K (eV)' % T)

# plot the binaries
xs = []
y_Gamma = []
y_X = []
y_L = []
labels = []
for b in quaternary.binaries:
    xs.append(b.a(T=T))
    y_Gamma.append(b.Eg_Gamma(T=T))
    y_X.append(b.Eg_X(T=T))
    y_L.append(b.Eg_L(T=T))
    labels.append(b.name)
ax.plot(xs, y_Gamma, 'r.')
ax.plot(xs, y_X, 'b.')
ax.plot(xs, y_L, 'g.')

# label the binaries
for x, y, label in zip(xs, y_Gamma, labels):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')
for x, y, label in zip(xs, y_X, labels):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')
for x, y, label in zip(xs, y_L, labels):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')

# plot the quaternary
indices = numpy.arange(100)
fractions = numpy.linspace(0, 1, 100)
x = numpy.empty(100, dtype=numpy.float)
y_Gamma = numpy.empty(100, dtype=numpy.float)
y_X = numpy.empty(100, dtype=numpy.float)
y_L = numpy.empty(100, dtype=numpy.float)
first = True
for xfrac in numpy.linspace(0, 1, 10):
    for i, yfrac in zip(indices, fractions):
        instance = quaternary(x=xfrac, y=yfrac)
        x[i] = instance.a(T=T)
        y_Gamma[i] = instance.Eg_Gamma(T=T)
        y_X[i] = instance.Eg_X(T=T)
        y_L[i] = instance.Eg_L(T=T)
    if first:
        ax.plot(x, y_Gamma, 'r-', label='$\Gamma$')
        ax.plot(x, y_X, 'b-', label='$X$')
        ax.plot(x, y_L, 'g-', label='$L$')
        first = False
    else:
        ax.plot(x, y_Gamma, 'r-')
        ax.plot(x, y_X, 'b-')
        ax.plot(x, y_L, 'g-')
for yfrac in numpy.linspace(0, 1, 10):
    for i, xfrac in zip(indices, fractions):
        instance = quaternary(x=xfrac, y=yfrac)
        x[i] = instance.a(T=T)
        y_Gamma[i] = instance.Eg_Gamma(T=T)
        y_X[i] = instance.Eg_X(T=T)
        y_L[i] = instance.Eg_L(T=T)
    ax.plot(x, y_Gamma, 'r--')
    ax.plot(x, y_X, 'b--')
    ax.plot(x, y_L, 'g--')

plt.legend(loc='best')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        plt.savefig(output_filename)
    else:
        plt.show()