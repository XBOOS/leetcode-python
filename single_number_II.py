#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
""" Method 1 Sorting"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        nums.sort()
        i=0
        while i <leng-2:
            if nums[i]!= nums[i+2]:
                return nums[i]
            else:
                i+=3
        return nums[leng-1]

    """"""


