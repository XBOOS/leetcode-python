/*
 * Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
 *
 * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
 *
 *         _______3______
 *                /              \
 *                    ___5__          ___1__
 *                       /      \        /      \
 *                          6      _2       0       8
 *                                   /  \
 *                                            7   4
 * For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 *
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root||!p||!q) return root;
        if(root==p||root==q) return root;
        if(dfs(root->left,p)){
            if(dfs(root->left,q)) return lowestCommonAncestor(root->left,p,q);
            else return root;
        }else{
            if(dfs(root->right,q)) return lowestCommonAncestor(root->right,p,q);
            else return root;
        }
    }
    bool dfs(TreeNode* root,TreeNode* target){
        if(!root||!target) return false;
        if(root==target) return true;
        return dfs(root->left,target)||dfs(root->right,target);
    }
};
