/*
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 *
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 *
 * You are given a target value to search. If found in the array return its index, otherwise return -1.
 *
 * You may assume no duplicate exists in the array.
 */

/* find pivot helper function to find the pivot which divids the array to
 * two sorted arrays since it was rotated once.
 */
class Solution {
public:
//trivial linear time search, think about binary search
    int search(vector<int>& nums, int target) {
        if(nums.size()<=0) return -1;
        int pivot = findPivot(nums);
        return binarySearch(nums,target,pivot);
    }
    int findPivot(vector<int>& nums)
    {
        int mid;
        int low = 0,high = nums.size()-1;
        while(low<high)
        {
            mid =(low+high)/2;
            if(nums[mid]>nums[high])
            {
                low = mid+1;
            }
            else
            {
                high = mid;
            }
        }
        return low;
    }
    int binarySearch(vector<int>& nums,int target,int pivot)
    {
        int mid;
        int low = 0,high = nums.size()-1;
        while(low<=high)
        {
            mid = (low+high)/2;
            if(nums[(mid+pivot)%nums.size()]<target)
            {
                low = mid+1;
            }
            else if(nums[(mid+pivot)%nums.size()]>target)
            {
                high = mid-1;
            }
            else
            {
                return (mid+pivot)%nums.size();
            }
        }
        return -1;

    }
};
