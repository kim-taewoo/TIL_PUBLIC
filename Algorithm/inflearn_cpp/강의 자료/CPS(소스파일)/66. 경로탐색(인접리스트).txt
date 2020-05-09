#include<stdio.h>
#include<vector>
using namespace std;
int ch[30], cnt=0, n;		
vector<int> map[30];
void DFS(int v){
	int i;
	if(v==n){
		cnt++;
	}
	else{
		for(i=0; i<map[v].size(); i++){
			if(ch[map[v][i]]==0){
				ch[map[v][i]]=1;
				DFS(map[v][i]);
				ch[map[v][i]]=0;
			}
		}
	}
}			
int main(){
	freopen("input.txt", "rt", stdin);
	int m, i, a, b;
	scanf("%d %d", &n, &m);
	for(i=1; i<=m; i++){
		scanf("%d %d", &a, &b);
		map[a].push_back(b);
	}
	ch[1]=1;
	DFS(1);
	printf("%d\n", cnt);
	return 0;
}


<경로까지 출력하는 코드>
#include<stdio.h>
#include<vector>
using namespace std;	
int ch[30], cnt=0, n, path[30];
vector<int> map[30];
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
		for(i=0; i<map[v].size(); i++){
			if(ch[map[v][i]]==0){
				ch[map[v][i]]=1;
				path[L]=map[v][i];
				DFS(map[v][i], L+1);
				ch[map[v][i]]=0;
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
		map[a].push_back(b);
	}
	ch[1]=1;
	path[0]=1;
	DFS(1, 1);
	printf("%d\n", cnt);
	return 0;
}