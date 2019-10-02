#!/usr/bin/env python
#
#    This file is part of <Crystal Spells Package>
#
#    Copyright Xiaoyu Wang (xwang224@buffalo.edu)
#
#    Department of Wizardary and Alchemical Engineering
#    State University of New York at Buffalo, U.S.A.
#
#    Fall 2019
#
#    "tcrystal.py"
#
#    Test functions in crystal.py


import sys
import numpy as np
sys.path.append(
    '/projects/academic/ezurek/xiaoyu/crystalspells2/src'
)
from crystal import *

print '- reading structure from qe output'
qe_cryst = from_file('scf.out', 'qe')
print qe_cryst
print

print '- output vasp format'
print qe_cryst.to('vasp')
print

print '- output qe format'
print qe_cryst.to('qe')
print

print '- output dftb+ format'
print qe_cryst.to('dftb+')
print

print '- output adf format'
print qe_cryst.to('adf')
print

print '- calculate reciprocal lattice (qe convention)'
print qe_cryst.reciprocal('qe')
print

print '- convert fractional kpoints to cartesian \
(qe convention in units 2pi/alat)'
frac = np.array(
    [
        [ 0.0000000,  0.0000000,  0.0000000], 
        [ 0.0000000,  0.0000000,  0.0625000], 
        [ 0.0000000,  0.0000000,  0.1250000], 
        [ 0.0000000,  0.0000000,  0.1875000], 
        [ 0.0000000,  0.0000000,  0.2500000], 
        [ 0.0000000,  0.0000000,  0.3125000], 
        [ 0.0000000,  0.0000000,  0.3750000], 
        [ 0.0000000,  0.0000000,  0.4375000], 
        [ 0.0000000,  0.0000000, -0.5000000], 
        [ 0.0000000,  0.0833333,  0.0000000], 
        [ 0.0000000,  0.0833333,  0.0625000], 
        [ 0.0000000,  0.0833333,  0.1250000], 
        [ 0.0000000,  0.0833333,  0.1875000], 
        [ 0.0000000,  0.0833333,  0.2500000], 
        [ 0.0000000,  0.0833333,  0.3125000], 
        [ 0.0000000,  0.0833333,  0.3750000], 
        [ 0.0000000,  0.0833333,  0.4375000], 
        [ 0.0000000,  0.0833333, -0.5000000], 
        [ 0.0000000,  0.1666667,  0.0000000], 
        [ 0.0000000,  0.1666667,  0.0625000], 
    ]
)
print qe_cryst.reciprocal('qe', frac=frac)
print

print '- convert fractional kpoints to cartesian \
(vasp convention in units 2pi/angstr)'
print qe_cryst.reciprocal('vasp', frac=frac)
print

print '- convert cartesian kpoints to fractional'
cart = np.array(
    [
        [ 0.         , 0.        ,  0.        ], 
        [ 0.         , 0.        ,  0.17535443],
        [ 0.         , 0.        ,  0.35070885],
        [ 0.         , 0.        ,  0.52606328],
        [ 0.         , 0.        ,  0.70141771],
        [ 0.         , 0.        ,  0.87677213],
        [ 0.         , 0.        ,  1.05212656],
        [ 0.         , 0.        ,  1.22748098],
        [ 0.         , 0.        , -1.40283541],
        [ 0.         , 0.14786996,  0.        ],
        [ 0.         , 0.14786996,  0.17535443],
        [ 0.         , 0.14786996,  0.35070885],
        [ 0.         , 0.14786996,  0.52606328],
        [ 0.         , 0.14786996,  0.70141771],
        [ 0.         , 0.14786996,  0.87677213],
        [ 0.         , 0.14786996,  1.05212656],
        [ 0.         , 0.14786996,  1.22748098],
        [ 0.         , 0.14786996, -1.40283541],
        [ 0.         , 0.2957401 ,  0.        ],
        [ 0.         , 0.2957401 ,  0.17535443],
    ]
)
print qe_cryst.reciprocal('qe', cart=cart)
print

print '- reading structure from lmto ctrl file'
lmto_cryst = from_file('CTRL', 'lmto')
print lmto_cryst
print

print '- reading structure from vasp poscar file'
vasp_cryst = from_file('POSCAR', 'vasp')
print vasp_cryst
print
