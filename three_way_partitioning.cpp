/*
 * The implementation of three way partationing, array version of Dutch flag problem!
 * partition the elements into three groups.
 */

void threeWayPartation(vector<int>& nums, int low, int high,int pivot){
    int i=low;//bound of the smaller part
    int j=0;// current element in attention
    int k = high; //bound of the bigger part
    while(j<=k){
        if(nums[j]<pivot){
            swap(nums[i],nums[j]);
            i++;
            j++;
        }else if(nums[j]>pivot){
            swap(nums[j],nums[k]);
            k--;
        }else{
            j++;
        }
    }
}
//can see that the i is the first element of the middle part (if any)
//i< j only when a middle element is encountered!
