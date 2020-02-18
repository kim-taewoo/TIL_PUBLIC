#include<iostream>
using namespace std;
#define MAX 51

int N, M;
int input[MAX][MAX];
int x, y;
int result;
int direction;

//북, 동, 남, 서
int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

int main() {

	cin >> N >> M;
	cin >> x >> y >> direction;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> input[i][j];

	while (1) {

		// 현재위치 청소
		if (input[x][y] == 0) {
			input[x][y] = 2;
			result++;
		}

		int nextStep = 0;
		for (int i = 0; i < 4; i++) {

			// 왼쪽 방향으로 전환
			direction = (direction + 3) % 4;
			int newX = x + dx[direction];
			int newY = y + dy[direction];

			if (input[newX][newY] == 0) {
				x = newX;
				y = newY;
				nextStep = 1;
				break;
			}
		}

		if (nextStep == 1)
			continue;

		// 후진
		int newDirection = (direction + 2) % 4;
		x = x + dx[newDirection];
		y = y + dy[newDirection];

		if (input[x][y] == 1)
			break;
	}
	cout << result;
}