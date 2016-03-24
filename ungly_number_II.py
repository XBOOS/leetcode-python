#!/usr/bin/env python
# encoding: utf-8

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5)."""


""" My original mistake is that use if-else to update the ptr.which results in duplicates in the result list.
should all update the ptr if nextMin==min_pow"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        ptr2 = ptr3 = ptr5=0

        while len(dp)<n:
            min_pow2 = dp[ptr2]*2
            min_pow3 = dp[ptr3]*3
            min_pow5 = dp[ptr5]*5
            nextMin = min(min_pow2,min_pow3,min_pow5)
            if nextMin==min_pow2:
                ptr2+=1
            if nextMin==min_pow3:
                ptr3+=1
            if nextMin ==min_pow5:
                ptr5+=1
            dp.append(nextMin)
        return dp[-1]

