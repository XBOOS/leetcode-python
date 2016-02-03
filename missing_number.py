#!/usr/bin/env python
# encoding: utf-8

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

""" Method 1 using bit manipulation, hint from the maximum product of words length
to find the missing one
But this is not fast enough"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = 0
        for num in nums:
            bit |= 1<<num
        bit = bit^(bit+1)
        count = -1
        while bit>0:
            bit>>=1
            count +=1
        return count


    """Method 2 using XOR"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res^=(i^nums[i])
        return res


""" Method 3
if num after x all is 1 bigger than what it is supposed to be.
    then sum(nums)- (len(nums)-1)*len(nums)/2 is how many numbers is bigger"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        return leng-(sum(nums)-leng*(leng-1)/2)
