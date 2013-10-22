from openbandparams.iii_v.zinc_blende.binary import *

# Print a hardcoded parameter (API subject to change)
print 'InAs electron effective mass in Gamma-valley:  %.3f eV'%InAs._meff_e_Gamma
print ''

# Print an unformatted temperature dependent parameters
print 'GaAs bandgap (at T = 300 K): ', GaAs.Eg(), 'eV'
print ''

# Print some formatted temperature dependent parameters
print 'GaAs bandgap (at T = 300 K):  %.3f eV'%GaAs.Eg()
print 'GaAs Gamma-valley gap (at T = 300 K):  %.3f eV'%GaAs.Eg_Gamma()
print 'GaAs X-valley gap (at T = 300 K):  %.3f eV'%GaAs.Eg_X()
print 'GaAs bandgap (at T = 0 K):  %.3f eV'%GaAs.Eg(T=0)
print 'InAs bandgap (at T = 300 K):  %.3f eV'%InAs.Eg()
print ''

# Print a table of material lattice parameters and bandgaps
import string
print ' Material | Lattice Param. [Ang] | Bandgap [eV]'
print '------------------------------------------------'
for mat in binaries:
    print string.rjust(mat.name, 7),
    print '  | ', string.rjust('%.3f'%mat.a(), 12), ' '*4,
    print '  |    %.3f'%mat.Eg()