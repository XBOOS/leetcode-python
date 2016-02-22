#!/usr/bin/env python
# encoding: utf-8

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length<1:
            return None
        else:
            middle = length/2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[:middle])
            root.right = self.sortedArrayToBST(nums[middle+1:])
            return root# Definition for a binary tree node.


""" Method 1 is not quick enough, maybe due to the continuous copy of the array, i should just pass the bound of the array
Below is method 2 using helper function"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBST_withrange(nums,0,len(nums)-1)
    def sortedArrayToBST_withrange(self,nums,l,r):
        if r-l<0:
            return None
        else:
            middle = (l+r)/2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST_withrange(nums,l,middle-1)
            root.right = self.sortedArrayToBST_withrange(nums,middle+1,r)
            return root
