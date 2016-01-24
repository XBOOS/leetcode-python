#!/usr/bin/env python
# encoding: utf-8

"""

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # first detect if intersection by the last one. and if yes, how many nodes more than another one
        # start from the same distant from the end
        if not headA or not headB:
            return None
        if headA == headB:
            return headA

        walk1 = headA
        walk2 = headB
        while walk1.next and walk2.next:
            walk1 = walk1. next
            walk2 = walk2. next
        if not walk1.next and not walk2.next:
            if walk1 != walk2:
                return None
        #else detect
        step = 0
        if walk1.next:
            while walk1.next:
                walk1 = walk1.next
                step +=1
            if walk1 !=walk2:
                return None
            walk1 = headA
            walk2 = headB
        elif walk2.next:
            while walk2.next:
                walk2 = walk2.next
                step += 1
            if walk1 !=walk2:
                return None
            walk1 = headB
            walk2 = headA
        else:
            walk1 = headA
            walk2 = headB
        while step>0:
            walk1 = walk1.next
            step -= 1

        while walk1:
            if walk1==walk2:
                return walk1
            walk1 = walk1.next
            walk2 = walk2.next


