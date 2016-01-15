#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return
        left = 0
        right =1
        while left<right and right<len(nums):
            if nums[left]==0:
                while nums[right]==0 :
                    right += 1
                    if right >= len(nums):
                        return
                nums[left],nums[right]=nums[right],nums[left]
            left +=1
            right +=1
