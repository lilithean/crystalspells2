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
#    "dftbp2v.py"
#
#    Convert dftbplus output into vasp files for XtalOpt use


import sys
sys.path.append(
    '/projects/academic/ezurek/xiaoyu/crystalspells2/src'
)
from crystal import *

from_file('geom.out.gen', 'dftb+').to('vasp')

with open('detailed.out', 'r') as fid:
    tmpdata = fid.readlines()

energy = float(
    next(x for x in tmpdata if 'Extrapolated to 0' in x).split()[5]
)

with open('OUTCAR', 'w') as fid:
    fid.write('free  energy   TOTEN  =      %13.8f eV' % energy)
