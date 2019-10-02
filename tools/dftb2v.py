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
    '/home/xwang224/crystalspells2/src'
)
from crystal import *

with open('CONTCAR', 'w') as fid:
    fid.write(from_file('geom.out.gen', 'dftb+').to('vasp'))
    fid.write('\n')

with open('detailed.out', 'r') as fid:
    tmpdata = fid.readlines()

if 'SCC is NOT converged, maximal SCC iterations exceeded' in tmpdata:
    print 'SCC unconverge'
    sys.exit(-1)

energy = float(
    next(x for x in tmpdata if 'Extrapolated to 0' in x).split()[5]
)

with open('OUTCAR', 'w') as fid:
    fid.write('    free  energy   TOTEN  =      %13.8f eV\n' % energy)
    fid.write('    General timing and accounting informations for this job:\n')
