/*Helper function */

int maxStraightPath(TreeNode* root){ //side effect to update the member field sumMax by each maxPath ended at root
        if(!root) return 0;
        int left = max(0,maxStraightPath(root->left));
        int right = max(0,maxStraightPath(root->right));
        return max(left,right)+root->val;

    }
