#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists. Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = result
        while l1 !=None and l2 !=None:
            if l1.val<l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        if l1!=None:
            tmp.next = l1
        if l2!=None:
            tmp.next = l2

        return result.next
