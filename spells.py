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

    def __init(self)__:

        self.x = np.linspace(0, 1)
        self.y = [
            np.cos(self.x * 1) + 2,
            np.cos(self.x * 2) + 3,
            np.cos(self.x * 3) + 4,
        ]


