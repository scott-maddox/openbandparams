import matplotlib.pyplot as plt
import numpy

T = 300

# initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('Lattice Parameter at %g K ($\AA$)'%T)
plt.ylabel('Bandgap at %g K (eV)'%T)

# plot the binaries
from openbandparams.iii_v.zinc_blende.binary import *
x = []
y = []
label = []
for b in [AlP, GaP, InP,
          AlAs, GaAs, InAs,
          AlSb, GaSb, InSb]:
    x.append(b.a(T))
    y.append(b.Eg(T))
    label.append(b.name)
ax.plot(x, y, 'k.')

# label the binaries
for x, y, label in zip(x, y, label):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), ha='right', va = 'bottom',
                bbox = dict(linewidth=0, fc = 'white', alpha = 0.9),
                textcoords='offset points')

# plot the ternaries
from openbandparams.iii_v.zinc_blende.ternary import *
indices = numpy.arange(100)
fractions = numpy.linspace(0, 1, 100)
x = numpy.empty(100, dtype=numpy.float)
y = numpy.empty(100, dtype=numpy.float)
for tern in [AlGaP,  AlInP,  GaInP,
             AlGaAs, AlInAs, GaInAs,
             AlGaSb, AlInSb, GaInSb,
             AlPAs,  GaPAs,  InPAs,
             AlPSb,  GaPSb,  InPSb,
             AlAsSb, GaAsSb, InAsSb]:
    for i, f in zip(indices, fractions):
        instance = tern(f)
        x[i] = instance.a(T)
        y[i] = instance.Eg(T)
    ax.plot(x, y)

plt.show()