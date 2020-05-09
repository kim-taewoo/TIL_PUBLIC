#include<stdio.h>
int n, r, ch[20];

void dfs(int s, int L){
	int i, j;
	if(L==r){
		for(j=0; j<L; j++){
			printf("%d ", ch[j]);
		}
		printf("\n");
	}
	else{
		for(i=s; i<n; i++){
				ch[L]=i;
				dfs(i+1, L+1);
		}
	}
}

int main(){
	scanf("%d %d", &n, &r);
	dfs(0, 0);
	return 0;
}