iiis = ['Al', 'Ga', 'In']
vs = ['N', 'P', 'As', 'Sb']

print '''
# Type 1: AB_{x}C_{y}D_{1-x-y}
# binaryies = (AB, AC, AD)
# ternaries = (ABC, ABD ,ACD)'''
for iii in iiis:
    for i in xrange(len(vs)):
        for j in xrange(i + 1, len(vs)):
            for k in xrange(j + 1, len(vs)):
                print '''
class {A}{B}{C}{D}(Quaternary1):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{B}, {A}{C}, {A}{D})
    ternaries = ({A}{B}{C}, {A}{B}{D}, {A}{C}{D})
'''.format(A=iii, B=vs[i], C=vs[j], D=vs[k])

print '''
# Type 2: A_{x}B_{y}C_{1-x-y}D
# binaries = (AD, BD, CD)
# ternaries = (ABD, ACD, BCD)'''
for v in vs:
    for i in xrange(len(iiis)):
        for j in xrange(i + 1, len(iiis)):
            for k in xrange(j + 1, len(iiis)):
                print '''
class {A}{B}{C}{D}(Quaternary2):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{D}, {B}{D}, {C}{D})
    ternaries = ({A}{B}{D}, {A}{C}{D}, {B}{C}{D})
'''.format(A=iiis[i], B=iiis[j], C=iiis[k], D=v)

print '''
# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# binaries = (AC, AD, BC, BD)
# ternaries = (ABC, ABD, ACD, BCD)'''
for i in xrange(len(iiis)):
    for j in xrange(i + 1, len(iiis)):
        for k in xrange(len(vs)):
            for l in xrange(k + 1, len(vs)):
                print '''
class {A}{B}{C}{D}(Quaternary3):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{C}, {A}{D}, {B}{C}, {B}{D})
    ternaries = ({A}{B}{C}, {A}{B}{D}, {A}{C}{D}, {B}{C}{D})
'''.format(A=iiis[i], B=iiis[j], C=vs[k], D=vs[l])
