#include <iostream>
#include <limits>
// #include <fstream>

using namespace std;
int main()
{
  int n, m, max = 0, min = numeric_limits<int>::max();

  // 파일 입력 방법 1. freopen // C-style
  freopen ("4_input.txt", "rt", stdin); // redirects stdin (cin 포함)
  // if (!cin)
  // {
  //   cerr << "Cannot open the file" << endl;
  //   exit(1);
  // }

  // 파일 입력 방법 2. ifstream
  // ios_base::sync_with_stdio(false);
  // ifstream cin("4_input.txt");
  // if (!cin)
  // {
  //   cerr << "Cannot open the file" << endl;
  //   exit(1);
  // }
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> m;
    min = min > m ? m : min;
    max = max < m ? m : max;
  }
  cout << max - min << endl;
  return 0;
}