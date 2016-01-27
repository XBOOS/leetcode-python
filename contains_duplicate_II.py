#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k."""
"""
Lessons learned:
1. distance k means 0...k not 0....(k-1)
2. to detect duplicates, consider using set()"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k<1: return False
        n = len(nums)
        bag = set()
        i = 0
        while i<n and i<k+1:
            if nums[i] in bag:
                return True
            else:
                bag.add(nums[i])
            i+=1

        while i<n:
            bag.remove(nums[i-k-1])
            if nums[i] in bag:
                return True
            else:
                bag.add(nums[i])
            i+=1
        return False
