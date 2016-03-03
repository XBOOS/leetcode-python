#include<stdio.h>
#include<string.h>
#include<assert.h>
#define maxn 3000
int f[maxn];
int main(){

    memset(f,0,sizeof(f));
    f[0] = 1;
    //mimic the manual calculation process
    int n,i,j;
    scanf("%d",&n);
    assert(n>=0);
    if(n==0) printf("%d\n",0);
    for(i=2;i<=n;i++){
        int c = 0;
        for(j=0;j<maxn;j++){
            int tmp = f[j]*i+c;
            c = tmp/10;
            f[j] = tmp%10;
        }
    }
/* this is false
    for(int i=maxn-1;i>=0;i--){
        if(f[i]) printf("%d",f[i]);

    }

 */
    int k;
    for(k=maxn-1;k>=0;k--){
        if(f[k]) break;
    }
    while(k>=0){
        printf("%d",f[k]);
        k--;
    }
    printf("\n");
    return 0;
}
