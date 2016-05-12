/*
 * Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
 *
 * Example:
 * (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
 * (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
 *
 * Note:
 * You may assume all input has valid answer.
 *
 * Follow Up:
 * Can you do it in O(n) time and/or in-place with O(1) extra space?
 *
 *
 */

//Method 1 : using nlog(n) time complexity and O(n) space complexity;
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        vector<int> copy(nums);
        std::sort(copy.begin(),copy.end());
        int idx = 1;
        for(int i=n-1;i>=0;i--){
            nums[idx] = copy[i];
            idx+=2;
            if(idx>=n&&i) idx=0;
        }
     }

};
//using different method
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        vector<int> copy(nums);
        std::sort(copy.begin(),copy.end());
        // int idx = 1;
        // for(int i=n-1;i>=0;i--){
        //     nums[idx] = copy[i];
        //     idx+=2;
        //     if(idx>=n&&i) idx=0;
        // }
        for(int i=1;i<n;i+=2){
            nums[i]=copy.back();
            copy.pop_back();
        }
        for(int i=0;i<n;i+=2){
            nums[i] = copy.back();
            copy.pop_back();
        }
     }

};

//method 2
//
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    int partition(vector<int>&nums,int low, int high){ //without duplicates. should be randomized partition
        if(low>high) return -1;
        int pivot = nums[high];
        int left = low;
        for(int i =low;i<=high;++i){
            if(nums[i]<pivot) swap(nums,i,left);
        }
        swap(nums,i,high);
        return i;
    }
    int partition_with_duplicates(vector<int>&nums,int low, int high){ //without duplicates. should be randomized partition
        if(low>high) return -1;
        int pivot = nums[high];
        int k = low,j=low;
        for(int i =low;i<=high;++i){
            if(nums[i]<pivot){
                swap(nums,i,k);
                swap(nums,i,j);
                ++k;++j;
            }else if(nums[i]==pivot){
                swap(nums,i,j);
                ++;
            }
        }
        swap(nums,j,high);
        return k;//the first index has value==pivot
    }
    int quick_selection(vector<int>& nums, int low,int high, int k){
        if(low>high) return -1;
        int q = partition(nums,low,high);
        if(q==k) return nums[q];
        else if(q<k) return quick_selection(nums,low,q-1,k);
        else return quick_selection(nums,q+1,high,k-q);
    }
    //index mapping n=> (2n+1)%(n|1)

    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        //find median
        int median = quick_selection(nums,0,n-1,n/2);
        for(int i=0;i<n;++i){
            if(nums[i]>=pivot) swap(i,(2*i+1)%(n|1));

        }

     }

};
