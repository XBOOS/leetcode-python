#!/usr/bin/env python
# encoding: utf-8

"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
 Method1 : TLE!!!!
 Obviously that I computed the son and grandson at the parent.where the grandson
 will be recomputed in the future."""

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lmax = rmax = lmax_noroot = rmax_noroot = 0
        if root.left:
            lmax = self.rob(root.left)
            lmax_noroot = self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            rmax = self.rob(root.right)
            rmax_noroot = self.rob(root.right.left)+self.rob(root.right.right)

        return max(lmax+rmax,root.val+lmax_noroot+rmax_noroot)

""" Method2 Dynamic programming. Recursion with memoriazation.
Here pay attention to that for DP, we maintain a list to access the precomputed result to avoid recomputation.
But here in a tree we cannot store the data (one way is to maintain a boolean hasComputed+update the val to max),
so we need to return two level data(son and grandson) back to father when go back in the recursive process"""
