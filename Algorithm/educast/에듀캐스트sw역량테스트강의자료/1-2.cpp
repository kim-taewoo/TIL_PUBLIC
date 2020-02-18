#include<cstdio>
int N, M, H, minCnt = 9999999, map[31][11];

// 자기 자신과 매칭되는 사다리인지 판단하는 함수
bool checkLadder() {
	for (int i = 1, pos; i <= N; i++) {
		pos = i;
		for (int j = 1; j <= H; j++) {
			if (map[j][pos] == 1)    pos++;
			else if (map[j][pos - 1] == 1) pos--;
		}
		if (i != pos) return false;
	}
	return true;
}


// 재귀함수 : (x, y) 부터 사다리를 추가하여 사다리 개수의 최소값을 구함, cnt는 현재 추가된 사다리 개수
void func(int cnt, int x, int y) {

	// 불필요한 탐색을 탈출하는 조건 (가지치기, 백트래킹)
	if (cnt >= minCnt) return;

	// 종료 부
	if (checkLadder()) {
		minCnt = cnt;
		return;
	}
	if (cnt == 3) return;


	for (int i = y; i <= H; i++, x = 1)
		for (int j = x; j < N; j++) {
			if (map[i][j]) {
				j++;
				continue;
			}

			map[i][j] = 1; // 사다리 추가, 해결 부
			func(cnt + 1, j + 2, i); //분할 부
			map[i][j] = 0;
		}
}
int main() {
	scanf("%d%d%d", &N, &M, &H);
	for (int i = 0, a, b; i < M; i++) {
		scanf("%d%d", &a, &b);
		map[a][b] = 1;
	}
	func(0, 1, 1);
	if (minCnt>3) printf("-1");
	else printf("%d", minCnt);
	return 0;
}
