#!/usr/bin/env python
# encoding: utf-8

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!"""

""" Method1 Recursion by myself. So happy to get accepted the first submit!
The two sides are important! The lower one dicide the throughout height.
THe classic l<r condition in the while loop!"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]: return 0
        def trapWithBar(bar):
            l = 0
            r = len(height)-1
            while l<r and height[l]<=bar:
                l+=1
            while l<r and height[r]<=bar:
                r-=1
            minHeight = min(height[l],height[r])
            if l>=r: return 0
            acc = 0
            for i in range(l+1,r):
                acc+=max(0,minHeight-max(bar,height[i]))
            return acc+trapWithBar(minHeight)

        return trapWithBar(0)



""" Method 2 change the recursive solution to iterative."""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]: return 0
        bar = 0
        acc = 0
        l = 0
        r = len(height)-1
        while True:
            while l<r and height[l]<=bar:
                l+=1
            while l<r and height[r]<=bar:
                r-=1
            minHeight = min(height[l],height[r])
            if l>=r: return acc
            for i in range(l+1,r):
                acc+=max(0,minHeight-max(bar,height[i]))
            bar = minHeight

        return acc




