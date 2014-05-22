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

T = 300

# initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('Lattice Parameter at %g K ($\AA$)' % T)
plt.ylabel('Bandgap at %g K (eV)' % T)

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
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va='bottom',
                bbox=dict(linewidth=0, fc='white', alpha=0.9),
                textcoords='offset points')

# plot the strained binaries
first = True
for binary in [AlP, GaP, InP,
          AlAs, GaAs, InAs,
          AlSb, GaSb, InSb]:
    Eg = binary.Eg(T=T)
    a_0 = binary.a(T=T)
    c_12 = binary.c_12()
    c_11 = binary.c_11()
    a_c = binary.a_c()
    a_v = binary.a_v()
    b = binary.b()
    x = []
    y_c = []
    y_lh = []
    y_hh = []
    # Plot from -2% to +2% strain
    for eps_xx in numpy.linspace(-0.02, 0.02, 100):
        # The strain can be defined in either of the two following
        # ways. The first seems more appropriate to me, at least in
        # this instance.
        # 1. relative to a_0 [ eps = ( a0 - ax ) / a0 ]:
        a_strained = a_0 * (1 - eps_xx)
        # 2. relative to a_strianed [ eps = ( a0 - ax ) / ax ]:
        # a_strained = a_0 / ( eps_xx + 1 )
        # Note: I'm implicitly assuming growth is on the (100) surface.
        # Growth on other surfaces will have different strain effects.
        # This is approach is probably also not directly applicable to
        # ternaries or quaternaries near transitions to indirect gap,
        # since the various conduction band valleys react differently
        # to strain.
        eps_zz = -2. * c_12 / c_11 * eps_xx
        dE_c = a_c * (2 * eps_xx + eps_zz)
        P_eps = -a_v * (2 * eps_xx + eps_zz)
        Q_eps = -b / 2 * (2 * eps_xx - 2 * eps_zz)
        dE_hh = -P_eps - Q_eps
        dE_lh = -P_eps + Q_eps
        E_c = Eg + dE_c
        E_c_hh = Eg + dE_c - dE_hh
        E_c_lh = Eg + dE_c - dE_lh
        Eg_strained = min(E_c_hh, E_c_lh)
        x.append(a_strained)
        y_c.append(E_c)
        y_lh.append(E_c_lh)
        y_hh.append(E_c_hh)
    if first:
        plt.plot(x, y_c, 'b--', label='Hydrostatic')
        plt.plot(x, y_lh, 'r-', label='Biaxial HH')
        plt.plot(x, y_hh, 'g-', label='Biaxial LH')
        first = False
    else:
        plt.plot(x, y_c, 'b--')
        plt.plot(x, y_lh, 'r-')
        plt.plot(x, y_hh, 'g-')
    # TODO: check that this isn't BS

plt.legend(loc='best')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        plt.savefig(output_filename)
    else:
        plt.show()