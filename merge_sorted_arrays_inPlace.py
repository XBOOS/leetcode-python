#!/usr/bin/env python
# encoding: utf-8

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively."""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[n:m+n] = nums1[0:m]
        i = n
        j = 0
        k = 0
        while i<m+n and j<n:
            if nums1[i]<nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k+=1
        if j<n:
            for jj in range(j,n):
                nums1[k] = nums2[jj]
                k+=1

