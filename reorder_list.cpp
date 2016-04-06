/*
 *Given a singly linked list L: L0→L1→…→Ln-1→Ln,
 reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

 You must do this in-place without altering the nodes' values.

 For example,
 Given {1,2,3,4}, reorder it to {1,4,2,3}.
 *
 */

/* My original method. find the middle one and split,rotate the second list and do the merge
 */
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
    void reorderList(ListNode* head) {
        if(!head||!head->next||!head->next->next) return;
        ListNode* mid = findMiddle(head);
        mid = rotateList(mid);
        head = mergeList(head,mid);
    }
    ListNode* findTail(ListNode* head){
        if(!head) return head;
        while(head->next){
            head = head->next;
        }
        return head;
    }
    ListNode* findMiddle(ListNode* head){
        if(!head||!head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* middle = slow->next;
        slow->next = NULL;
        return middle;
    }
    ListNode* rotateList(ListNode* head){
        if(!head||!head->next) return head;
        ListNode* prev = head;
        head = head->next;
        prev->next = NULL;

        ListNode* next;
        while(head->next){
            next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        head->next = prev;
        return head;
    }

    ListNode* mergeList(ListNode* head1,ListNode* head2){
        ListNode dummy = ListNode(-1);
        ListNode* walk = &dummy;
        while(head1&&head2){
                walk->next = head1;
                head1 = head1->next;
                walk = walk->next;
                walk->next = head2;
                head2 = head2->next;
                walk = walk->next;
        }
        if(head1) walk->next =head1;
        if(head2) walk->next = head2;
        return dummy.next;
    }
};







/**
 * Modify the rotate method!!!!
 * Most of my debug time is wasted on rotateList,forget about to change the first and last node's next pointer!
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head||!head->next||!head->next->next) return;
        ListNode* mid = findMiddle(head);
        mid = rotateList(mid);
        head = mergeList(head,mid);
    }
    ListNode* findTail(ListNode* head){
        if(!head) return head;
        while(head->next){
            head = head->next;
        }
        return head;
    }
    ListNode* findMiddle(ListNode* head){
        if(!head||!head->next) return head;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* middle = slow->next;
        slow->next = NULL;
        return middle;
    }
    ListNode* rotateList(ListNode* head){
        if(!head||!head->next) return head;
        ListNode* prev = NULL;
        ListNode* next;
        while(head){
            next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }

    ListNode* mergeList(ListNode* head1,ListNode* head2){
        ListNode dummy = ListNode(-1);
        ListNode* walk = &dummy;
        while(head1&&head2){
                walk->next = head1;
                head1 = head1->next;
                walk = walk->next;
                walk->next = head2;
                head2 = head2->next;
                walk = walk->next;
        }
        if(head1) walk->next =head1;
        if(head2) walk->next = head2;
        return dummy.next;
    }
};
