#!/usr/bin/env python
# encoding: utf-8

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

"""
""" The method is to do 2 reflactions, on along x-axis, one along diagonal axis"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n):
                matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j],matrix[i][j]

        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]




