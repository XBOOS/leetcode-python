/*
 * Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *     3
 *        / \
 *          9  20
 *              /  \
 *                 15   7
 *                 return its zigzag level order traversal as:
 *                 [
 *                   [3],
 *                     [20,9],
 *                       [15,7]
 *                       ]
 *
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int> > res;
        if(root==nullptr) return res;
        stack<TreeNode*> stack1;
        stack1.push(root);
        stack<TreeNode*> stack2;
        TreeNode* tmp;
        while(!stack1.empty()||!stack2.empty()){
            if(!stack1.empty()){
                vector<int> level;
                while(!stack1.empty()){
                    tmp = stack1.top();
                    if(tmp->left) stack2.push(tmp->left);
                    if(tmp->right) stack2.push(tmp->right);
                    stack1.pop();
                    level.push_back(tmp->val);
                }
                res.push_back(level);
            }else{
                vector<int> level;
                while(!stack2.empty()){
                    tmp = stack2.top();
                    if(tmp->right) stack1.push(tmp->right);
                    if(tmp->left) stack1.push(tmp->left);
                    stack2.pop();
                    level.push_back(tmp->val);
                }
                res.push_back(level);
            }
        }
        return res;
    }
};
