#!/usr/bin/env python
# encoding: utf-8

"""

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
    """
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.connect_with_sibling(root,None)

    def connect_with_sibling(self,root,sibling):
        if not root:
            return
        root.next = sibling
        if not root.left:
            return
        self.connect_with_sibling(root.left,root.right)
        if sibling:
            self.connect_with_sibling(root.right,sibling.left)
        else:
            self.connect_with_sibling(root.right,None)


"""Method 2.
In method 1 I deal with the root's next in the current loop, here I can deal with it in the previous loop,
so that, after checking root's next, can decide root.right.next"""
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            self.dfs(root)

    def dfs(self,root):
        if not root.left:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        else:
            root.right.next = None
        self.dfs(root.left)
        self.dfs(root.right)
