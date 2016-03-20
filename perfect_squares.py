#!/usr/bin/env python
# encoding: utf-8

"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9."""

""" ALways TLE at the first. Must declare the DP array as static array to limit time"""
class Solution(object):

    dp = [0] * 10001

    for i in range(1, 101):
        dp[i**2] = 1

    def numSquares(self, n):
        for i in range(2,n+1):
            x = 1
            if self.dp[i]!=0:
                    continue
            self.dp[i] = n
            while x*x<=i:
                self.dp[i] = min(self.dp[i],self.dp[i-x*x]+1)
                x+=1

        return self.dp[n]
