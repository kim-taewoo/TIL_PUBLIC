#include<stdio.h>

int T, N, M;
int input[501][501];
int visit[501][501] = { 0, };
int answer = 0;

typedef struct point {
	int x, y;
}point;

// STACK 정의
point STACK[5];
int top = -1;
point pop() {
	return STACK[top--];
}
void push(int x, int y) {
	STACK[++top].x = x;
	STACK[top].y = y;
}

// 상하좌우 dx, dy
int dArr[][4] = { { 0,1 },{ 0,-1 },{ 1,0 },{ -1,0 } };

void dfs(int n, int m, int sum, int depth) {

	sum += input[n][m];

	// 종료조건
	if (depth == 1) {
		if (sum > answer)
			answer = sum;
		return;
	}

	// stack에 추가함
	push(n, m);
	visit[n][m] = 1;

	for (int k = 0; k <= top; k++) { // STACK에 담긴 모든 원소들을 하나씩 탐색
		for (int a = 0; a < 4; a++) {  // 각 각의 STACK 원소의 상하좌우 원소 : (newX, newY)

			int newX = STACK[k].x + dArr[a][0];
			int newY = STACK[k].y + dArr[a][1];

			// 좌표 범위 검사
			if (newX >= N || newY >= M || newX < 0 || newY < 0)
				continue;

			if (visit[newX][newY] == 0)
				dfs(newX, newY, sum, depth - 1);
		}
	}

	// stack에서 삭제함
	visit[n][m] = 0;
	pop();

	return;
}

int main() {

	int temp;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {

			scanf("%d", &temp);
			input[i][j] = temp;
		}


	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {

			dfs(i, j, 0, 4);
		}

	printf("%d", answer);
}
