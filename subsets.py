#!/usr/bin/env python
# encoding: utf-8

"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
""" Backtracing"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.getSubsets(0,nums)

    def getSubsets(self,idx,nums):
        if idx>=len(nums):
            return [[]]
        res = list()
        subsets = self.getSubsets(idx+1,nums)
        for subset in subsets:
            res.append(subset[:])
            subset.append(nums[idx])
            subset.sort()
            if subset not in res:
                res.append(subset[:])
        return res


