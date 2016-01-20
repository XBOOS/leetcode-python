#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        money = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                money[i]=nums[0]
            elif i==1:
                money[i] = max(nums[0],nums[1])
            else:
                money[i] = max(money[i-1],money[i-2]+nums[i])

        return money[len(nums)-1]

