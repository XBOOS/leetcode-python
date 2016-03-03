#include<stdio.h>

int main(){
    int a,b;
    while( scanf("%d%d",&a,&b)==2){
        if(!a &&!b) return 0;
        int c=0,times=0;
        while(a>0 && b>0){
            if (a%10+b%10+c>9){
                times++;
                c = 1;
            }else{
                c = 0;
            }

            a/=10;
            b/=10;
        }
        printf("%d\n",times);
    }
    return 0;
}
