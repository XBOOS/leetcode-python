/*
 * Write a function that takes a string as input and returns the string reversed.
 *
 * Example:
 * Given s = "hello", return "olleh".
 *
 */

//Method 1
class Solution {
public:
    string reverseString(string s) {
        string res;
        for(char& c:s){
            res=c+res;
        }
        return res;
    }
};

//method 2
class Solution {
public:
    string reverseString(string s) {
        int n = s.size();
        int i=0,j=n-1;
        while(i<j){
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            ++i;--j;
        }
        return s;
    }
};
