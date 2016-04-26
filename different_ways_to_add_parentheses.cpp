/*
 * Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
 *
 *
 * Example 1
 * Input: "2-1-1".
 *
 * ((2-1)-1) = 0
 * (2-(1-1)) = 2
 * Output: [0, 2]
 *
 *
 * Example 2
 * Input: "2*3-4*5"
 *
 * (2*(3-(4*5))) = -34
 * ((2*3)-(4*5)) = -14
 * ((2*(3-4))*5) = -10
 * (2*((3-4)*5)) = -10
 * (((2*3)-4)*5) = 10
 * Output: [-34, -14, -10, -10, 10]
 *
 */

//solution1: very clever and simple way.
//use map to hash the input->result value list to avoid recomputation
//the divide and conquer bottom case is the whole input is an integer
// Also remember the map methods and atoi(string.c_str())
class Solution {
private:
    map<string,vector<int> >inputToValues;
public:
    vector<int> diffWaysToCompute(string input) {
        map<string,vector<int> >::iterator itr;
        itr = inputToValues.find(input);
        if(itr!=inputToValues.end()){
            return itr->second;
        }
        vector<int> res;
        int num;
        for(auto i=0;i<input.size();++i){
            char c = input[i];
            vector<int> list1,list2;
            if(c=='+'||c=='-'||c=='*'){
                list1 = diffWaysToCompute(input.substr(0,i));
                list2 = diffWaysToCompute(input.substr(i+1));
                for(int left:list1){
                    for(int right: list2){
                        if(c=='+') res.push_back(left+right);
                        else if(c=='-') res.push_back(left-right);
                        else if(c=='*') res.push_back(left*right);
                        else printf("Invalid input operator!");
                    }
                }
            }
        }
        if(res.empty()) res.push_back(atoi(input.c_str()));
            inputToValues[input] = res;
            return res;
    }
};
