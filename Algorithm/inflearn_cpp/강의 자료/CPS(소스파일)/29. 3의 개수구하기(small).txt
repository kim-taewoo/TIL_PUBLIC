#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	freopen("input.txt", "rt", stdin);
	int n, tmp, i, cnt=0, digit;
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		tmp=i;
		while(tmp>0){
			digit=tmp%10;
			if(digit==3) cnt++;
			tmp=tmp/10;
		}
	}
	printf("%d\n", cnt);
	return 0;
}
	


#include<stdio.h>
int res;
int main(){
	int n, i, j;
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		for(j=i; j>0; j=j/10){
			if(j%10==3) res++;
		}
	}
	printf("%d\n", res);
	return 0;
}