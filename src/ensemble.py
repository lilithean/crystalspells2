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

class Ensemble(object):

    def __init__(self):
        """
            Each entry in Ensemble is, currently:
            [
                crystal,
                enthalpy,
            ]

        """

        self.ensemble = []

    def convex_hull(self, reference=None):

        elements = list(
            set().union(
                x[0].elements()[0] for x in self.ensemble
            )
        )
        return elements



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

