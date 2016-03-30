#!/usr/bin/env python
# encoding: utf-8


""" Use the classic range bound binary search( attention to the difference for pure
binay search) to search for the lower bound and the higher bound"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchLowerBound(low,high):
            while low<=high:
                mid = (low+high)/2
                if nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
            return low

        def searchHigherBound(low,high):
            while low<=high:
                mid = (low+high)/2
                if nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return high
        low = searchLowerBound(0,len(nums)-1)
        high = searchHigherBound(0,len(nums)-1)
        if low>high:
            return [-1,-1]
        else:
            return [low,high]

""" Incorrect problematic solution. Cant tell if we already found the value.will
append non-neccessary [-1,-1].Could pass a flag parameter through recursion.
but this is not a good solution"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.minIdx = len(nums)-1
        self.maxIdx = 0
        if self.minIdx==self.maxIdx:
            if nums[0]!=target:
                return [-1,-1]
            else:
                return [0,0]
        def searchRangeHelper(low,high):
            if low>high:
                return
            if low==high:
                if nums[low]==target:
                    self.minIdx = min(low,self.minIdx)
                    self.maxIdx = max(low,self.maxIdx)
                else:
                    return
            mid = (low+high)/2
            if nums[mid]>target:
                searchRangeHelper(low,mid-1)
            elif nums[mid]<target:
                searchRangeHelper(mid+1,high)
            else:
                self.minIdx = min(low,self.minIdx)
                self.maxIdx = max(low,self.maxIdx)
                searchRangeHelper(low,mid-1)
                searchRangeHelper(mid+1,high)
        searchRangeHelper(0,len(nums)-1)
        if self.minIdx>self.maxIdx:
            return [-1,-1]
        else:
            return [self.minIdx,self.maxIdx]

