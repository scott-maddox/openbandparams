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

import matplotlib.pyplot as plt
import numpy


T = 300

# initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('Strained Lattice Parameter at %g K ($\AA$)' % T)
plt.ylabel('Strained Bandgap at %g K (eV)' % T)

# plot the binaries
x = []
y = []
label = []
for b in [AlP, GaP, InP,
          AlAs, GaAs, InAs,
          AlSb, GaSb, InSb]:
    x.append(b.a(T=T))
    y.append(b.Eg(T=T))
    label.append(b.name)
ax.plot(x, y, 'k.')

# label the binaries
for x, y, label in zip(x, y, label):
    ax.annotate(label, xy=(x, y), xytext=(5, 5), ha='left', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')

# plot the strained binaries
first = True
eps_xx = numpy.linspace(-0.02, 0.02, 100)
for b in [AlP, GaP, InP,
          AlAs, GaAs, InAs,
          AlSb, GaSb, InSb]:
    a_strained = [b.biaxial_strained_a0(eps_xx=eps_xx_) for eps_xx_ in eps_xx]
    E_c_hh = [b.biaxial_strained_E_c_hh(eps_xx=eps_xx_) for eps_xx_ in eps_xx]
    E_c_lh = [b.biaxial_strained_E_c_lh(eps_xx=eps_xx_) for eps_xx_ in eps_xx]
    if first:
        plt.plot(a_strained, E_c_hh, 'r-', label='CB-HH gap')
        plt.plot(a_strained, E_c_lh, 'g-', label='CB-LH gap')
        first = False
    else:
        plt.plot(a_strained, E_c_hh, 'r-')
        plt.plot(a_strained, E_c_lh, 'g-')

plt.legend(loc='best')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        plt.savefig(output_filename)
    else:
        plt.show()