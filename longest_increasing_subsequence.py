#!/usr/bin/env python
# encoding: utf-8

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?"""

# Method 1 dynamic programming
"""
The state is defiend to be the longest increasing sequence ending at this point.
the transformation among states are maxLeng[i] = max(maxLeng[i],maxLeng[j]+1 for any j<i)
The final result is the maximum of the whole maxLeng list. The total time complexity is 0+1+2+3+...+(n-1) O(n^2)"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        leng = len(nums)
        maxs = [1]*leng

        for i in range(1,leng):
            for j in range(i):
                if nums[j]<nums[i]:
                    maxs[i] = max(maxs[i],maxs[j]+1)

        return max(maxs)

"""
Method 2 """
