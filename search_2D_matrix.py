#!/usr/bin/env python
# encoding: utf-8

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

"""  Method 1: Recursion.
    modify the binary search method for array to do the binary search for a matrix,be careful of the ending condition, start>=end"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        return self.matrixBinarySearch(0,m*n-1,matrix,n,target)

    def matrixBinarySearch(self,start,end,matrix,n,target):
        if start>=end and matrix[start/n][start%n]!=target:
            return False
        mid = (start+end)/2
        x = mid/n
        y = mid%n
        if matrix[x][y]==target:
            return True
        elif matrix[x][y]>target:
            return self.matrixBinarySearch(start,mid-1,matrix,n,target)
        else:
            return self.matrixBinarySearch(mid+1,end,matrix,n,target)




    def binarySearch(self,start,end,arr,target):
        if start==end and arr[start]!=target:
            return False
        mid = (start+end)/2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            return self.binarySearch(start,mid-1,arr,target)
        else:
            return self.binarySearch(mid+1,end,arr,target)



""" Method 2  Iterative method"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n-1
        mid = x = y = 0
        while start<end:
            mid = (start+end)/2
            x = mid/n
            y = mid%n
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                end = mid-1
            else:
                start = mid+1
        return matrix[start/n][start%n]==target
