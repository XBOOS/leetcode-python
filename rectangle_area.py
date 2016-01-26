#!/usr/bin/env python
# encoding: utf-8

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int."""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        xs = [A,C,E,G]
        xs.sort()
        ys = [B,D,F,H]
        ys.sort()
        if (E<=A<=G or A<=E<=C) and (F<=B<=H or B<=F<=D):
            return abs(A-C)*abs(B-D)+abs(E-G)*abs(F-H)-abs(xs[1]-xs[2])*abs(ys[1]-ys[2])
        else:
            return abs(A-C)*abs(B-D)+abs(E-G)*abs(F-H)

