/*
 * Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
 *
 * Hint:
 *
 * Expected runtime complexity is in O(log n) and the input is sorted.
 *
 */

/*
 * As it is already sorted, we could use binary search to do the work
 */
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int low = 0;
        int high = n-1;
        int mid;
        while(low<=high){
            mid = (low+high)/2;
            if(citations[mid]==(n-mid)){
                return n-mid;
            }else if(citations[mid]<(n-mid)){
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
        return n-low;

    }
};
