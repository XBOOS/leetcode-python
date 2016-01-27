#!/usr/bin/env python
# encoding: utf-8

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n==0:
            return head

        king = soldier = dummy = ListNode(0)
        dummy.next = head
        step = n
        while step>0 and soldier.next:
            soldier = soldier.next
            step -=1

        while soldier.next:
            king = king.next
            soldier = soldier.next
        if not king.next:
            return None
        if not king.next.next:
            king.next = None
        else:
            king.next = king.next.next
        return dummy.next


