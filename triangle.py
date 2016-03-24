#!/usr/bin/env python
# encoding: utf-8

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11)."""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if not triangle or n==0:
            return 0
        dp = [214748364]*(n+1)
        dp[1] = triangle[0][0]
        for row in range(1,n):
            for col in (range(1,row+2)[::-1]):
                dp[col] = min(dp[col-1],dp[col])+triangle[row][col-1]
        return min(dp[1:])
