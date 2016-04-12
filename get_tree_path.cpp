void getPath(std::stack<TreeNode*>& path,TreeNode* root, TreeNode* target){
        TreeNode* prev = nullptr;
        //actually postorder traversal//since I cannot just pop it out need to go back to parent the second time
        while(!path.empty() || root){
            if(root==target){
                path.push(root);
                return;
            }
            if(root){
                path.push(root);
                root = root->left;
            }else if((path.top()->right)==prev){
                prev = path.top();
                path.pop();
            }else{
                root = path.top();
                prev = root;
                root = root->right;
                prev = nullptr;
            }
        }
