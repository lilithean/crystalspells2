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
#    "crystal.py"
#
#    This is the data structure to store the information of a
#    crystal, also methods for structure manipulation and
#    structural properties calculation are provided.

_BOHR_TO_ANGSTR = 0.5291772108

import numpy as np
#import os
#import re
import sys
from scipy.spatial import distance

class Crystal(object):
    """ The data structure """

    def __init__(self):
        self.lattice = np.array(
            [
                [1.85, 1.85, 0.00],
                [0.00, 1.85, 1.85],
                [1.85, 0.00, 1.85]
            ]
        )
        self.ions = [
            ['D', np.array([0.00, 0.00, 0.00])],
            ['E', np.array([0.50, 0.00, 0.00])],
            ['M', np.array([0.00, 0.50, 0.00])],
            ['O', np.array([0.00, 0.00, 0.50])],
        ]

    def __str__(self):
        tmpstr = (
            'Crystal Information\n'
            + '\033[91mLattice vector      =\033[00m\n'
            + '\n'.join(
                (
                    '\033[91m    %8.3f %8.3f %8.3f\033[00m' % (
                        x[0], x[1], x[2]
                    )
                    for x in self.lattice
                )
            )
            +'\n'
            + 'a, b, c             = %8.3f %8.3f %8.3f\n' % (
	        np.linalg.norm(self.lattice[0]),
                np.linalg.norm(self.lattice[1]),
                np.linalg.norm(self.lattice[2])
            )
            + 'alpha, beta, gamma  = %8.3f %8.3f %8.3f\n' % (
                1 - distance.cosine(self.lattice[0], self.lattice[2]),
                1 - distance.cosine(self.lattice[1], self.lattice[2]),
                1 - distance.cosine(self.lattice[0], self.lattice[1])
            )
            + 'volume              = %8.3f\n' % (
                np.dot(
                    self.lattice[0],
                    np.cross(self.lattice[1], self.lattice[2])
                )
            )
            + '\033[94mIons                =\033[00m\n'
            + '\n'.join(
                '\033[94m    %4s %8.3f %8.3f %8.3f\033[00m' % (
                    x[0], x[1][0], x[1][1], x[1][2]
                )
                for x in self.ions
            )
            +'\n'
            + '\033[92mReciprocal lattice  =\033[00m '
            + '\033[92m(in units 2pi/angstr)\033[00m\n'
            + '\n'.join(
                (
                    '\033[92m    %8.3f %8.3f %8.3f\033[00m' % (
                        x[0], x[1], x[2]
                    )
                    for x in self.reciprocal()
                )
            )
        )
        return tmpstr

    def reciprocal(self, conv='vasp', frac=[], cart=[]):
        """ b1 = (a2 x a3)/(a1 (a2 x a3)),
            frac: numpy.array; return cart or
            cart: numpy.array; return frac """

        conv = conv.lower()

        reciprocal_lattice = np.transpose(
            np.linalg.inv(self.lattice)
        )

        if conv in ('qe', 'eqpresso'):
            reciprocal_lattice = (
                reciprocal_lattice
                * np.linalg.norm(self.lattice[0])
            )

        if len(frac):
            return np.dot(frac, reciprocal_lattice)
        elif len(cart):
            return np.dot(cart, np.linalg.inv(reciprocal_lattice))
        else:
            return reciprocal_lattice

    def to(self, style='vasp'):
        """ output a string of given input file """

        style = style.lower()

        elements = [x[0] for x in self.ions]
        #     funny fact: list comprehension is the fastest way
        # see https://stackoverflow.com/a/48157038

        elements_count = zip(
            *sorted(
                [
                    [x, elements.count(x)]
                    for x in set(elements)
                ],
                key = lambda y: y[0]
            )
        )
        #     the built-in set function returns an unordered set

        if style in ('vasp', 'poscar', 'contcar'):
            tmpstr = (
                'VASP5 Format POSCAR File\n'
                + '  1.000\n'
                + '\n'.join(
                    '  %14.10f  %14.10f  %14.10f' % (x[0], x[1], x[2])
                    for x in self.lattice
                )
                + '\n'
                + '  '.join('%3s' % x for x in elements_count[0])
                + '\n  '
                + '  '.join('%3i' % x for x in elements_count[1])
                + '\nDirect\n'
                + '\n'.join(
                    '  %14.10f  %14.10f  %14.10f' % (
                        x[1][0], x[1][1], x[1][2]
                    )
                    for x in self.ions
                )
            )

        elif style in ('dftb+', 'dftbplus'):
            tmpstr = (
                'Geometry = {\n'
                + '  TypeNames = {'
                + ' '.join('"%s"' % x for x in elements_count[0])
                + '}\n'
                + '  TypesAndCoordinates [relative] = {\n'
                + '\n'.join(
                    '    %i %9.6f %9.6f %9.6f' % (
                        elements_count[0].index(x[0]) + 1,
                        x[1][0], x[1][1], x[1][2]
                    )
                    for x in self.ions
                )
                + '\n  }\n'
                + '  Periodic = Yes\n'
                + '  LatticeVectors [Angstrom] = {\n'
                + '\n'.join(
                    '    %9.6f  %9.6f  %9.6f' % (
                        x[0], x[1], x[2]
                    )
                    for x in self.lattice
                )
                + '\n  }\n}'
            )

        elif style in ('adf', 'ams'):
            tmpstr = (
                'System\n'
                + '    FractionalCoords True\n'
                + '    Atoms\n'
                + '\n'.join(
                    '        %s  %14.9f  %14.9f  %14.9f' % (
                        x[0], x[1][0], x[1][1], x[1][2]
                    )
                    for x in self.ions
                )
                + '\n    End\n'
                + '    Lattice [Angstrom]\n'
                + '\n'.join(
                    '    %14.9f  %14.9f  %14.9f' % (
                        x[0], x[1], x[2]
                    )
                    for x in self.lattice
                )
                + '\n    End\n'
                +'End'
            )

        elif style in ('qe', 'espresso'):
            tmpstr = (
                'CELL_PARAMETERS (angstrom)\n'
                + '\n'.join(
                    '  %14.9f  %14.9f  %14.9f' % (
                        x[0], x[1], x[2]
                    )
                    for x in self.lattice
                )
                + '\n'
                + 'ATOMIC_POSITIONS (crystal)\n'
                + '\n'.join(
                    '  %s  %14.9f  %14.9f  %14.9f' % (
                        x[0], x[1][0], x[1][1], x[1][2]
                    )
                    for x in self.ions
                )
            )

        else:
            tmpstr = False

        return tmpstr


