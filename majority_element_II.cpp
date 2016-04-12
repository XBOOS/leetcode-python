/*
 * Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
 *
 * Hint:
 *
 * How many majority elements could it possibly have?
 * Do you have a better hint? Suggest it!
 *
 */
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return nums;
        int tmp1 = nums[0];
        int tmp2 = nums[0];
        int flag1 =1;
        int flag2 =0;
        for(int i=1;i<n;++i){
            if(nums[i]==tmp1){
                flag1++;
            }else if(nums[i]==tmp2){
                flag2++;
            }else if(!flag1){
                tmp1=nums[i];
                flag1++;
            }
            else if(!flag2){
                tmp2 = nums[i];
                flag2++;
            }
            else{
                flag1--;
                flag2--;
            }
        }
        vector<int> res;
        if(flag1&&std::count(nums.begin(),nums.end(),tmp1)>n/3) res.push_back(tmp1);
        //if(tmp2==tmp1) return res;
        if(flag2&&std::count(nums.begin(),nums.end(),tmp2)>n/3) res.push_back(tmp2);
        return res;
    }
};
