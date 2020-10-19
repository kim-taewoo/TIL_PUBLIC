#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int num1, int num2) {
    string str1 = to_string(num1) + to_string(num2);
    string str2 = to_string(num2) + to_string(num1);
    return str1 > str2;
}

string solution(vector<int> numbers) {
    string answer = "";
    sort(numbers.begin(), numbers.end(), cmp);
    for (auto& i: numbers) answer += to_string(i);
    return answer[0] == '0' ? "0" : answer; // 여기 주의! 반환해야 될 건 string 타입이다.
}