def from_file(fpath, ftype='vasp'):
    """ Read crystal data from output file and return a Crystal """

    try:
        with open(fpath, 'r') as fid:
            tmpdata = fid.readlines()
    except OSError:
        print("Error opening structure file")
        sys.exit(-1) # will be replaced by error handler

    ftype = ftype.lower()
    crystal = Crystal()

    if ftype in ('vasp', 'poscar', 'contcar'):
        scale = float(tmpdata[1])
        crystal.lattice = np.array(
            [
                [float(x)*scale for x in y.split()]
                for y in tmpdata[2:5]
            ]
        )

        try:
            nion = [int(x) for x in tmpdata[5].split()]
        except ValueError:
            nion = [int(x) for x in tmpdata[6].split()]
            elements = sum(
                [[x]*y for x, y in zip(tmpdata[5].split(), nion)],
                list()
            )
        else:
            element = ['Xx'] * sum(nion)

        for i in range(6, 9):
            if tmpdata[i][0].lower() in ['k', 'c']:
                cartesian = True
                break
            elif tmpdata[i][0].lower() == 'd':
                cartesian = False
                break
        else:
            print("Error reading POSCAR file")
            sys.exit(-1)

        if cartesian:
            crystal.ions = zip(
                elements,
                [
                    np.matmul(
                        np.array([float(x)*scale for x in y.split()]),
                        np.linalg.inv(crystal.lattice)
                    )
                    for y in tmpdata[i+1:i+sum(nion)+1]
                ]
            )
        else:
            crystal.ions = zip(
                elements, [
                    np.array([float(x) for x in y.split()])
                    for y in tmpdata[i+1:i+sum(nion)+1]
                ]
            )

    if ftype in ('qe', 'espresso'):
        """ this one reads only qe output file """
        scale = float(
            next(x for x in tmpdata if 'celldm' in x).split()[1]
        ) * _BOHR_TO_ANGSTR
        crystal.lattice = np.array(
            [
                [float(x)*scale for x in y.split()[3:6]]
                for y in tmpdata if 'a(' in y
            ]
        )
        try:
            crystal.ions = [
                [
                    v.split()[1],
                    np.matmul(
                        np.array([float(x)*scale for x in v.split()[6:9]]),
                        np.linalg.inv(crystal.lattice)
                    )
                ]
                for v in tmpdata if 'tau' in v
            ]
        except ValueError:
            crystal.ions = [
                [
                    v.split()[1],
                    np.matmul(
                        np.array([float(x)*scale for x in v.split()[7:10]]),
                        np.linalg.inv(crystal.lattice)
                    )
                ]
                for v in tmpdata if 'tau' in v
            ]

    if ftype in ('dftb+', 'dftbplus', 'gen'):
        nion = int(tmpdata[0].split()[0])
        elements = tmpdata[1].split()
        crystal.ions = [
            [
                elements[int(w)-1],
                np.array([float(x), float(y), float(z)])
            ]
            for w, x, y, z in (
                v.split()[1:] for v in tmpdata[2:2+nion]
            )
        ]
        crystal.lattice = np.array(
            [
                [float(x) for x in y.split()]
                for y in tmpdata[2+nion+1:2+nion+4]
            ]
        )

    if ftype in ('lmto', 'tb-lmto-asa'):
        istruc = next(
            x for x, y in enumerate(tmpdata) if 'STRUC' in y
        )
        alat = (
            float(tmpdata[istruc].split('=')[-1]) 
            * _BOHR_TO_ANGSTR
        )
        try:
            crystal.lattice = np.array(
                [
                    [float(x)*alat for x in y[15:48].split()]
                    for y in tmpdata[istruc+1:istruc+4]
                ]
            )
        except ValueError:
            print "Only accept CTRL file generated by lmctl.run"
            sys.exit(-1)
        crystal.ions = [
            [
                w.strip('0123456789'), 
                np.matmul(
                    np.array([float(x), float(y), float(z)]),
                    np.linalg.inv(crystal.lattice) * alat
                )
            ]
            for w, x, y, z in (
                v.replace(
                    'ATOM=', ''
                ).replace(
                    'POS=',''
                ).replace(
                    'SITE', ''
                ).split()
                for v in tmpdata if 'POS' in v
            )
        ]

    crystal.ions.sort(key = lambda x: x[0])
    #     the ions are sorted by the elemental names, which allows
    # us access to many hashable/unsorted methods

    return crystal

