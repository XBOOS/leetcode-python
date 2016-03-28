#!/usr/bin/env python
# encoding: utf-8

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?"""

"""Method 1 using recursion:"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        return self.inorder(root,res)
    def inorder(self,root,res):
        """
        :rtype:None
        """
        if not root:
            return res
        if root.left:
            self.inorder(root.left,res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right,res)
        return res

    """ Method2 interactively using stack
    traverse going into the leftmost node and pop it out and record the value,
    if it has a right child, add the right child to the stack"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = list()
        while stack:
            tmp = stack[-1]

            while tmp.left:
                stack.append(tmp.left)
                left = tmp.left
                tmp.left = None  # pretty important!!! avoid go left again.
                tmp = left
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)

        return res

"""Comparing to method 3, this method kind of lost control of the processing,
only record the stack, but not the in stack control point. so to make a mod here"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = list()
        pushControl = True
        while stack:
            tmp = stack[-1]
            if pushControl:
                while tmp.left:
                    stack.append(tmp.left)
                    tmp = tmp.left

            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
                pushControl = True
            else:
                pushControl = False
        return res






""" Method 3 no need to modify the tree iteself"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
""" To simulate the recursion process. The current means the focus of processing"""

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        stack = list()
        current = root
        while current or stack!=[]:
            if current:
                stack.append(current)
                current = current.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                current = tmp.right

        return res



""" Method 4 a good solution"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res



