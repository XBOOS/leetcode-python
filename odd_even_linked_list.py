#!/usr/bin/env python
# encoding: utf-8

# Method 1
# Must loop the walk with stepsize of 2
# could also make dummy starting node then start with head not head.next.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oddHead = odd = head
        evenHead = even = head.next
        head = head.next.next
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if head.next:
                head = head.next.next
            else:
                head = None

        odd.next = evenHead
        return oddHead

# Method 2
# Time limit exeeds!!  walk one step each time

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next

        while even.next:
            odd.next = even.next
            odd = odd.next
            if odd.next:
                even.next = odd.next
                even = even.next
        odd.next = head.next
        return head

