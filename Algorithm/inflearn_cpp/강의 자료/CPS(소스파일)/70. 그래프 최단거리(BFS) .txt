#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int ch[30], dis[30];
int main(){
	freopen("input.txt", "rt", stdin);
	int n, m, a, b, x, i;
	vector<int> map[30];
	queue<int> Q;
	scanf("%d %d", &n, &m);
	for(i=1; i<=m; i++){
		scanf("%d %d", &a, &b);
		map[a].push_back(b);
	}
	Q.push(1);
	ch[1]=1;
	while(!Q.empty()){
		x=Q.front();
		Q.pop();
		for(i=0; i<map[x].size(); i++){
			if(ch[map[x][i]]==0){
				ch[map[x][i]]=1;
				Q.push(map[x][i]);
				dis[map[x][i]]=dis[x]+1;
			}
		}
	}
	for(i=2; i<=n; i++){
		printf("%d : %d\n", i, dis[i]);
	}	
	return 0;
}