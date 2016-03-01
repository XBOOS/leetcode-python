#!/usr/bin/env python
# encoding: utf-8

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

"""

""" Method 1: remove the smaller one which will not make up the bigger container."""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # maxs = [0]*n
        # mins = [0]*n
        # maxs[0] = mins[0] = height[0]
        i = 0
        j = n-1
        maxArea = 0
        while i<j:
            maxArea = max(maxArea,min(height[i],height[j])*(j-i))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return maxArea

""" Method 2 take the smaller one to be the bar"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # maxs = [0]*n
        # mins = [0]*n
        # maxs[0] = mins[0] = height[0]
        i = 0
        j = n-1
        maxArea = 0
        while i<j:
            smaller = min(height[i],height[j])
            maxArea = max(maxArea,smaller*(j-i))
            while i<j and height[i]<=smaller:
                i+=1
            while i<j and height[j]<=smaller:
                j-=1


        return maxArea

""" Method 3  Faster solution"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # maxs = [0]*n
        # mins = [0]*n
        # maxs[0] = mins[0] = height[0]
        i = 0
        j = n-1
        maxArea = 0
        while i<j:
            loMax = height[i]
            hiMax = height[j]
            if loMax<hiMax:
                maxArea = max(maxArea,loMax*(j-i))
                while i<j and height[i]<=loMax:
                    i+=1
            else:
                maxArea = max(maxArea,hiMax*(j-i))
                while i<j and height[j]<=hiMax:
                    j-=1

        return maxArea


