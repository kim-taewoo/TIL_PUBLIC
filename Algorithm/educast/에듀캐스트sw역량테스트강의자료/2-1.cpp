#include <stdio.h>
#include <memory.h>

int input[10][10];
int n, m, c, res;

int max(int a, int b) {
	return (a > b) ? a : b;
}

// (x,y) 좌표부터 m개의 꿀통을 선택해서 얻을 수 있는 최대 가격을 구하는 재귀 함수
void getMaxPrice(int x, int y, int cnt, int sum, int price) {
	if (sum > c) return;
	res = max(res, price);
	if (cnt == m) return;

	getMaxPrice(x, y + 1, cnt + 1, sum + input[x][y], price + input[x][y] * input[x][y]);
	getMaxPrice(x, y + 1, cnt + 1, sum, price);
}

int solve(int x, int y) {

	res = 0;
	getMaxPrice(x, y, 0, 0, 0);
	int priceA = res;

	// 두번째 사람이 고른 벌통 M개의 비용구하기
	int priceB = 0;
	int j = y + m;
	for (int i = x; i < n; i++, j = 0) {
		for (; j < n - m + 1; j++) {
			res = 0;
			getMaxPrice(i, j, 0, 0, 0);
			priceB = max(priceB, res);
		}
	}

	return priceA + priceB;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &n, &m, &c);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &input[i][j]);
			}
		}

		int maxPrice = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n - m + 1; j++) {
				maxPrice = max(maxPrice, solve(i, j));
			}
		}
		printf("#%d %d\n", tc, maxPrice);
	}
}
