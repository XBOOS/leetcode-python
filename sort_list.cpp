/*
 *Sort a linked list in O(n log n) time using constant space complexity.
 */


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/*
 * Method1. Recursive merge sort
 * helper functions: mergeList(),splitList()::return the head of the seconde one(i.e.findMiddleNode)
 *
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head||!head->next) return head;
        ListNode* nextHead = splitList(head);
        ListNode* res1 = sortList(head);
        ListNode* res2 = sortList(nextHead);
        return mergeList(res1,res2);


    }

private:
//split the list into two part with almost the same length.
//return the head of the second list--also the middle node of the original list
//remember to slice the node by setting the fist list's last'node->next ==NULL!

    ListNode* splitList(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next!=NULL && fast->next->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* nextHead = slow->next;
        slow->next = NULL;
        return nextHead;

    }
    ListNode* mergeList(ListNode* head1,ListNode* head2){
        ListNode fakeHead = ListNode(-1);
        ListNode* walkNode = &fakeHead;

        while(head1 && head2){
            if(head1->val<=head2->val){//append head2 after head1
                walkNode->next = head1;
                head1 = head1->next;
            }else{
                walkNode->next = head2;
                head2 = head2->next;
            }
            walkNode = walkNode->next;
        }
        if(head1) walkNode->next = head1;
        if(head2) walkNode->next = head2;
        return fakeHead.next;
    }

};
