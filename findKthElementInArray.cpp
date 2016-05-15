//utility function
//find the kth smallest element in an array iteratively
//This is different from three-way-partationing, regardless of repeated element. and also slower then the three-way-partationing if there are duplicated elements
int findKthSmallestElementInArray(vector<int>& nums, int low, int high, int k){
    while(true){
        if(low>=high) return nums[low];
        int j=low;
        int pivot = nums[high];
        //this is the hoarse partation method.
        //also we can do partattion from two ends
        for(int i=low;i<high;++i){
            if(nums[i]<=pivot){
                swap(nums[i],nums[j]);
                j++;
            }
        }
        swap(nums[j],nums[high]);
        if(j==(k-1)) return nums[j];
        else if(j>(k-1)) high = j-1;
        else low = j+1;
    }

}

int partation(vector<int>& nums, int low,int high){
    if(low>=high) return low;
    int pivot = nums[high];
    int i = low;
    int j = high;
    while(true){
        while(nums[i]<pivot) ++i;
        while(nums[j]>pivot) --j;
        if(i>=j) return j;
        swap(nums[i],swap[j]);
    }
}
