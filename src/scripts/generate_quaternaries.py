iiis = ['Al', 'Ga', 'In']
vs = ['N', 'P', 'As', 'Sb']

print '''
# Type 1: AB_{x}C_{y}D_{1-x-y}
# binary1 = AB
# binary2 = AC
# binary3 = AD
# ternary1 = ABC
# ternary2 = ABD
# ternary3 = ACD'''
for iii in iiis:
    for i in xrange(len(vs)):
        for j in xrange(i+1, len(vs)):
            for k in xrange(j+1, len(vs)):
                print '''
class {A}{B}{C}{D}(Quaternary1):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{B}, {A}{C}, {A}{D})
    ternaries = ({A}{B}{C}, {A}{B}{D}, {A}{C}{D})
    element1 = '{A}'
    element2 = '{B}'
    element3 = '{C}'
    element4 = '{D}'
    binary1 = {A}{B}
    binary2 = {A}{C}
    binary3 = {A}{D}
    ternary1 = {A}{B}{C}
    ternary2 = {A}{B}{D}
    ternary3 = {A}{C}{D}'''.format(A=iii, B=vs[i], C=vs[j], D=vs[k])

print '''
# Type 2: A_{x}B_{y}C_{1-x-y}D
# binary1 = AD
# binary2 = BD
# binary3 = CD
# ternary1 = ABD
# ternary2 = ACD
# ternary3 = BCD'''
for v in vs:
    for i in xrange(len(iiis)):
        for j in xrange(i+1, len(iiis)):
            for k in xrange(j+1, len(iiis)):
                print '''
class {A}{B}{C}{D}(Quaternary2):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{D}, {B}{D}, {C}{D})
    ternaries = ({A}{B}{D}, {A}{C}{D}, {B}{C}{D})
    element1 = '{A}'
    element2 = '{B}'
    element3 = '{C}'
    element4 = '{D}'
    binary1 = {A}{D}
    binary2 = {B}{D}
    binary3 = {C}{D}
    ternary1 = {A}{B}{D}
    ternary2 = {A}{C}{D}
    ternary3 = {B}{C}{D}'''.format(A=iiis[i], B=iiis[j], C=iiis[k], D=v)

print '''
# Type 3: A_{x}B_{1-x}C_{y}D_{1-y}
# binary1 = AC
# binary2 = AD
# binary3 = BC
# binary4 = BD
# ternary1 = ABC
# ternary2 = ABD
# ternary3 = ACD
# ternary4 = BCD'''
for i in xrange(len(iiis)):
    for j in xrange(i+1, len(iiis)):
        for k in xrange(len(vs)):
            for l in xrange(k+1, len(vs)):
                print '''
class {A}{B}{C}{D}(Quaternary3):
    name = '{A}{B}{C}{D}'
    elements = ('{A}', '{B}', '{C}', '{D}')
    binaries = ({A}{C}, {A}{D}, {B}{C}, {B}{D})
    ternaries = ({A}{B}{C}, {A}{B}{D}, {A}{C}{D}, {B}{C}{D})
    element1 = '{A}'
    element2 = '{B}'
    element3 = '{C}'
    element4 = '{D}'
    binary1 = {A}{C}
    binary2 = {A}{D}
    binary3 = {B}{C}
    binary4 = {B}{D}
    ternary1 = {A}{B}{C}
    ternary2 = {A}{B}{D}
    ternary3 = {A}{C}{D}
    ternary4 = {B}{C}{D}'''.format(A=iiis[i], B=iiis[j], C=vs[k], D=vs[l])