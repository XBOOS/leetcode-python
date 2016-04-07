/*
 *Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 For example:
 Given the following binary tree,
    1            <---
     /   \
     2     3         <---
      \     \
        5     4       <---
        You should return [1, 3, 4].
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
    vector<int> rightSideView(TreeNode* root) {
        if(!root) return vector<int>();
        std::queue<TreeNode*> queue1,queue2;
        vector<int> res;
        TreeNode* tmpNode;
        int tmp;
        queue1.push(root);
        while(!queue1.empty()||!queue2.empty()){
            if(!queue1.empty()){
                while(!queue1.empty()){
                    tmpNode = queue1.front();
                    if(tmpNode->left) queue2.push(tmpNode->left);
                    if(tmpNode->right) queue2.push(tmpNode->right);
                    tmp = tmpNode->val;
                    queue1.pop();
                }
            }else{
                while(!queue2.empty()){
                    tmpNode = queue2.front();
                    if(tmpNode->left) queue1.push(tmpNode->left);
                    if(tmpNode->right) queue1.push(tmpNode->right);
                    tmp = tmpNode->val;
                    queue2.pop();
                }
            }
            res.push_back(tmp);
        }
        return res;
    }
};
