#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""

""" Method 1: three pass"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leng=len(nums)
        res = [1]*leng
        for i in (range(leng-1)[::-1]):
            res[i] = res[i+1]*nums[i+1]

        for i in range(1,leng):
            nums[i] = nums[i-1]*nums[i]

        for i in range(1,leng):
            res[i] *=nums[i-1]
        return res


    """Method 2, two passes and a little bit faster"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leng=len(nums)
        res = [1 for _ in range(leng)]
        for i in range(1,leng):
            res[i] = res[i-1]*nums[i-1]

        tmp = nums[leng-1]
        for i in (range(leng-1)[::-1]):
            res[i] *= tmp
            tmp *=nums[i]
        return res
