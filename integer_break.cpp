/*
 * Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
 *
 * For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
 *
 * Note: you may assume that n is not less than 2.
 *
 * Hint:
 *
 * There is a simple O(n) solution to this problem.
 * You may check the breaking results of n ranging from 7 to 10 to discover the regularities.
 *
 *
 */

//A false solution!!! 8=>18 instead of 16!. 3 is a special number it seems, except for 4=2+2
class Solution {
public:
    int integerBreak(int n) {
        if(n==2) return 1;
        if(n==3) return 2;
        return helper(n);
    }
    int helper(int n){
        if(n<=4) return n;
        if(n&1==1) return helper(n/2)*helper((n+1)/2);
        else return pow(helper(n/2),2);
    }
};

//the right solution!
class Solution {
public:
    int integerBreak(int n) {
        if(n==2) return 1;
        if(n==3) return 2;
        int res = 1;
        while(n>3&&n!=4){
            res*=3;
            n-=3;
        }
        return res*n;
    }
};
