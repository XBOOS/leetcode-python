#!/usr/bin/env python
# encoding: utf-8

"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4."""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # similar to find the largest power of 2 which is less and equal to n
        k=31
        while k>0 and not (m&(1<<k)) ^ (n&(1<<k)):
            k-=1
        mask = 0
        while k<=31:
            mask |=(1<<k)
            k+=1
        return m&mask



class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p
