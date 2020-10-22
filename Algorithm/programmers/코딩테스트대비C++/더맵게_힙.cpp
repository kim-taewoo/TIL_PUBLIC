#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
  int answer = 0;
  priority_queue<int, vector<int>, greater<int>> pq;
  for (auto& i: scoville) pq.push(i);
  while (1) {
    int min1 = pq.top(); pq.pop();
    if (min1 >= K) break;
    else if (pq.empty()) {
      answer = -1;
      break;
    }
    int min2 = pq.top(); pq.pop();
    pq.push(min1 + 2 * min2);
    answer++;
  }
  return answer;
}