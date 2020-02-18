#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int dx[] = { 0,0,-1,1 };
int dy[] = { -1,1,0,0 };

int inputMap[8][8];
int tempMap[8][8];
int n, m;
int ans = 0;



//지도 복사
void copyMap(int a[8][8], int b[8][8]) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			a[i][j] = b[i][j];
		}
	}
}

//바이러스 퍼트리기(BFS)
void BFSforVirus() {
	//AfterSpreadMap은 3개의 벽을 세운 후 바이러스가 퍼졌을 때의 연구소의 상황을 저장하는곳.
	int AfterSpreadMap[8][8];
	copyMap(AfterSpreadMap, tempMap);
	queue<pair<int, int>> q;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (AfterSpreadMap[i][j] == 2)
				q.push(make_pair(i, j));

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int newX = x + dx[i];
			int newY = y + dy[i];
			// 감염되지 않은 영역만 선택
			if (0 <= newX && newX<n && 0 <= newY && newY<m) {
				if (AfterSpreadMap[newX][newY] == 0) {
					AfterSpreadMap[newX][newY] = 2;
					q.push(make_pair(newX, newY));
				}
			}
		}
	}
	//연구소에 오염되지 않은 부분 체크.
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (AfterSpreadMap[i][j] == 0)
				cnt++;
		}
	}
	ans = max(ans, cnt);
}

// 벽을 세우는 재귀 함수 
void recursiveWall(int cnt) {
	// 종료 부, 바이러스를 퍼트려서 오염되지 않은 부분의 갯수를 확인한다.
	if (cnt == 3) {
		BFSforVirus();
		return;
	}
	//벽 세우는 부분.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (tempMap[i][j] == 0) {
				tempMap[i][j] = 1; // 해결 부, 실제로 벽을 세우는 부분
				recursiveWall(cnt + 1); // 분할 부, cnt를 ++ 시켜 벽을 세워야하는 갯수를 -1 시키면서 문제를 분할.				
				tempMap[i][j] = 0;
			}
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &inputMap[i][j]);
		}
	}
	//연구소에서 0인 부분을 모두 벽을 세워야 하므로 다음과 같이 진행.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (inputMap[i][j] == 0) {
				copyMap(tempMap, inputMap);
				tempMap[i][j] = 1;
				recursiveWall(1);
				tempMap[i][j] = 0;
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}