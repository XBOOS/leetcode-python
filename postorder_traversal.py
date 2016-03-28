#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""

""" Trivial recursion solution"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = []
        right = []
        if root.left:
            left = self.postorderTraversal(root.left)
        if root.right:
            right = self.postorderTraversal(root.right)
        return left+right+[root.val]


""" Method 2 the non-recursive way.Use while loop to mimic one the recursive processing of stack.
and one stack to store the remiaining information waiting to be processed later.
use root==None to determine whether it's the end traversal along left side."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = list()
        res = []
        prev = None
        if not root:return []
        while root or stack!=[]:
            if root:
                tmp = root
                stack.append(tmp)
                root = root.left
            elif stack[-1].right==prev: #have already traversed the right subtree, pop and print the root
                prev = stack.pop()
                res.append(prev.val)
            else:
                root = stack[-1]
                root = root.right
                prev = None

        return res

