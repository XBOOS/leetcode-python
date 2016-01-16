#!/usr/bin/env python
# encoding: utf-8

# Notice the difference between binary tree and binary search tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        m = n = 0
        if p.val > q.val:
            m = q.val
            n = p.val
        else:
            m = p.val
            n = q.val
        if not root:
            return root
        if m<=root.val<=n:
            return root
        elif root.val<m:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)

