#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import numpy

from topopt.boundary_conditions import TopOptBoundaryConditions
from topopt.utils import xy_to_id

from topopt import cmd_helper


class Exercise02_1BoundaryConditions(TopOptBoundaryConditions):
    @property
    def fixed_nodes(self):
        """Return a list of fixed nodes for the problem."""
        bottom_left = 2 * xy_to_id(0, self.nely, self.nelx, self.nely)
        bottom_right = 2 * xy_to_id(self.nelx, self.nely, self.nelx, self.nely)
        fixed = numpy.array(
            [bottom_left, bottom_left + 1, bottom_right, bottom_right + 1])
        return fixed

    @property
    def forces(self):
        """Return the force vector for the problem."""
        f = numpy.zeros((2 * (self.nelx + 1) * (self.nely + 1), 1))
        id1 = 2 * xy_to_id(7 * self.nelx // 20, 0, self.nelx, self.nely) + 1
        id2 = 2 * xy_to_id(13 * self.nelx // 20, 0, self.nelx, self.nely) + 1
        f[[id1, id2], 0] = -1
        return f


def main():
    # Default input parameters
    nelx, nely, volfrac, penal, rmin, ft = cmd_helper.parse_sys_args(
        nelx=120, volfrac=0.2, rmin=1.5)
    cmd_helper.main(nelx, nely, volfrac, penal, rmin, ft,
                    bc=Exercise02_1BoundaryConditions(nelx, nely))


if __name__ == "__main__":
    main()
