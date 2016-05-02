/* Additive number is a string whose digits can form additive sequence.
 *
 * A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
 *
 * For example:
 * "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
 *
 * 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
 * "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
 * 1 + 99 = 100, 99 + 100 = 199
 * Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
 *
 * Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
 *
 * Follow up:
 * How would you handle overflow for very large input integers?
 */

//Method1 iterative solution. Becareful of the integer overflow. So need to use atol instead of atoi and need stringstream to change long back to string
class Solution {
public:

    bool isAdditiveNumber(string num) {
        if(num.size()<3) return false;

        for(int i=1;i<=num.size()/2;++i){//representing length
            for(int j=1;j<=(num.size()-i)/2;++j){
                string num1 = num.substr(0,i);
                string num2 = num.substr(i,j);
                string num3 = num.substr(i+j);
               // printf("%d%d",i,j);
                if(helper(num1,num2,num3)) return true;
            }
        }
        return false;
    }

    bool helper(string num1, string num2,string num3){
        if((num1.size()>1&&num1[0]=='0')||(num2.size()>1 && num2[0]=='0')) return false;
        long tmp = atol(num1.c_str())+atol(num2.c_str());
        stringstream ss;
        ss<<tmp;
        string num =ss.str();

        if(num==num3){
            return true;
        }else if(num==num3.substr(0,num.size())){
            return helper(num2,num,num3.substr(num.size()));
        }else{
            return false;
        }
    }
};

//Method 2 this is the iterative way . The idea is the same as the recursive way.
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        string num1,num2,num3,other;
        stringstream ss;
        for(int i=1;i<=n/2;++i){
            for(int j=1;j<=(n-i)/2;++j){
                num1 = num.substr(0,i);
                num2 = num.substr(i,j);
                other = num.substr(i+j);
                if((num1.size()>1&&num1[0]=='0')||(num2.size()>1&& num2[0]=='0')) continue;
                while(true){
                    long tmp = atol(num1.c_str())+atol(num2.c_str());
                    //printf("%d----%d %d %d ...",count,atol(num1.c_str()),atol(num2.c_str()),tmp);
                    ss.str("");
                    ss<<tmp;
                    num3 = ss.str();
                    if(num3==other) return true;
                    else if(num3 == other.substr(0,num3.size())){
                        num1 = num2;
                        num2 = num3;
                        other = other.substr(num3.size());
                        continue;
                    }else break;
                }
            }
        }
          return false;
    }
};

//What if i dont use stringstream to do the addition??
//the above method is " long tmp = atol(num1.c_str())+atol(num2.c_str()); stringstream ss;ss<<tmp;string num3 = ss.str(); "
//if reusing the same stringstream, flush it by setting ss.str(""). remember that the clear() is used to clear the error state
//flushing has no meaning for stringstream, as there is no external device that it sends data to.
//Based on your use case, you want to empty the stringstream, that's done by calling str(""))
/*
 * #include <iostream>
 * #include <sstream>
 * using namespace std;
 * int main()
 * {
 *     stringstream x;
 *         x << "abc";
 *             x.str("");
 *                 x << "def";
 *
 *                   cout << x.str() << '\n';   // it's either .str()
 *                       cout << x.rdbuf()  << '\n'; // or rdbuf()
 *        }
 *))
 */
class Solution {
public:
    string add(string a,string b){
        int m = a.size();
        int n = b.size();
        int sz = m>n?m:n;
        a = string(sz-m,'0')+a;
        b = string(sz-n,'0')+b;
        int carry=0,tmp; //here carry! must be initialized!!!!!!!
        string res = b;
        for(int i=sz-1;i>=0;--i){
            tmp = a[i]-'0'+(b[i]-'0')+carry;
            carry = (tmp>9);
            //printf("%d",carry);
            res[i] = tmp-carry*10+'0';
        }
        if(carry>0) res = '1'+res;
        return res;
    }

    bool isAdditiveNumber(string num) {
        int n = num.size();
        string num1,num2,num3,other;
        //stringstream ss;
        for(int i=1;i<=n/2;++i){
            for(int j=1;j<=(n-i)/2;++j){
                num1 = num.substr(0,i);
                num2 = num.substr(i,j);
                other = num.substr(i+j);
                if((num1.size()>1&&num1[0]=='0')||(num2.size()>1&& num2[0]=='0')) continue;
                while(true){
                    //long tmp = atol(num1.c_str())+atol(num2.c_str());

                    //ss.str("");
                    //ss<<tmp;
                    //num3 = ss.str();
                    num3 = add(num1,num2);
                    //printf("%d %d %d...",atol(num1.c_str()),atol(num2.c_str()),atol(num3.c_str()));
                    if(num3==other) return true;
                    else if(num3 == other.substr(0,num3.size())){
                        num1 = num2;
                        num2 = num3;
                        other = other.substr(num3.size());
                        continue;
                    }else break;
                }
            }
        }
          return false;
    }
};
