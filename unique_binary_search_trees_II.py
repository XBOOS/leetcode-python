#!/usr/bin/env python
# encoding: utf-8
"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}"."""

""" Incorrect. need to be changed"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [0]*(n+1)
        dp[0] = None

        def dfsAdd(root,addVal):
            if not root:
                return root
            root.val+=addVal
            dfsAdd(root.left,addVal)
            dfsAdd(root.right,addVal)

        trees = list()
        for i in range(1,n+1):
            for j in range(i): # j represents how many nodes are in the left subtree
                root = TreeNode(j+1)
                root.left = dp[i]
                root.right = dp[i-1-j]
                dfsAdd(root.right,j)
            trees.append(root)
            dp[i] = trees
        return dp[n]
