#!/usr/bin/env python
# encoding: utf-8

"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


""" Method: Be careful of the transformation equation and computing order.
The outer loop should be the length of ballons in [i,j], not the
for left in range(1,n+1):
    right in range(left+1,n+1). here we compute the different length first. which is false

Another point is the k. k is defiend to be the last ballon bursted. so nums[l-1]*nums[k]*nums[r+1]    """
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if nums==[] or n==0:
            return 0
        nums = [1]+nums+[1]
        dp = [[0]*(n+2) for x in range(n+2)]

        for length in range(1,n+1):
            for l in range(1,n+2-length):
                r = l+length-1
                for k in range(l,r+1):
                    dp[l][r] = max(dp[l][r],dp[l][k-1]+dp[k+1][r]+nums[l-1]*nums[k]*nums[r+1])

        return dp[1][n]


