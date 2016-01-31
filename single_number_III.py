#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?"""

""" Method 1 bit manipulation"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor =0
        for num in nums:
            xor ^=num

        last_diff_bit = xor & ~(xor-1)
        res = [0]*2
        for num in nums:
            if num&last_diff_bit==0:
                res[0] ^=num
            else:
                res[1] ^=num
        return res

""" Method2 Sorting first"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums.sort()
        i = 0
        leng=len(nums)
        while i <leng-1:
            if nums[i]!=nums[i+1]:
                res.append(nums[i])
                i+=1
            else:
                i+=2
        if i<leng:
            res.append(nums[i])
        return res
