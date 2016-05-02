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

//This is used to avoid big integer overflow. The second way is to using long and stringstream
string add(string num1,string num2){
    stringtream ss;
    long tmp = atol(num1.c_str())+atol(num2.c_str());
    ss.str("");
    ss<<tmp;
    string res = ss.str();
    return res;
}
