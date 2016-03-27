#!/usr/bin/env python
# encoding: utf-8

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""
""" Need to be really careful about the edge cases. take care of the input.
k = k%leng
leng==0
k==0
leng==k"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head

        #find the leng of list
        leng = 0
        walk = head
        while walk:
            leng+=1
            walk = walk.next
        k = k%leng
        count = leng-k
        if not count or k==0:return head
        walk = head
        while count>1:
            count-=1
            walk = walk.next
        tmp = walk.next
        walk.next = None
        walk3 = tmp
        count = k
        while count>1:
            count-=1
            walk3 =walk3.next
        walk3.next = head
        return tmp


