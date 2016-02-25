#!/usr/bin/env python
# encoding: utf-8

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

""" Be careful that it is non-duplicates"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        startWith = 1
        comb = []
        combs = []
        self.genComb(k,n,startWith,comb,combs)
        return combs

    def genComb(self,k,n,startWith,comb,combs):
        if n==0 and k==0:
            combs.append(comb[:])
            return
        if k==0 or n<0:
            return
        for i in range(startWith,10):
            comb.append(i)
            self.genComb(k-1,n-i,i+1,comb,combs)
            comb.pop()
