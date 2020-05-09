#include<stdio.h>			
int main(){
	//freopen("input.txt", "rt", stdin);
	int n, i, cnt=0, h[101], max;
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		scanf("%d", &h[i]);
	}
	max=h[n];
	for(i=n-1; i>=1; i--){
		if(h[i]>max){
			max=h[i];
			cnt++;
		}
	}		
	printf("%d\n", cnt);			
	return 0;
}