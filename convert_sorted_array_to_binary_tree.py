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
        elif length==1:
            return TreeNode(nums[0])
        else:
            middle = length/2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[:middle])
            root.right = self.sortedArrayToBST(nums[middle+1:])
            return root
