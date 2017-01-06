
//TLE! so looping is not ok. Tend to bit manipulation!
class Solution {
public:
    bool isPowerOfFour(int num) {
        int n=1;
        while(n<num){
            n>>2;
        }
        return n==num;
    }
};
