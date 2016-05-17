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
