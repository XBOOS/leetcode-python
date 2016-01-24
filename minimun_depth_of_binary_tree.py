#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""
# method 1 : interactive way

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


# method2 : recursive way
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
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return self.minDepth(root.left)+1
        elif root.right and not root.left:
            return self.minDepth(root.right)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1

