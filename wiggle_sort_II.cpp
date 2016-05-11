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
