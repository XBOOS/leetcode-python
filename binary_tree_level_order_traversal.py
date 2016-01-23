#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

"""
Method1: maintain two queue for intercharging level orders."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current = queue1 = [root]
        next = queue2 = list()
        result = list()

        while current:
            tmp = list()
            for i in range(len(current)):
                tmp.append(current[i].val)
                if current[i].left:
                    next.append(current[i].left)
                if current[i].right:
                    next.append(current[i].right)
            result.append(tmp)
            current = next[:]
            del next[:]

        return result





