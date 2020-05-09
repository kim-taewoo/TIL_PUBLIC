#include<stdio.h>
int n, T[20], P[20], res=0;
void DFS(int L, int sum){
	if(L==n+1){
		if(sum>res) res=sum;
	}
	else{
		if(L+T[L]<=n+1) DFS(L+T[L], sum+P[L]);
		DFS(L+1, sum);
	}
}

int main(){
	freopen("input.txt", "rt", stdin);
	int i;
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		scanf("%d %d", &T[i], &P[i]);
	}
	DFS(1, 0);
	printf("%d\n", res);

	return 0;
}