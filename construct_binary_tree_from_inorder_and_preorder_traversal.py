#!/usr/bin/env python
# encoding: utf-8

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree."""

""" Must use offset to shift the array position.
Runtime error is due to illegal memory access!"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        m = len(preorder)
        n = len(inorder)
        if m!=n or m==0:
            return None
        if m==1:
            return TreeNode(inorder[0])

        def rangeBuild(pstart,pend,istart,iend):
            if pstart>pend:
                return None
            if pstart==pend:
                return TreeNode(preorder[pstart])
            root = TreeNode(preorder[pstart])
            rootIdx = inorder.index(preorder[pstart])

            root.left = rangeBuild(pstart+1,rootIdx-istart+pstart,istart,rootIdx-1)
            root.right = rangeBuild(rootIdx-istart+pstart+1,pend,rootIdx+1,iend)
            return root

        return rangeBuild(0,m-1,0,n-1)
