#!/usr/bin/env python
# encoding: utf-8

"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = walk = ListNode(0)
        dummy.next = head
        while walk.next:
            if walk.next.val == val:
                walk.next = walk.next.next
            else:
                walk = walk.next

        return dummy.next

    # Instantiate the new object ListNode dummy consumes a lot of time
 # method 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val==val:
            head = head.next
        if not head:
            return head
        walk = head
        while walk.next:
            if walk.next.val == val:
                walk.next = walk.next.next
            else:
                walk = walk.next
        return head
