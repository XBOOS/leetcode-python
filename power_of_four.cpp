
//TLE! so looping is not ok. Tend to bit manipulation!
class Solution {
public:
    bool isPowerOfFour(int num) {
        int n=1;
        while(n<num){
           n<<=2;
        }
        return n==num;
    }
};

class Solution {
public:
    bool isPowerOfFour(int num) {
        if(!num) return false;
        while((num&3)==0) num=(num>>2);
        return num==1;
    }


};

//method 2
class Solution {
public:
    bool isPowerOfFour(int num) {
        return (num&(num-1))==0 && (num&0x55555555)!=0;
    }


};

//method 3
class Solution {
public:
    bool isPowerOfFour(int num) {
        return (num&(num-1))==0 && (num-1)%3==0;
    }


};
