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
#    "spells.py"
#
#    This is the data structure to store the information of density of
#    states and band structure dispersion, also provide the method for
#    reading data files and rendering plot
#

import numpy as np

class Spells(object):

    def __init__(self):

        self.x = np.linspace(0, 1)
        self.y = [
            np.cos(self.x * 1) + 2,
            np.cos(self.x * 2) + 3,
            np.cos(self.x * 3) + 4,
        ]

    def __str__(self):

        tmpstr = (
            'Data Infomation:\n'
            + 'X min, X max             = %6.3f, %6.3f\n' % (
                min(self.x), max(self.x)
            )
            + 'Y min, Y max             = %6.3f, %6.3\n'  % (
                min(min(x) for x in self.y),
                max(max(x) for x in self.y)
            )
            + 'Number of data points    = %i\n' % len(self.x)
            + 'Number of Y lines        = %i\n' % len(self.y)
        )
 
        return tmpstr

