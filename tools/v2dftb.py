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
#    "v2dftb.py"
#
#    Convert vasp structure into dftbplus input file

import sys
sys.path.append(
    '/home/xwang224/crystalspells2/src'
)
from crystal import *

tmpstr = (
    from_file('POSCAR', 'vasp').to('dftb+')
    + '\n'
    + 'Driver = ConjugateGradient {\n'
    + '    LatticeOpt = Yes\n'
    + '    MovedAtoms = 1:-1\n'
    + '    MaxForceComponent = 1E-4\n'
    + '    MaxSteps = 1500\n'
    + '    OutputPrefix = "geom.out"\n'
    + '}\n'
    + 'Hamiltonian = DFTB {\n'
    + '    SCC = Yes\n'
    + '    SlaterKosterFiles = Type2FileNames {\n'
    + '        Prefix = "/home/xwang224/src/dftbplus/lib/tiorg-0-1/"\n'
    + '        Separator = "-"\n'
    + '        Suffix = ".skf"\n'
    + '        LowerCaseTypeName = No\n'
    + '    }\n'
    + '    MaxAngularMomentum {\n'
    + '        O = "p"\n'
    + '        Ti = "d"\n'
    + '    }\n'
    + '    Filling = Fermi {\n'
    + '        Temperature [Kelvin] = 300.0\n'
    + '    }\n'
    + '    KPointsAndWeights = SupercellFolding {\n'
    + '        2   0   0\n'
    + '        0   2   0\n'
    + '        0   0   2\n'
    + '        0.5 0.5 0.5\n'
    + '    }\n'
    + '}\n'
)


with open('dftb_in.hsd', 'w') as fid:
    fid.write(tmpstr)
