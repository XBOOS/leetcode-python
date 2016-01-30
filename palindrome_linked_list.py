#!/usr/bin/env python
# encoding: utf-8

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?"""
"""
This is singly linked list,so I cannot traverse it in reverse order, so if i want
to check wether it is palindrome, I have to change half of the list to
linke list.
Thus I need to know the length frist
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        walk = head
        while walk:
            length +=1
            walk = walk.next

        if length==0:
            return True
        elif length==1:
            return True

        #reverse the linked list first, then compare
        prev = None
        current = head
        step = 0
        while step<length/2:
            next = current.next
            current.next = prev
            prev = current
            current = next
            step +=1
        #now the prev is the head
        walk1 = prev
        if length%2 == 0:
            walk2 = next
        else:
            walk2 = next.next
        while walk1:
            if walk1.val != walk2.val:
                return False
            walk1 = walk1.next
            walk2 = walk2.next

        return True

