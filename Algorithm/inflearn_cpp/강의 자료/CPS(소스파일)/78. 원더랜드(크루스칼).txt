#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
int unf[10001];

struct Edge{
	int s;
	int e;
	int val;
	Edge(int a, int b, int c){
		s=a;
		e=b;
		val=c;
	}
	bool operator<(const Edge &b)const{
		return val<b.val;
	}
};

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
	//freopen("input.txt", "rt", stdin);
	vector<Edge> Ed;
	int i, n, m, a, b, c, cnt=0, res=0;
	scanf("%d %d", &n, &m);
	for(i=1; i<=n; i++){
		unf[i]=i;
	}
	for(i=1; i<=m; i++){
		scanf("%d %d %d", &a, &b, &c);
		Ed.push_back(Edge(a, b, c));	
	}
	sort(Ed.begin(), Ed.end());
	for(i=0; i<m; i++){
		int fa=Find(Ed[i].s);
		int fb=Find(Ed[i].e);
		if(fa!=fb){
			res+=Ed[i].val;
			Union(Ed[i].s, Ed[i].e);
		}
	}
	printf("%d\n", res);
	return 0;
}