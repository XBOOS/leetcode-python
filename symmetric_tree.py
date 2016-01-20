#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.symmetric(root.left,root.right)


    def symmetric(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False
        else:
            return self.symmetric(root1.left,root2.right) and self.symmetric(root1.right,root2.left)



