#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string s = "";
    for (int i; i < number.length(); i++) {
        while (!s.empty() && s.back() < number[i] && k > 0) {
            s.pop_back();
            k--;
        }
        if (k == 0) {
            s += number.substr(i, number.length() - i);
            break;
        }
        s.push_back(number[i]);
    }
    return s.substr(0, s.length() - k);
}