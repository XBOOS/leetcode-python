#!/usr/bin/env python
# encoding: utf-8

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

""" Method 1 maintain two locations to store red and blue ones.
and a walk pointer to do the test and swap. Be careful that after the swapping of
walk and j, walk remains and check the value"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        walk = 0
        while walk<=j:
            if nums[walk]==0:
                nums[i],nums[walk] = nums[walk],nums[i]
                i += 1
                walk += 1
            elif nums[walk]==2:
                nums[j],nums[walk] = nums[walk],nums[j]
                j -=1
            else:
                walk +=1



""" Method 2 count sort"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #count sort
        red = white = blue = 0
        for num in nums:
            if num==0:
                red +=1
            elif num==1:
                white +=1
        for i in range(red):
            nums[i]=0
        for i in range(red,red+white):
            nums[i]=1
        for i in range(red+white,len(nums)):
            nums[i]=2

