#!/usr/bin/env python
# encoding: utf-8

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array."""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        for i in range(1,leng):
            if nums[i]-nums[i-1]<0:
                return nums[i]
        return nums[0]
