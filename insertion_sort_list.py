#!/usr/bin/env python
# encoding: utf-8


"""TLE"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while head:
            nextNode = head.next
            walk = dummy
            while  walk.next and walk.next.val<head.val:
                walk = walk.next
            head.next = walk.next
            walk.next = head
            head = nextNode
        return dummy.next
""" I dont know why there is TLE here. I used C++ it worked fine. Maybe due to something wrong of python semantics? or just python is slow"""
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode dummy(0);
        ListNode *walk,*next;

        while(head!=NULL){
            walk = &dummy;
            next = head->next;
            while (walk->next!=NULL && walk->next->val<head->val)
            {
                walk = walk->next;
            }
            head->next = walk->next;
            walk->next = head;
            head = next;

        }
        return dummy.next;
    }
};


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while head:
            nextNode = head.next
            walk = dummy
            while walk:
                if not walk.next or walk.next.val>head.val:
                    head.next = walk.next
                    walk.next = head
                    break
                walk = walk.next
            head = nextNode
        return dummy.next

