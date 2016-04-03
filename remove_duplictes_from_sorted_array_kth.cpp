/*
 * A generalized version of remove duplicates from sorted array
 */

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 2;// allow k duplicates
        if(nums.size()<=2) return nums.size();
        int slow = k;
        for(int fast=k;fast<nums.size();++fast)
        {
            if(nums[fast]!=nums[slow-k])
                nums[slow++] = nums[fast];
        }
        return slow;
    }
};
