#!/usr/bin/env python
# encoding: utf-8

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
            if istart<iend:
                return None
            if istart==iend:
                return TreeNode(inorder[istart])

            root = TreeNode(inorder[istart])
        # left = TreeNode(inorder[1])
        # right = TreeNode(postorder[-1])
            rightIdx = postorder.index(inorder[istart+1])
            leftIdx = inorder.index(postorder[pend-1])
            root.left = rangeBuild(istart+1,leftIndx-1,pstart,rightIdx)
            root.right = rangeBuild(leftIdx,iend-1,leftIdx,pend-1)
            return root

        return rangeBuild(0,m-1,0,n-1)
