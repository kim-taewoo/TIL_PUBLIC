#include <stdio.h>
using namespace std;

int price[4]; // 각 이용권 별 요금
int dayOfMonth[13];  // 이용 계획

int minMonth[13]; // 각 달을 이용하는 데 필요한 최소 이용 금액.
int d[13];

int min(int a, int b) {
	return (a < b) ? a : b;
}

int main() {

	int tc;
	scanf("%d", &tc);

	for (int t = 1; t <= tc; t++) {
		for (int i = 0; i < 4; i++) {
			scanf("%d", &price[i]);
		}

		for (int i = 1; i <= 12; i++) {
			scanf("%d", &dayOfMonth[i]);
		}

		//min(하루요금x일수, 한달요금)
		//1~12월 월간 최소값 저장
		for (int i = 1; i <= 12; i++) {
			minMonth[i] = min(price[0] * dayOfMonth[i], price[1]);
		}

		//d[N]=N번째 날의 누적된 최소값
		for (int i = 1; i <= 12; i++) {
			d[i] = d[i - 1] + minMonth[i];
			if (i - 3 >= 0) {
				if (d[i] > d[i - 3] + price[2]) {
					d[i] = d[i - 3] + price[2];
				}
			}
		}

		// 1달권과 3달권의 이용만으로 구해낸 최소 값과 1년권을 사용했을때의 값을 비교
		if (d[12] > price[3]) {
			d[12] = price[3];
		}

		printf("#%d %d\n", t, d[12]);
	}
}