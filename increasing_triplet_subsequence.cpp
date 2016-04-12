/*
 * Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
 *
 * Formally the function should:
 * Return true if there exists i, j, k
 * such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
 * Your algorithm should run in O(n) time complexity and O(1) space complexity.
 *
 * Examples:
 * Given [1, 2, 3, 4, 5],
 * return true.
 *
 * Given [5, 4, 3, 2, 1],
 * return false.
 *
 */

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        if(n<3) return false;
        std::vector<int> memory;
        int pos = 0;
        for(int num:nums){
            pos = findPosition(memory,num);
            if(pos==2) return true;
            else if(pos>=memory.size()){
                memory.push_back(num);
            }else{
                memory[pos] = num;
            }

        }
        return false;

    }
    int findPosition(vector<int>& memory,int& target){
        int pos = memory.size()-1;
        while(pos>=0&&memory[pos]>=target){
            pos--;
        }
        return pos+1;
    }
};
