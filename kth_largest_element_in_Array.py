#!/usr/bin/env python
# encoding: utf-8

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length."""

""" Method1 cheating"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]


    """ Method2 O(nk) TLE"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        basket = [-214748364]*k
        basket[-1] = nums[0]
        n = len(nums)
        for i in range(1,n):
            cur = 0
            while cur<k and nums[i]>=basket[cur]:
                cur+=1
            if cur<k:
                basket[cur] =nums[i]
        return basket[-1]

""" Method3  recursive quick selection.   linear complexity
Attention:
1) change it to kth smallest. as i just pass in low and high index, k is not changing. didnt change the array.
2) the classic partition method to return the index of the pivot value. the right way is actually to find the medianThree.
only using the partition. each time hopefully descard half of the array.
3) in quicksort, recursively do the partition to both part.
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickSelection(l,r,k):
            if l>r:
                return 214748364
            if l==r:
                return nums[l]
            pivot = nums[r]
            left = l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[left],nums[i] = nums[i],nums[left]
                    left+=1
            nums[r],nums[left] = nums[left],nums[r]
            if left==k:
                return nums[left]
            elif left>k:
                return quickSelection(l,left-1,k)
            else:
                return quickSelection(left+1,r,k)

        return quickSelection(0,len(nums)-1,len(nums)-k)

"""
Method4 just change the recuisive method3 to iterative one"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        k = len(nums)-k
        while True:
            if l>r:
                return 214748364
            if l==r:
                return nums[l]
            pivot = nums[r]
            left = l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[left],nums[i] = nums[i],nums[left]
                    left+=1
            nums[r],nums[left] = nums[left],nums[r]
            if left==k:
                return nums[left]
            elif left>k:
                r = left-1
            else:
                l = left+1



