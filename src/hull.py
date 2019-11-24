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
#    "ensemble.py"
#
#    This is the datastructure to store and manipulate a collection
#    of crystals and their properties
#


import numpy as np
import os
import sys
sys.path.append(
    '/home/xwang224/crystalspells2/src'
)
sys.path.append(
    '/projects/academic/ezurek/xiaoyu/crystalspells2/src'
)
from crystal import from_file

class Hull(object):

    def __init__(self):
        # [elements, nref, eV/FU]
        self.reference = [
            ['F', 2.,  35.44],
            ['Y', 1., 121.31],
            ['I', 3., 241.60],
        ]
        # [x, y, eV/atom]
        self.hulldata = np.array(
            [
                [0.100, 0.333, 128.63],
                [0.250, 0.666,  32.51],
                [0.750, 0.375,  30.66],
            ]  
        )

    def position(self, data):
        # data = [n1, n2, n3]
        ratio = 

        return

    def formation_enthalpy(self, data):
        # data = [n1, n2, n3, eV/FU]
        # reaction = n1/nref1 A_nref1 
        #          + n2/nref2 B_nref2 
        #          + n3/nref3 C_nref3
        #          -> A_n1 B_n2 C_n3
        # formation_enthalpy = [H 
        #                    - (n1/nref1)*H1
        #                    - (n2/nref2)*H2
        #                    - (n3/nref3)*H3
        #                    ] / (n1 + n2 + n3)
        # in eV/atom    
        return (
            data[3]
            - self.reference[0][1]/data[0] * self.reference[0][2]
            - self.reference[1][1]/data[1] * self.reference[1][2]
            - self.reference[2][1]/data[2] * self.reference[2][2]
        )/(data[0] + data[1] + data[2])

def from_directory(dpath):

    collection = Ensemble()

    subdirs = filter(
        lambda x: os.path.isdir(os.path.join(dpath, x)),
        os.listdir(dpath)
    )

    for i in subdirs:
        try:
            crystal = from_file(i+'/CONTCAR', 'vasp')
        except:
            print 'Error reading structure in folder %s' %i
        else:
            try:
                with open(i+'/OUTCAR', 'r') as fid:
                    tmpdata = fid.readlines()
                enthalpy = float(
                    next(
                        x for x in reversed(tmpdata) if 'TOTEN' in x
                    ).split()[4]
                )
            except:
                    print 'Error reading enthalpy in folder %s' %i
            else:
                collection.ensemble.append([crystal, enthalpy])

    return collection

