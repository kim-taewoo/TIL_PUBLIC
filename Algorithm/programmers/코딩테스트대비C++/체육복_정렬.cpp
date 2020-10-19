#include <vector>
#include <set>
#include <unordered_set>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
  unordered_set<int> l(lost.begin(), lost.end()); // l 변수에 잃어버린 사람들을 순서 없이 집어넣기. map 과 달리 set 은 그냥 key 만 집어넣는 느낌이다. 
  set<int> r; // 여분을 가져온 아이들은 정렬해서 집어넣고 싶기에 unordered 안 쓴다. 
  for (auto& x: reserve) {
    // l 에 들어있다면 잃어버리기도 한, 빌려줄 수 없는 사람이 된다.
    // 아래에서 l.find() 가 l.end() 와 같다는 건, 찾지 못했다는 뜻이 된다. 즉, 여분이 남은 사람
    if (l.find(x) == l.end()) r.insert(x);
    else l.erase(x);
  }
  for (auto& x : r) {
    if (l.find(x-1) != l.end()) l.erase(x-1);
    else if (l.find(x+1) != l.end()) l.erase(x+1);
  }
  return n - l.size();
}