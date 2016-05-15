/*
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Determine if you are able to reach the last index.
 *
 * For example:
 * A = [2,3,1,1,4], return true.
 *
 * A = [3,2,1,0,4], return false.
 *
 */


class Solution {

public:
    bool canJump(vector<int>& nums) {
        //backtracking
        int n = nums.size();
        vector<bool> isPossible(n,false);
        isPossible[n-1] = true;
        int closest = n-1;
        for(int i=n-2;i>=0;--i){
            if(nums[i]>=(closest-i)){ isPossible[i]=true; closest = i;}
        }

        return isPossible[0];
    }
    // bool canJump(vector<int>& nums) {
    //     //backtracking . too slow, since the best algorithm here is greedy algorithm
    //     int n = nums.size();
    //     vector<bool> isPossible(n,false);
    //     vector<bool> visited(n,false);
    //     return helper(nums,0,n,visited,isPossible);
    // }
    bool helper(vector<int>& nums,int idx,int n,vector<bool>& visited,vector<bool>& isPossible){
        if(visited[idx]) return isPossible[idx];
        visited[idx]=true;
        if(idx>=n-1||(nums[idx]+idx>=n-1)){ isPossible[idx] = true; return true;}
        for(int i=1;i<=nums[idx];++i){
            if(helper(nums,idx+i,n,visited,isPossible)){isPossible[idx]=true;return true;}
        }
        isPossible[idx]=false;
        return false;
    }
};
