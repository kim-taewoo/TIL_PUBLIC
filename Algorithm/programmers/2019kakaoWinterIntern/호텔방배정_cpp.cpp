#include <string>
#include <vector>
#include <map>

using namespace std;

map<long long, long long> p;

long long find(long long v) {
    if (p[v] == 0)
        return v;
    else return p[v]=find(p[v]);
}


vector<long long> solution(long long k, vector<long long> room_number)
{  

    vector<long long> answer;
    for (long long x : room_number) {
        long long y = find(x);
        answer.push_back(y);
        p[y]=y+1;
    }
    
    return answer;
}