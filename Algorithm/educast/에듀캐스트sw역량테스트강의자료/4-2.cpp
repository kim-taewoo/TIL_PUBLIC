#include<iostream>
#include<vector>
#include<queue>
using namespace std;

vector<pair<int, int>> people;
vector<pair<int, int>> stair;

int N;
int board[10][10] = { 0, };

int mappingTable[10];
int answer;
int peopleCnt;

int getTime() {
	int t = 0;
	int chk = 0;
	int d[10];
	queue<int> c[2];

	for (int i = 0; i < peopleCnt; i++) {
		d[i] = abs(people[i].first - stair[mappingTable[i]].first) + abs(people[i].second - stair[mappingTable[i]].second);
	}

	while (true) {
		if (t >= answer) return t;

		if (chk == peopleCnt) return t;

		//계단에 들어간 경우
		for (int i = 0; i < 2; i++) {
			int cs = c[i].size();
			for (int j = 0; j < cs; j++) {
				int top = c[i].front();
				c[i].pop();
				top--;
				if (top != 0)
					c[i].push(top);
				else {
					chk++;
				}
			}
		}

		// 입구에 도착한 경우
		for (int i = 0; i < peopleCnt; i++) {
			if (t == d[i]) {
				if (c[mappingTable[i]].size()<3)//계단 입구 도착시 사람이 아무도 없다면
					c[mappingTable[i]].push(board[stair[mappingTable[i]].first][stair[mappingTable[i]].second]);
				else {
					c[mappingTable[i]].push(board[stair[mappingTable[i]].first][stair[mappingTable[i]].second] + c[mappingTable[i]].front());
				}
			}
		}
		t++; // 시간 증가

	}

}

void recursive(int cnt) {

	// 종료부
	if (cnt == people.size()) {
		int tmp = getTime();
		if (answer > tmp) answer = tmp;
		return;
	}

	// 분할부
	mappingTable[cnt] = 0; recursive(cnt + 1);
	mappingTable[cnt] = 1; recursive(cnt + 1);

}

int main() {

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		cin >> N;
		people.clear();
		stair.clear();
		for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
			cin >> board[i][j];
			if (board[i][j] == 1) people.push_back({ i,j });
			else if (board[i][j] > 1) stair.push_back({ i,j });
		}
		peopleCnt = people.size();
		answer = 99999999;
		recursive(0);
		cout << "#" << test_case << ' ' << answer << '\n';

	}
	return 0;