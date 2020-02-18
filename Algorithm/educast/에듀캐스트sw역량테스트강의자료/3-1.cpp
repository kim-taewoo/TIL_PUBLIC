#include <iostream>
#include <algorithm>
using namespace std;

int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

int t, n, k, res;
int input[9][9];
bool visit[9][9];


void dfs(int x, int y, int cnt, int flag) {
	visit[x][y] = true;
	if (res < cnt) res = cnt;

	for (int i = 0; i < 4; i++) {
		int ax = x + dx[i];
		int ay = y + dy[i];

		//방문했거나 범위 벗어나면 continue
		if (ax == 0 || ay == 0 || ax == n + 1 || ay == n + 1 || visit[ax][ay]) continue;

		//내리막길인 경우
		if (input[x][y] > input[ax][ay]) {
			dfs(ax, ay, cnt + 1, flag);
		}
		//내리막길이 아닌 경우
		else {
			if (input[x][y] > input[ax][ay] - k && flag) {

				int temp = input[ax][ay];

				input[ax][ay] = input[x][y] - 1;
				dfs(ax, ay, cnt + 1, 0);
				input[ax][ay] = temp; // 원상 복귀
			}
		}
	}
	visit[x][y] = false;
}

int main() {
	ios_base::sync_with_stdio(false);

	cin >> t;

	for (int tc = 1; tc <= t; tc++) {

		cin >> n >> k;
		res = 0;
		int maxCnt = 0;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				cin >> input[i][j];
				maxCnt = max(input[i][j], maxCnt);
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (input[i][j] == maxCnt) {
					//탐색
					dfs(i, j, 1, 1);
				}
			}
		}

		cout << "#" << tc << " " << res << endl;

	}
}
