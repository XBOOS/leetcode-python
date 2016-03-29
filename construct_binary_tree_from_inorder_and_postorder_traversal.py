#!/usr/bin/env python
# encoding: utf-8

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree."""

""" Lesson: I wrote > to > at the begining!!! And wasted a lot of times!!"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        m = len(inorder)
        n = len(postorder)

        if m!=n or m==0:
            return None
        if m==1:
            return TreeNode(inorder[0])
        def rangeBuild(istart,iend,pstart,pend):
            if istart>iend:
                return None
            if istart==iend:
                return TreeNode(inorder[istart])


            root = TreeNode(postorder[pend])
            # rootIdx = postorder.index(inorder[istart+1])
            rootIdx = inorder.index(postorder[pend])
            root.left = rangeBuild(istart,rootIdx-1,pstart,rootIdx-istart+pstart-1)
            root.right = rangeBuild(rootIdx+1,iend,rootIdx-istart+pstart,pend-1)
            return root

        return rangeBuild(0,m-1,0,n-1)
