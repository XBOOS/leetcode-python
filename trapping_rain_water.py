#!/usr/bin/env python
# encoding: utf-8

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!"""

""" Method1 by myself. So happy to get accepted the first submit!"""
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



