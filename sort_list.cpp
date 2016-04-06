/*
 *Sort a linked list in O(n log n) time using constant space complexity.
 *
 * The classic sorting methods with time complexity of O(nlogn) are
 * merge_sort,quick_sort.heap_sort
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
 * THe merge sort for array need extra linear space for merging. but here is linked list. so that it dont need to use extra space.
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


/*
 * Mathod2 Recuisive Quick sort
 * Partition + concate the small part,middle part and big part
 * Be careful to set the tail to NULL to split the list during partition!
 * and in the concate where to start the while loop.use walk->next, we can arrive at the tail of the list
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
    ListNode* sortList(ListNode* head) {
        return quickSort(head);
    }
    ListNode* quickSort(ListNode* head){
        if(!head||!head->next) return head;
        ListNode smallHead = ListNode(-1);
        ListNode midHead = ListNode(-1);
        ListNode bigHead = ListNode(-1);
        ListNode* small = &smallHead;
        ListNode* big = &bigHead;
        ListNode* mid = &midHead;
        int pivot = head->val;
        while(head){
            if(head->val<pivot){
                small->next = head;
                small = small->next;
            }else if(head->val==pivot){
                mid->next = head;
                mid = mid->next;
            }else{
                big->next = head;
                big = big->next;
            }
            head = head->next;
        }
        small->next = NULL;
        mid->next = NULL;
        big->next = NULL;
        return concate(quickSort(smallHead.next),midHead.next,quickSort(bigHead.next));
    }
    ListNode* concate(ListNode* small,ListNode* mid,ListNode* big){
        ListNode dummy = ListNode(-1);
        ListNode* walk = &dummy;
        walk->next = small;
        while(walk->next){
            walk = walk->next;
        }
        walk->next = mid;
        while(walk->next){
            walk = walk->next;
        }
        walk->next = big;

        return dummy.next;
    }
};
