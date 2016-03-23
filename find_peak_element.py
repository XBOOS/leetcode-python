#!/usr/bin/env python
# encoding: utf-8

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i <n-1 and nums[i]<nums[i+1]:
            i+=1
        return i


""" Method2 need to do in logarithmic complexity
Maintain the invariants. It keeps shrinking the area //like a plague??....
nums[left-1]<nums[left] and nums[right]<nums[right+1]. when left=right.obviously it's a local peak.
Fantastic solution!"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low+high)/2
            if nums[mid]< nums[mid+1]:
                low  = mid+1
            else:
                high = mid
        return low#or high
