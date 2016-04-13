void duplicated_quick_select(vector<int>& nums,int low,int high,int len,vector<int>& ans){
        if(low>high) return;
        int pivot = nums[low];//or to safely get the mid and swap it with the first element
        int i = low+1, k = low, j=low+1;
        while(i<=high){
            if(nums[i]<pivot){
                swap(nums[i],nums[k++]);
                swap(nums[i++],nums[j++]);
            }else if(nums[i]==pivot){
                swap(nums[i++],nums[j++]);
            }else{
                i++;
            }
        }
//        if(j-k>len) ans.push_back(nums[k]);
//        if(k-low>len) duplicated_quick_select(nums,low,k-1,len,ans);
//        if(high-j+1>len) duplicated_quick_select(nums,j,high,len,ans);
