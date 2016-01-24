#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        current = [root]
        next = list()
        while len(current)!=0:
            depth += 1
            for node in current:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next[:]
            next = []


