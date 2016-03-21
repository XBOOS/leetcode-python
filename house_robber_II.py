#!/usr/bin/env python
# encoding: utf-8

"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""
"""
Method 1. Need to be optimized to have less condition decision"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if leng==0:return 0
        elif leng==1:return nums[0]
        elif leng==2:return max(nums[0],nums[1])
        maxs1 = [0]*leng #with the first element
        maxs2 = [0]*leng #without the first element
        maxs1[0] = maxs1[1] = nums[0]
        maxs2[1] = nums[1]

        for i in range(2,leng-1):
            maxs1[i] = max(maxs1[i-1],maxs1[i-2]+nums[i])
            maxs2[i] = max(maxs2[i-1],maxs2[i-2]+nums[i])

        maxs1[leng-1] = maxs1[leng-2]
        maxs2[leng-1] = max(maxs2[leng-2],maxs2[leng-3]+nums[leng-1])

        return max(maxs1[-1],maxs2[-1])

"""Method 2 make the condition decisino in the loop"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if leng<=0:return 0

        maxs1 = [0]*leng #with the first element
        maxs2 = [0]*leng #without the first element
        maxs1[0] = nums[0]

        for i in range(1,leng):
            if i<2:
                maxs1[i] = max(maxs1[i-1],nums[i])
                maxs2[i] = max(maxs2[i-1],nums[i])
            else:
                maxs1[i] = max(maxs1[i-1],maxs1[i-2]+nums[i])
                maxs2[i] = max(maxs2[i-1],maxs2[i-2]+nums[i])

        maxs1[leng-1] = maxs1[leng-2]
        #maxs2[leng-1] = max(maxs2[leng-2],maxs2[leng-3]+nums[leng-1])

        return max(maxs1[-1],maxs2[-1])
