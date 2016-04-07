/*
 *
 * Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
 *
 * Calling next() will return the next smallest number in the BST.
 *
 * Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
 *
 */



/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
private:
    std::stack<TreeNode*,vector<TreeNode*> > myStack;
public:
    BSTIterator(TreeNode *root) {
        while(root){
            myStack.push(root);
            root = root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return myStack.size()>0;
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* next = myStack.top();
        myStack.pop();
        TreeNode* tmp = next->right;
        while(tmp){
            myStack.push(tmp);
            tmp = tmp->left;
        }
        return next->val;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
