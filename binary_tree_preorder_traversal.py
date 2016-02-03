#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?"""

""" Method 1 using recursion.
adding another argument to the method to adding the return result list"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        return self.preorder(root,res)
    def preorder(self,root,res):
        if not root:
            return res
        res.append(root.val)
        self.preorder(root.left,res)
        self.preorder(root.right,res)
        return res

""" Method 2 traverse iteractively using stack. I used queue at first which is false,
queue is for level traversal.
But when using stack, take care to push in right child first and then the left child"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = list()
        stack = [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res




