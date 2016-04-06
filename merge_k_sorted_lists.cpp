/*
 * Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 */



/* Method1 Using a min-heap to store the k sorted list
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct CompareListHead{
    bool operator()(ListNode* lhs,ListNode* rhs){
        return lhs->val>rhs->val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //auto cmp = [](ListNode* head1,ListNode* head2){ return head1->val<head2->val;}
        std::priority_queue<ListNode*,vector<ListNode*>,CompareListHead> heap;
        //build the heap first
        for(ListNode* list:lists){
            if(list) heap.push(list);
        }
        ListNode dummy = ListNode(-1);
        ListNode* walk = &dummy;

        while(!heap.empty()){
            ListNode* picked = heap.top();
            walk->next = picked;
            walk = walk->next;
            heap.pop();
            picked = picked->next;
            if(picked) heap.push(picked);
        }
        return dummy.next;
    }
};

/*====================================================================
 * Method 2 divide and conquer. the time complexity is still O(Nlogk)
 *====================================================================
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct CompareListHead{
    bool operator()(ListNode* lhs,ListNode* rhs){
        return lhs->val>rhs->val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if(n==0) return nullptr;
        return mergeHelper(lists,0,n-1);
    }

    ListNode* mergeHelper(vector<ListNode*>& lists, int low,int high){
        if(low==high) return lists[low];
        int mid = (low+high)/2;
        ListNode* l1 = mergeHelper(lists,low,mid);
        ListNode* l2 = mergeHelper(lists,mid+1,high);
        //then merge the two lists l1 and l2
        ListNode dummy = ListNode(-1);
        ListNode* walk = &dummy;
        while(l1 && l2){
            if(l1->val<l2->val){
                walk->next = l1;
                l1 = l1->next;
            }else{
                walk->next = l2;
                l2 = l2->next;
            }
            walk = walk->next;
        }
        if(l1) walk->next = l1;
        if(l2) walk->next = l2;
        return dummy.next;
    }
};
