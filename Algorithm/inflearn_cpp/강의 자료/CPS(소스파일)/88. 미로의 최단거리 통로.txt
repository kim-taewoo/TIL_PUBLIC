#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
int dx[4]={-1, 0, 1, 0};
int dy[4]={0, 1, 0, -1};
int main(){
	ios_base::sync_with_stdio(false);
	freopen("input.txt", "rt", stdin);
	vector<vector<int> > board(7, vector<int>(7, 0));
	vector<vector<int> > dis(7, vector<int>(7, 0));
	queue<pair<int, int> > Q;
	for(int i=0; i<7; i++) {
		for(int j=0; j<7; j++) {
			cin>>board[i][j];
		}
	}
	Q.push(make_pair(0, 0));
	board[0][0]=1;
	while(!Q.empty()) {
		pair<int, int> tmp = Q.front();
		Q.pop();
		for(int i=0; i<4; i++) {
			int x=tmp.x+dx[i];
			int y=tmp.y+dy[i];
			if(x>=0 && x<7 && y>=0 && y<7 && board[x][y]==0) {
				Q.push(make_pair(x, y));
				board[x][y]=1;
				dis[x][y] = dis[tmp.x][tmp.y] + 1;
			}
		}
	}
	if(dis[6][6]==0) cout<<"-1";	
	else cout<<dis[6][6];
	return 0;
}