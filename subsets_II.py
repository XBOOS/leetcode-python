#!/usr/bin/env python
# encoding: utf-8

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]"""

""" Spent so long on trial and error. Here are some lessons learned
1. the length of res is changing, so becareful when it is used in the loop ending condition.
    need to store the original value in the beginning.
2. when it starts to duplicates, the length of duplicates is no changing , not each time numOfSubsets/2
3. remember the creating subset process.
    if this is not duplicate, adding this element to all the current element and insert it into the res array
    else just apply to the duplength
4. i+length-1 = j  (length = j-i+1)
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = [[]]
        startDup = False
        dupLength = 0
        for i in range(n):
            j=0
            numSubsets = len(res)
            if i>0 and nums[i]==nums[i-1]:
                if not startDup:
                    startDup=True
                    dupLeng = numSubsets/2
                j = numSubsets - dupLeng
            else:
                startDup = False
            while j<numSubsets:
                tmp = res[j][:]
                tmp.append(nums[i])
                res.append(tmp)
                j+=1
        return res
