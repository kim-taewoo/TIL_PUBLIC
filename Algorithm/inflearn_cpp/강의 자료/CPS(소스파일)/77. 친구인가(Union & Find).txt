#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
int unf[1001];

int Find(int v){
	if(v==unf[v]) return v;
	else return unf[v]=Find(unf[v]);
}

void Union(int a, int b){
	a=Find(a);
	b=Find(b);
	if(a!=b) unf[a]=b;
}

int main(){
	freopen("input.txt", "rt", stdin);
	int i, n, m, a, b, fa, fb, j;
	scanf("%d %d", &n, &m);
	for(i=1; i<=n; i++){
		unf[i]=i;
	}
	for(i=1; i<=m; i++){
		scanf("%d %d", &a, &b);
		Union(a, b);
	}
	scanf("%d %d", &a, &b);
	fa=Find(a);
	fb=Find(b);
	if(fa==fb) printf("YES\n");
	else printf("NO\n");
	return 0;
}