#include<stdio.h>
#include<algorithm>
using namespace std;
int a[1001], n;
int Count(int s){
	int i, cnt=1, sum=0;
	for(i=1; i<=n; i++){
		if(sum+a[i]>s){
			cnt++;
			sum=a[i];
		}
		else sum=sum+a[i];
	}
	return cnt;
}
int main(){
	freopen("input.txt", "rt", stdin);
	int m, i, lt=1, rt=0, mid, res, maxx=-2147000000;
	scanf("%d %d", &n, &m);
	for(i=1; i<=n; i++){
		scanf("%d", &a[i]);
		rt=rt+a[i];
		if(a[i]>maxx) maxx=a[i];
	}
	while(lt<=rt){
		mid=(lt+rt)/2;
		if(mid>=maxx && Count(mid)<=m){	
			res=mid;
			rt=mid-1;
		}
		else lt=mid+1;
	}
	printf("%d\n", res);
	return 0;
}