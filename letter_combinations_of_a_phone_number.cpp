/*
 * Given a digit string, return all possible letter combinations that the number could represent.
 *
 * A mapping of digit to letters (just like on the telephone buttons) is given below.
 *
 *
 *
 * Input:Digit string "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * Note:
 * Although the above answer is in lexicographical order, your answer could be in any order you want.
 *
 */

/* Take care of the string and char relationship. Many compiling errors got there*/

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        int leng = digits.size();
        if(leng<1) return vector<string>();
        map<char,string> numToLetters = {{'1',""},{'2',"abc"},{'3',"def"},{'4',"ghi"},{'5',"jkl"},{'6',"mno"},{'7',"pqrs"},{'8',"tuv"},{'9',"wxyz"}};
        vector<string> combs;
        string comb = "";
        int digits_idx = 0;
        getCombinations(numToLetters,combs,comb,digits,digits_idx,leng);
        return combs;
    }
    void getCombinations(map<char,string>& numToLetters, vector<string>& combs,string& comb,const string& digits,int digits_idx,int leng){
        if(digits_idx>=leng){
            combs.push_back(comb);
            return;
        }

        char digit = digits[digits_idx++];
        for(char& c:numToLetters[digit]){
            comb +=c;
            getCombinations(numToLetters,combs,comb,digits,digits_idx,leng);
            comb.erase(comb.size()-1);
        }

    }
};
