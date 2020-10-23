#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<string> solution(vector<vector<string>> tickets) {
  vector<string> answer;
  sort(tickets.begin(), tickets.end(), greater<vector<string> >());
  unordered_map<string, vector<string> > routes;
  for (int i = 0; i <tickets.size(); i++) {
    routes[tickets[i][0]].push_back(ticekts[i][1]);
  }
  vector<string> s = vector<string> {"ICN"};
  while (!s.empty()) {
    string airport = s.back();
    if (routes.find(airport) == routes.end() || routes[airport].size() == 0) {
      answer.push_back(airport);
      s.pop_back();
    } else {
      s.push_back(routes[airport].back());
      routse[airport].pop_back();
    }
  }
  reverse(answer.begin(), answer.end());
  return answer;
}