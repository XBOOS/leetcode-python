#!/usr/bin/env python
# encoding: utf-8

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""

""" Method1 using """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # dummy = ListNode(0)
        # dummy.next = head

        smallHead = smallCur = ListNode(0)
        bigHead = bigCur = ListNode(0)

        while head:
            if head.val<x:
                smallCur.next = head
                smallCur = smallCur.next
            else:
                bigCur.next = head
                bigCur = bigCur.next
            head = head.next
        smallCur.next = bigHead.next
        return smallHead.next




""" TLE"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_slow = prev_fast = dummy

        def swap(prev1,node1,prev2,node2):
            tmp = node1.next
            node1.next = node2.next
            node2.next = tmp
            prev1.next = node2
            prev2.next = node1

        if not head:
            return head
        fast = slow = head
        while fast:
            if fast.val<x:
                swap(prev_fast,fast,prev_slow,slow)
                slow = slow.next
                prev_slow = prev_slow.next
            fast = fast.next
            prev_fast = prev_fast.next
        return head
