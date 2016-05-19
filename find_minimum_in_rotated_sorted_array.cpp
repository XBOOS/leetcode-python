/*
 * Follow up for "Find Minimum in Rotated Sorted Array":
 * What if duplicates are allowed?
 *
 * Would this affect the run-time complexity? How and why?
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 *
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 *
 * Find the minimum element.
 *
 * The array may contain duplicates.
 *
 */

//method1 linear time complexity
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        for(int i=1;i<n;++i){
            if(nums[i]<nums[i-1]) return nums[i];
        }
        return nums[0];
    }
};


//method 2
//  this is actually even slower. But this is not all tail recursion, so that I cannot change them all to be iterative.
class Solution {
public:
    int findMin(vector<int>& nums) {
        return findMinRecur(nums,0,nums.size()-1);
    }
    int findMinRecur(vector<int>& nums,int low, int high){
        if(low>=high) return nums[low];
        int mid = (low+high)/2;
        if(nums[mid]<nums[low]) return findMinRecur(nums,low,mid);
        if(nums[mid]>nums[high]) return findMinRecur(nums,mid+1,high);
        return min(findMinRecur(nums,low,mid-1),findMinRecur(nums,mid+1,high));
    }

};
