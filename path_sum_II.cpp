/*
 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        onePath(root,sum,res,path);
        return res;
    }

    void onePath(TreeNode* root, int remainSum, vector<vector<int>>& res, vector<int>& path){
        if(!root) return;
        path.push_back(root->val);
        if(!root->left&&!root->right&&remainSum==root->val){
            res.push_back(vector<int>(path));
        }
        onePath(root->left,remainSum-root->val,res,path);
        onePath(root->right,remainSum-root->val,res,path);
        path.pop_back();

    }
};
