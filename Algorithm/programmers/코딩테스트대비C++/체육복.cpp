#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> u(n+2, 1);
    for (auto& i:reserve) u[i]++;
    for (auto& i:lost) u[i]--;
    for (int i = 1; i <= n; i++) {
        if (u[i] == 2 && u[i-1] == 0) {
            u[i] = u[i-1] = 1;
        } else if (u[i] == 2 && u[i+1] == 0) {
            u[i] = u[i+1] = 1;
        }
    }
    for (int i = 1; i <= n; i++) {
        if (u[i] >= 1) answer++;
    }
    return answer;
}