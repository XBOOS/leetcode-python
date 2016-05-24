/*
 * Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
 *
 * For example, given the array [2,3,1,2,4,3] and s = 7,
 * the subarray [4,3] has the minimal length under the problem constraint.
 *
 * click to show more practice.
 *
 * More practice:
 * If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
 *
 *
 */


class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {

        int n = nums.size();
        //if(n<1) return 0;
        int i=0,j=0,res=INT_MAX,sum=0;
        while(j<n){
            sum+=nums[j];
            while(sum>=s){
                res = min(res,(j-i+1));
                sum-=nums[i++];
            }
            j++;
        }
        return res==INT_MAX?0:res;
    }
};
