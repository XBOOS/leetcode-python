#!/usr/bin/env python
# encoding: utf-8

"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Subscribe to see which companies asked this question"""


"""
It is to traverse the non-complete binary tree level by level.
Usually a queue is needed, but here we can use next pointer to maintain the queue of nodes
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
        if not root:
            return

        highHead = root
        lowHead = None
        pre = None
        while highHead:
            highCur = highHead
            while highCur:
                if highCur.left:
                    if not lowHead:
                        lowHead = highCur.left
                        pre = lowHead
                    else:
                        pre.next = highCur.left
                        pre = pre.next
                if highCur.right:
                    if not lowHead:
                        lowHead = highCur.right
                        pre = lowHead
                    else:
                        pre.next = highCur.right
                        pre = pre.next
                highCur = highCur.next
            highHead = lowHead
            lowHead = None
