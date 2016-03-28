#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidBSTHelper(root,minVal,maxVal):

            if not root:
                return True

            res = (minVal<root.val<maxVal)
            if root.left:
                res &= isValidBSTHelper(root.left,minVal,min(maxVal,root.val))
            if root.right:
                res &= isValidBSTHelper(root.right,max(minVal,root.val),maxVal)
            return res

        if not root:return True
        return isValidBSTHelper(root,-2147483649,2147483648)

