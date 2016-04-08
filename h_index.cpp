/*
 *Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

 According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

 For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
 *
 */
/* Method1 sorting*/
class Solution {
public:
    int hIndex(vector<int>& citations) {
        std::sort(citations.begin(),citations.end(),std::greater<int>());
        int n = citations.size();
        for(int i=0;i<n;++i){
            if(citations[i]<i+1){
                return i;
            }else if(citations[i]==i+1){
                return i+1;
            }
        }
        return n;
    }
};

/*Method2 Bucket sort behind.when the num is related to the index.O(n)*/
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> bucket(n+1,0);
        for(int cita:citations){
            // if(cita>=n){
            //     bucket[n]++;
            // }else{
            //     bucket[cita]++;
            // }
            bucket[std::min(cita,n)]++;
        }

        int sum=0;
        for(int i=n;i>0;--i){
            sum+=bucket[i];
            if(sum>=i) return i;
        }
        return 0;
    }
};

