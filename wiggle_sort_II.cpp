/*
 * Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
 *
 * Example:
 * (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
 * (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
 *
 * Note:
 * You may assume all input has valid answer.
 *
 * Follow Up:
 * Can you do it in O(n) time and/or in-place with O(1) extra space?
 *
 *
 */

//Method 1 : using nlog(n) time complexity and O(n) space complexity;
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        vector<int> copy(nums);
        std::sort(copy.begin(),copy.end());
        int idx = 1;
        for(int i=n-1;i>=0;i--){
            nums[idx] = copy[i];
            idx+=2;
            if(idx>=n&&i) idx=0;
        }
     }

};
//using different method
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        vector<int> copy(nums);
        std::sort(copy.begin(),copy.end());
        // int idx = 1;
        // for(int i=n-1;i>=0;i--){
        //     nums[idx] = copy[i];
        //     idx+=2;
        //     if(idx>=n&&i) idx=0;
        // }
        for(int i=1;i<n;i+=2){
            nums[i]=copy.back();
            copy.pop_back();
        }
        for(int i=0;i<n;i+=2){
            nums[i] = copy.back();
            copy.pop_back();
        }
     }

};

//Method2
//Explaination by stenfanPochmann, Thanks to him!!
/*
 * Solution
 *
 * Roughly speaking I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes.
 *
 * def wiggleSort(self, nums):
 *     nums.sort()
 *         half = len(nums[::2])
 *             nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
 *             Alternative, maybe nicer, maybe not:
 *
 *             def wiggleSort(self, nums):
 *                 nums.sort()
 *                     half = len(nums[::2]) - 1
 *                         nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
 *                         Explanation / Proof
 *
 *                         I put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:
 *
 *                         Example nums = [1,2,...,7]      Example nums = [1,2,...,8]
 *
 *                         Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
 *                         Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
 *                         --------------------------      --------------------------
 *                         Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
 *                         I want:
 *
 *                         Odd-index numbers are larger than their neighbors.
 *                         Since I put the larger numbers on the odd indexes, clearly I already have:
 *
 *                         Odd-index numbers are larger than or equal to their neighbors.
 *                         Could they be "equal to"? That would require some number M to appear both in the smaller and the larger half. It would be the largest in the smaller half and the smallest in the larger half. Examples again, where S means some number smaller than M and L means some number larger than M.
 *
 *                         Small half:  M . S . S . S      Small half:  M . S . S . S .
 *                         Large half:  . L . L . M .      Large half:  . L . L . L . M
 *                         --------------------------      --------------------------
 *                         Together:    M L S L S M S      Together:    M L S L S L S M
 *                         You can see the two M are quite far apart. Of course M could appear more than just twice, for example:
 *
 *                         Small half:  M . M . S . S      Small half:  M . S . S . S .
 *                         Large half:  . L . L . M .      Large half:  . L . M . M . M
 *                         --------------------------      --------------------------
 *                         Together:    M L M L S M S      Together:    M L S M S M S M
 *                         You can see that with seven numbers, three M are no problem. And with eight numbers, four M are no problem. Should be easy to see that in general, with n numbers, floor(n/2) times M is no problem. Now, if there were more M than that, then my method would fail. But... it would also be impossible:
 *
 *                         If n is even, then having more than n/2 times the same number clearly is unsolvable, because you'd have to put two of them next to each other, no matter how you arrange them.
 *                         If n is odd, then the only way to successfully arrange a number appearing more than floor(n/2) times is if it appears exactly floor(n/2)+1 times and you put them on all the even indexes. And to have the wiggle-property, all the other numbers would have to be larger. But then we wouldn't have an M in both the smaller and the larger half.
 *                         So if the input has a valid answer at all, then my code will find one.
 *
 */
//method 2
//
class Solution {
public:
    void swap(vector<int>& nums,int idx1,int idx2){
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    int partition(vector<int>&nums,int low, int high){ //without duplicates. should be randomized partition
        if(low>high) return -1;
        int pivot = nums[high];
        int left = low;
        for(int i =low;i<=high;++i){
            if(nums[i]<pivot) swap(nums,i,left);
        }
        swap(nums,i,high);
        return i;
    }
    int partition_with_duplicates(vector<int>&nums,int low, int high){ //without duplicates. should be randomized partition
        if(low>high) return -1;
        int pivot = nums[high];
        int k = low,j=low;
        for(int i =low;i<=high;++i){
            if(nums[i]<pivot){
                swap(nums,i,k);
                swap(nums,i,j);
                ++k;++j;
            }else if(nums[i]==pivot){
                swap(nums,i,j);
                ++;
            }
        }
        swap(nums,j,high);
        return k;//the first index has value==pivot
    }
    int quick_selection(vector<int>& nums, int low,int high, int k){
        if(low>high) return -1;
        int q = partition(nums,low,high);
        if(q==k) return nums[q];
        else if(q<k) return quick_selection(nums,low,q-1,k);
        else return quick_selection(nums,q+1,high,k-q);
    }
    //index mapping n=> (2n+1)%(n|1)

    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if(n<2) return;
        //find median
        int median = quick_selection(nums,0,n-1,n/2);
        for(int i=0;i<n;++i){
            if(nums[i]>=pivot) swap(i,(2*i+1)%(n|1));

        }

     }

};
