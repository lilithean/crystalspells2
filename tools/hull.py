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
#    "hull.py"
#
#    This is the function to calculate convexhull for a set of
#    crystals and energies
#

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append(
    '/home/xwang224/crystalspells2/src'
)
sys.path.append(
    '/projects/academic/ezurek/xiaoyu/crystalspells2/src'
)
from crystal import from_file
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
from matplotlib.animation import FuncAnimation

def update(i):
    points = np.random.rand(100, 3)
    hull = ConvexHull(points)
    ax.plot(points.T[0], points.T[1], points.T[2], "ko")
    for s in hull.simplices:
        s = np.append(s, s[0])
        ax.plot(points[s, 0], points[s, 1], points[s, 2], "b:")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
for i in ["x", "y", "z"]:
    eval("ax.set_{:s}label('{:s}')".format(i, i))

animation = FuncAnimation(fig, update, interval=50, blit=True)

plt.show()
