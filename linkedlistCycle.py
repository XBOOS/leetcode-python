#Method 1 : with O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        
        while head!=None:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False    


#Method 2 without extra space but changed the original linkedlist
 class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head!=None:
            if head.val==None:
                return True
            head.val = None    
            head = head.next
            
        return False   


# A pretty clever one

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
            
        slow = head.next
        fast = head.next.next
        while slow!=None and fast !=None:
            if slow==fast:
                return True
                
            slow = slow.next
            if fast.next==None:
                return False
            fast = fast.next.next
        return False
