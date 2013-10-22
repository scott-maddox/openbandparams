import matplotlib.pyplot as plt
import numpy
from openbandparams.iii_v.zinc_blende.ternary import AlGaAs as alloy

# calculate the data
xs = numpy.linspace(0, 1, 100)
T = 0 #K
gamma = [alloy(x).Eg_Gamma(T) for x in xs]
X = [alloy(x).Eg_X(T) for x in xs]
L = [alloy(x).Eg_L(T) for x in xs]

# plot it
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('%s (T = %.2g K)'%(alloy.name, T))
plt.xlabel('%s fraction'%alloy.element1)
plt.ylabel('Bandgap (eV)')
ax.plot(xs, gamma, 'k-', label='$\Gamma$')
ax.plot(xs, X, 'k--', label='$X$')
ax.plot(xs, L, 'k:', label='$L$')
plt.legend(loc='best')
plt.show()