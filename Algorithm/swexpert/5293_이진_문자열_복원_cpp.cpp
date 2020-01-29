// 출처 : https://organize-study.tistory.com/144

#include <iostream>
#include <string.h>
#include <string>
using namespace std;
 
string dp[21][21][21][21][2];
bool check[21][21][21][21][2];
 
void run(int aa, int bb, int cc, int dd, int bit) {
    string &ret = dp[aa][bb][cc][dd][bit];
    if (check[aa][bb][cc][dd][bit]) return;
    check[aa][bb][cc][dd][bit] = 1;
    if (aa && !bit) {
        run(aa - 1, bb, cc, dd, 0);
        if (dp[aa - 1][bb][cc][dd][0].length()) {
            ret = dp[aa - 1][bb][cc][dd][0] + "0";
            return;
        }
    }
    if (bb && bit) {
        run(aa, bb - 1, cc, dd, 0);
        if (dp[aa][bb - 1][cc][dd][0].length()) {
            ret = dp[aa][bb - 1][cc][dd][0] + "1";
            return;
        }
    }
    if (cc && !bit) {
        run(aa, bb, cc - 1, dd, 1);
        if (dp[aa][bb][cc - 1][dd][1].length()) {
            ret = dp[aa][bb][cc - 1][dd][1] + "0";
            return;
        }
    }
    if (dd && bit) {
        run(aa, bb, cc, dd - 1, 1);
        if (dp[aa][bb][cc][dd - 1][1].length()) {
            ret = dp[aa][bb][cc][dd - 1][1] + "1";
            return;
        }
    }
}
 
int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int tc, c2 = 0;
    cin >> tc;
    dp[1][0][0][0][0] = "00";
    dp[0][1][0][0][1] = "01";
    dp[0][0][1][0][0] = "10";
    dp[0][0][0][1][1] = "11";
 
    for (int t = 1; t <= tc; ++t) {
        int aa, bb, cc, dd;
        cin >> aa >> bb >> cc >> dd;
        cout << "#" << t << " ";
        run(aa, bb, cc, dd, 0);
        run(aa, bb, cc, dd, 1);
        if (dp[aa][bb][cc][dd][0].length())
            cout << dp[aa][bb][cc][dd][0];
        else if (dp[aa][bb][cc][dd][1].length())
            cout << dp[aa][bb][cc][dd][1];
        else
            cout << "impossible";
        cout << '\n';
    }
    return 0;
}
