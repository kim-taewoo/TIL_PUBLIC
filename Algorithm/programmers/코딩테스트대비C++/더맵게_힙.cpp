#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
  int answer = 0;
  // 최소힙. 3번째 인자가 greater 인 이유는, greater, 즉 클수록 true 를 반환해서 왼쪽으로 정렬되는데,
  // pop 했을 때 먼저 빠져야 하는 게 제일 작은 것이어야 하기 때문에, 작은 게 오른쪽으로 가는
  // greater 로 정렬해야 한다.
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