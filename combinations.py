#!/usr/bin/env python
# encoding: utf-8

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]"""


""" Method1: backtracking!"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k>n:
            return []

        def combineFrom(combination,start,k):
            #if k<0 or n-start+1<k:
             #   return False
            if k==0:
                combinations.append(combination[:])
                return True
            for i in range(start,n-k+2):
                combination.append(i)
                combineFrom(combination,i+1,k-1)
                combination.pop()
        combinations = []
        combination = []
        combineFrom(combination,1,k)

        return combinations

