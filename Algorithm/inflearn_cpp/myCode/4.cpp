#include <iostream>
#include <limits>
using namespace std;
int main()
{
  int n, m, max = 0, min = numeric_limits<int>::max();
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