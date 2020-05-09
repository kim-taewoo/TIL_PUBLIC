
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
int a[11], n, m, cnt=0;
void DFS(int L, int sum){
	if(L==n+1){
		if(sum==m){
			cnt++;
		}
	}
	else{
		DFS(L+1, sum+a[L]);
		DFS(L+1, sum);
		DFS(L+1, sum-a[L]);
	}
}

int main(){
	freopen("input.txt", "rt", stdin);
	int i;
	scanf("%d %d", &n, &m);
	for(i=1; i<=n; i++){
		scanf("%d", &a[i]);
	}
	DFS(1, 0);
	if(cnt==0) printf("-1\n");
	else printf("%d\n", cnt);
	return 0;
}



<경로출력코드>
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
int a[11], n, m, cnt=0, path[10];
void DFS(int L, int sum){
	if(L==n+1){
		if(sum==m){
			cnt++;
			for(int i=1; i<L; i++){
				printf("%d ", path[i]);
			}
			puts("");
		}
	}
	else{
		path[L]=a[L];
		DFS(L+1, sum+a[L]);
		path[L]=0;
		DFS(L+1, sum);
		path[L]=-a[L];
		DFS(L+1, sum-a[L]);
	}
}

int main(){
	freopen("input.txt", "rt", stdin);
	int i;
	scanf("%d %d", &n, &m);
	for(i=1; i<=n; i++){
		scanf("%d", &a[i]);
	}
	DFS(1, 0);
	if(cnt==0) printf("-1\n");
	else printf("%d\n", cnt);
	return 0;
}