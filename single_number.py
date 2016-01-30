#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        nums.sort()
        i = 0
        while i<len(nums)-2:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2
        return nums[len(nums)-1]
