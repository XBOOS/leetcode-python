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

/*Method 2
 * combine the pivot and search processes, since they all need to get the
 * middle value.
 * the to compare the middle value with start/end,we got the sorted side
 * and compare the target with the two extreme values,we got the next search subarray.
 */
class Solution {
public:
//trivial linear time search, think about binary search
    int search(vector<int>& nums, int target) {
        int low = 0,high = nums.size()-1;
        int mid;
        while(low<=high)
        {
            mid= (low+high)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]>nums[high])//the left side is sorted
            {
                if(target>=nums[low]&& target<nums[mid])
                {
                    high = mid-1;
                }
                else{
                    low = mid+1;
                }
            }
            else// if(nums[mid]<nums[high])//the right side is sorted
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
        }
        return -1;
    }
};
