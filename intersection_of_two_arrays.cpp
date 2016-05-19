/*
 * Given two arrays, write a function to compute their intersection.
 *
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
 *
 * Note:
 * Each element in the result must be unique.
 * The result can be in any order.
 */
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> numSet;
        set<int> res;
        if(nums1.size()<nums2.size()){
            numSet = set<int>(nums1.begin(),nums1.end());
            intersection_helper(nums2,numSet,res);
        }
        else{
            numSet = set<int>(nums2.begin(),nums2.end());
            intersection_helper(nums1,numSet,res);
        }
        return vector<int>(res.begin(),res.end());

    }
    void intersection_helper(vector<int>& numVec,set<int>& numSet,set<int>& res){
        for(int num:numVec){
            if(numSet.find(num)!=numSet.end()) res.insert(num);
        }
    }
};
