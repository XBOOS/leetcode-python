/*
 *
 * Given a collection of numbers that might contain duplicates, return all possible unique permutations.
 *
 * For example,
 * [1,1,2] have the following unique permutations:
 * [1,1,2], [1,2,1], and [2,1,1].
 *
 */


class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
       vector<vector<int>> res;
       vector<int> perm;
       map<int,int> numToCount;
       for(int num:nums){
           if(numToCount.find(num)!=numToCount.end()) numToCount[num]++;
           else numToCount[num]=1;
       }
       int n=nums.size();
       permute(nums,n,numToCount,res,perm,0);
       return res;
    }
    void permute(vector<int>& nums,int n, map<int,int> numToCount, vector<vector<int>>& res,vector<int>& perm,int count){
        if(count==n){
            res.push_back(vector<int>(perm));
            return;
        }
        for(map<int,int>::iterator it=numToCount.begin();it!=numToCount.end();++it){
                if(it->second==0) continue;
               perm.push_back(it->first);
               it->second--;
               permute(nums,n,numToCount,res,perm,count+1);
               perm.pop_back();
               it->second++;
           }

    }
};
