#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = end = 0

        for i in range(len(nums)):
            if (nums[i]-nums[start])==i-start:
                end = i
            elif start<end:
                res.append(str(nums[start])+"->"+str(nums[end]))
                start = end = i
            elif start==end:
                res.append(str(nums[start]))
                start = end =i
        print res
        if start<end:
            res.append(str(nums[start])+"->"+str(nums[end]))
        else:
            res.append(str(nums[start]))
        return res
