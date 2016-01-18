#!/usr/bin/env python
# encoding: utf-8

# Remember when to update pre and when not

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(None)
        walk = head
        while walk:
            if walk.val == pre.val:
                pre.next = walk.next
            else:
                pre = walk
            walk = walk.next


        return head
