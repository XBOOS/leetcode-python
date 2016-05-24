/*
 * Given a non-empty array of integers, return the k most frequent elements.
 *
 * For example,
 * Given [1,1,1,2,2,3] and k = 2, return [1,2].
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 *
 */

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> counts;
        map<int,int>::iterator itor;
        for(int num:nums){
            if(counts.find(num)!=counts.end()) counts[num]++;
            else counts[num]=1;
        }

        vector<int> res(k,0);
        vector<int> resCount(k,INT_MIN);

        for(itor=counts.begin();itor!=counts.end();++itor){
            int num = itor->first;
            int count=itor->second;
            //binary search
            int idx = binarySearch(resCount,0,k-1,count);
            //printf("idx = %d, num = %d, count= %d \n",idx,num,count);
            if(idx<k){
                for(int i=k-1;i>idx;--i){
                    res[i]=res[i-1];
                    resCount[i] = resCount[i-1];
                }
                res[idx] = num;
                resCount[idx] = count;
            }
        }
        return res;
    }
    int binarySearch(vector<int>& nums,int low,int high,int target){
        //if(low>=high) return high;
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]<target) high=mid-1;
            else low = mid+1;
        }
        return low;

    }
};
