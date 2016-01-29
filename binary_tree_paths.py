#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        elif not root.right and not root.left:
            return [str(root.val)]
        elif root.right and root.left:
            return [str(root.val)+"->"+x for x in self.binaryTreePaths(root.left)]+[str(root.val)+"->"+x for x in self.binaryTreePaths(root.right)]
        elif not root.right:
            return [str(root.val)+"->"+x for x in self.binaryTreePaths(root.left)]
        else:
            return [str(root.val)+"->"+x for x in self.binaryTreePaths(root.right)]

