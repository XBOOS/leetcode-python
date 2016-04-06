/*
 * Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
 */


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if(!head) return NULL;
        TreeNode* root;
        if(!head->next){
            root= new TreeNode(head->val);
            return root;
        }
        ListNode* middle = findMiddle(head);
        root = new TreeNode(middle->val);
        root->left = sortedListToBST(head);
        root->right = sortedListToBST(middle->next);
        return root;

    }
    ListNode* findMiddle(ListNode* head){
        if(!head||!head->next) return head;
        // if(!head->next->next){
        //     ListNode* middle = head->next;
        //     head->next = NULL;
        //     return middle;
        // }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prevSlow;
        while(fast&&fast->next){
            prevSlow = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prevSlow->next = NULL;
        return slow;
    }
};

/* Method 2 instead of spliting the original list to many sub-lists, we just
 * change the nullptr detection to A ListNode "afterLast".
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
       return sortedListToBSTHelper(head,nullptr);

    }
    TreeNode* sortedListToBSTHelper(ListNode* head,ListNode* afterLast){
        if(head==afterLast) return nullptr;
        ListNode* mid = findMiddle(head,afterLast);
        TreeNode* root = new TreeNode(mid->val);
        root->left = sortedListToBSTHelper(head,mid);
        root->right = sortedListToBSTHelper(mid->next,afterLast);
        return root;

    }
    ListNode* findMiddle(ListNode* head,ListNode* afterLast){
        if(head==afterLast||head->next==afterLast) return head;
        // if(!head->next->next){
        //     ListNode* middle = head->next;
        //     head->next = NULL;
        //     return middle;
        // }
        ListNode* slow = head;
        ListNode* fast = head;
      //  ListNode* prevSlow;
        while(fast!=afterLast&&fast->next!=afterLast){
           // prevSlow = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        //prevSlow->next = NULL;
        return slow;
    }
};

/*or just eliminate the helper function*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
       return sortedListToBSTHelper(head,nullptr);

    }
    TreeNode* sortedListToBSTHelper(ListNode* head,ListNode* afterLast){
        if(head==afterLast) return nullptr;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=afterLast&&fast->next!=afterLast){
            slow = slow->next;
            fast = fast->next->next;
        }
        TreeNode* root = new TreeNode(slow->val);
        root->left = sortedListToBSTHelper(head,slow);
        root->right = sortedListToBSTHelper(slow->next,afterLast);
        return root;

    }


};
