/*
 *Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
*/



class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<3) return nums.size();
        int prePrev = nums[0];
        int slow = 2;
        int fast = 2;
        for(;fast<nums.size();++fast)
        {
            if(nums[fast]!=nums[fast-1]||(nums[fast]==nums[fast-1]&&nums[fast]!=prePrev))
            {
                prePrev = nums[slow-1];
                nums[slow] = nums[fast];
                ++slow;
            }
            else{
                prePrev = nums[slow-1];

            }
        }
        return slow;
    }
};
