#include<stdio.h>			
int main(){
	//freopen("input.txt", "rt", stdin);
	int n, val, i, num, cnt=0, max=-2147000000;
	scanf("%d %d", &n, &val);
	for(i=1; i<=n; i++){
		scanf("%d", &num);
		if(num>val) cnt++;
		else cnt=0;
		if(cnt>max) max=cnt;
	}
	printf("%d\n", max);		
	return 0;
}
	