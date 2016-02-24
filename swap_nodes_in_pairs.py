#!/usr/bin/env python
# encoding: utf-8

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed."""


""" The lesson is that I must use an intermediate space to store the next,when I want to swap linked nodes"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            prev.next = head.next
            nxt = head.next.next
            head.next.next = head
            head.next = nxt
            prev = head
            head = nxt

        return dummy.next

