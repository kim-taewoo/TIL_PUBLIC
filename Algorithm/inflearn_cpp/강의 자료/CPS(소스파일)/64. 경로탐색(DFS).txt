
#include<stdio.h>	
int map[30][30], ch[30], cnt=0, n;
void DFS(int v){
	int i;
	if(v==n){
		cnt++;
	}
	else{
		for(i=1; i<=n; i++){
			if(map[v][i]==1 && ch[i]==0){
				ch[i]=1;
				DFS(i);
				ch[i]=0;
			}
		}
	}
}
				
int main(){
	freopen("input.txt", "rt", stdin);
	int m, i, j, a, b, c;
	scanf("%d %d", &n, &m);
	for(i=1; i<=m; i++){
		scanf("%d %d", &a, &b);
		map[a][b]=1;
	}
	ch[1]=1;
	DFS(1);
	printf("%d\n", cnt);
	return 0;
}




<경로도 함께 출력하는 코드>
#include<stdio.h>	
int map[30][30], ch[30], cnt=0, n, path[30];
void DFS(int v, int L){
	int i, j;
	if(v==n){
		cnt++;
		for(j=0; j<L; j++){
			printf("%d ", path[j]);
		}
		puts("");
	}
	else{
		for(i=1; i<=n; i++){
			if(map[v][i]==1 && ch[i]==0){
				ch[i]=1;
				path[L]=i;
				DFS(i, L+1);
				ch[i]=0;
			}
		}
	}
}
				
int main(){
	freopen("input.txt", "rt", stdin);
	int m, i, j, a, b, c;
	scanf("%d %d", &n, &m);
	for(i=1; i<=m; i++){
		scanf("%d %d", &a, &b);
		map[a][b]=1;
	}
	ch[1]=1;
	path[0]=1;
	DFS(1, 1);
	printf("%d\n", cnt);
	return 0;
}
