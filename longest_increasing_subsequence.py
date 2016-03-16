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


""" A little bit optimization of the corner case detection"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        maxs = [1]*leng

        for i in range(1,leng):
            for j in range(i):
                if nums[j]<nums[i]:
                    maxs[i] = max(maxs[i],maxs[j]+1)

        return max(maxs) if maxs else 0
"""
Method 2. From others. Really brilliant idea.
in method 1 some of the traversal time is wasted. because we maintained some information we no more need.
only when the encounter element is lareger than all the previous ones, we increase the length by 1.
we maintain a sorted list.always update it with smallest at the particular point of the array.
Using binary search to locate the updating position. so the time complexity is O(nlog(n))"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        leng = len(nums)
        tool = []

        for i in range(leng):
            low = 0
            high = len(tool)-1
            while low<=high:
                mid = (low+high)/2
                if tool[mid]==nums[i]:
                    break
                elif tool[mid]>nums[i]:
                    high = mid-1
                else:
                    low = mid+1
            if low<=high:
                continue
            if low>=len(tool):
                tool.append(nums[i])
            else:
                tool[low] = nums[i]

        return len(tool)

""" Also could modify like this to deal with the exact found situation"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        leng = len(nums)
        tool = []

        for i in range(leng):
            low = 0
            high = len(tool)-1
            while low<=high:
                mid = (low+high)/2
                if tool[mid]>=nums[i]:
                    high = mid-1
                else:
                    low = mid+1
            if low>=len(tool):
                tool.append(nums[i])
            else:
                tool[low] = nums[i]

        return len(tool)

