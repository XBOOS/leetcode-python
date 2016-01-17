#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        weight = 0
        while not n==0:
            if n%2 == 1:
                weight +=1
            n = n/2
        return weight
