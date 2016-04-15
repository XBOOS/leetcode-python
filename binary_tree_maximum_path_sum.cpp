/*
 * Given a binary tree, find the maximum path sum.
 *
 * For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
 *
 * For example:
 * Given the below binary tree,
 *
 *        1
 *       / \
 *      2   3
 * Return 6.
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
/* The main point is to avoid recomputation.
 * The fist time I seperate the straight path from top to bottom (like backtracking) and the maxPathSum computation apart. Which actually casued my recomputing
 * the straight path so I got TLE
 *
 * Divide and conquer-- the combing part is essential!---> the combination process should use the already-computated result of the divided sub-problem part
 */
#include <climits>
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if(!root) return 0;
        if(!root->left &&!root->right) return root->val;
        int curve = INT_MIN;
        int straight = 0;
        maxPathBottomUp(root,curve,straight);
        return curve;
    }
    void maxPathBottomUp(TreeNode* root, int& curve,int&straight){
        if(!root){
            curve = 0;
            straight = 0;
            return;
        }
        int leftCurve=INT_MIN,leftStraight=0,rightCurve=INT_MIN,rightStraight=0;
        if(root->left){
            maxPathBottomUp(root->left,leftCurve,leftStraight);
        }
        if(root->right){
            maxPathBottomUp(root->right,rightCurve,rightStraight);
        }
        curve = leftCurve>rightCurve?leftCurve:rightCurve;
        curve = curve>(leftStraight+root->val+rightStraight)?curve:(leftStraight+root->val+rightStraight);
        straight = (leftStraight>rightStraight? leftStraight:rightStraight)+root->val;
        straight = straight>0?straight:0;
    }
};
