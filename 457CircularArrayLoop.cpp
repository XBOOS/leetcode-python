/*
 * You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.
 *
 * Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
 *
 * Example 2: Given the array [-1, 2], there is no loop.
 *
 * Note: The given array is guaranteed to contain no element "0".
 *
 * Can you do it in O(n) time complexity and O(1) space complexity?
 *
 */

//Solution1
class Solution {
    public:
    bool circularArrayLoop(vector<int>& nums) {
            int n = nums.size();
            if(n<1) return false;
            int idx = 0;
            int last = 0;
            set<int> untouched;
            bool sign = nums[0]>0; //true for positive
            std::set<int>::iterator it = untouched.begin();
            for(int i=0;i<n;i++){
                        untouched.insert(it,i);
                    }

            while(!untouched.empty()){

                        if(untouched.find(idx)==untouched.end()&&idx!=last){
                                        return true;
                                    }
                        if(untouched.find(idx)==untouched.end()&&idx==last||sign!=(nums[idx]>0) ){
                                        idx = *untouched.begin();
                                        sign = idx>0;
                                        untouched.erase(untouched.begin());
                                        last = idx;
                                        continue;
                                    }

                        int step = nums[idx];
                        untouched.erase(idx);
                        last = idx;
                        idx = (idx+step) % n;
                        idx = idx>0?idx:idx+n;
                    }
            return false;
        }
};
