#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST)."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left = 0
        if root.left:
            left = self.countElement(root.left)
        if left < k-1:
            return self.kthSmallest(root.right,k-left-1)
        elif left == k-1:
            return root.val
        else:
            return self.kthSmallest(root.left,k)
    def countElement(self,root):
        if not root:
            return 0
        return self.countElement(root.left)+1+self.countElement(root.right)

