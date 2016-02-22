#!/usr/bin/env python
# encoding: utf-8

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6."""

""" This is classic dynamic programming problem"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if leng==0:
            return 0
        maxSum = nums[0]
        curSum = [0]*leng
        curSum[0]=nums[0]
        for i in range(1,leng):
            curSum[i] = max(curSum[i-1]+nums[i],nums[i])
            maxSum = max(curSum[i],maxSum)
        return maxSum
