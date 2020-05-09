#include<stdio.h>
using namespace std;
int cnt[50001];
int main(){
	//freopen("input.txt", "rt", stdin);
	int n, i, j;
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		for(j=i; j<=n; j=j+i){
			cnt[j]++;
		}
	}
	for(i=1; i<=n; i++){
		printf("%d ", cnt[i]);
	}
	return 0;
}