/*
 * Given two numbers represented as strings, return multiplication of the numbers as a string.
 *
 * Note:
 * The numbers can be arbitrarily large and are non-negative.
 * Converting the input string to integer is NOT allowed.
 * You should NOT use internal library such as BigInteger.
 *
 */
class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size();
        int n = num2.size();
        if(m==0) return num2;
        if(n==0) return num1;
        if(num1=="0"||num2=="0")return "0";
        int sz = m+n;
        string res(sz,'0');//initialization with the largest length
        int carry1 =0,tmp1,idx;

        for(int i=n-1;i>=0;--i){
            idx = m+i;//(m+n-1-(n-1-i))
            for(int j=m-1;j>=0;--j){
                tmp1 = (num2[i]-'0')*(num1[j]-'0')+carry1+(res[idx-(m-1-j)]-'0');
                carry1 = tmp1/10;
                res[idx-(m-1-j)] = tmp1%10+'0';
            }
            if(carry1>0){
                res[idx-m]=carry1+'0';
                carry1 = 0;
            }
        }
        if(res.size()>1&&res[0]=='0') return res.substr(1);
        else return res;
        //return res;
    }

};
