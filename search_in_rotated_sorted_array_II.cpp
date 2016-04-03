/*
 * Follow up for "Search in Rotated Sorted Array":
 * What if duplicates are allowed?
 *
 * Would this affect the run-time complexity? How and why?
 *
 * Write a function to determine if a given target is in the array.
 *
 */
class Solution {
public:
//trivial linear time search, think about binary search
    int search(vector<int>& nums, int target) {
        if(nums.size()<=0) return -1;
        int low = 0;
        int high = nums.size()-1;
        int mid;
        while(low<=high)
        {
            mid = (low+high)/2;
            if(nums[mid]==target) return true;
            if(nums[mid]>nums[high])//the left side is sorted
            {
                if(target>=nums[low]&&target<nums[mid])
                {
                    high = mid-1;
                }
                else
                {
                    low = mid+1;
                }
            }
            else if(nums[mid]<nums[high])
            {
                if(target>nums[mid]&&target<=nums[high])
                {
                    low = mid+1;
                }
                else
                {
                    high = mid-1;
                }
            }
            else
            {
                //the worst case is O(n), we eradicate the duplicates one by one
                --high;
            }



        }
        return false;
    }

};
