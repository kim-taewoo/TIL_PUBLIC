#include <iostream>
using namespace std;

int dy[101];

int dfs(int n)
{
  if (dy[n] != 0)
    return dy[n];
  if (n == 1 || n == 2)
    return n;
  return dy[n] = dfs(n - 1) + dfs(n - 2);
}

int main()
{
  ios_base::sync_with_stdio(false);
  freopen("input.txt", "rt", stdin);
  int n;
  cin >> n;
  cout << dfs(n) << endl;
  return 0;
}