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

""" Modification: there's no need to max and min. it is for sure shrinking the range"""
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
                res &= isValidBSTHelper(root.left,minVal,root.val)
            if root.right:
                res &= isValidBSTHelper(root.right,root.val,maxVal)
            return res

        if not root:return True
        return isValidBSTHelper(root,-2147483649,2147483648)

""" Method3  Using inorder traversal. and an extra record prev. the inorder traversal of a binary search tree will output the right order of tree"""
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
        if not root:
            return True
        prev = -2147483849
        stack = list()
        while root or stack:
            if root:
                tmp = root
                stack.append(tmp)
                root = root.left
            else:
                root = stack.pop()
                if root.val<=prev:
                    return False
                prev = root.val
                root = root.right
        return True

