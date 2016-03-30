#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

"""Method 1 linear search"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i<len(nums) and target>nums[i]:
            i+=1
        return i


""" Method 2 binary search"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)/2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return low


""" Testing for range search. range search is the same if there are no duplicates."""
""" Method3  lower_bound_range_search"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)/2
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return low

""" Higher bound range search. take care of the insertion position should be added 1 if not found"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)/2
            if nums[mid]<=target:
                low = mid+1
            else:
                high = mid-1
        if high<0 or nums[high]!=target:
            return high+1
        return high
