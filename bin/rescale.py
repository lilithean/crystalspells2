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
#    "icryst.py"
#
#    A quick tool to check crystal information

import sys
sys.path.append(
    '/home/xwang224/crystalspells2/src'
)
sys.path.append(
    '/projects/academic/ezurek/xiaoyu/crystalspells2/src'
)
from crystal import from_file

crystal = from_file(sys.argv[1], 'vasp')

print crystal
print crystal.rescale(25.729705037425987)

print crystal.rescale(25.729705037425987).to('vasp')
