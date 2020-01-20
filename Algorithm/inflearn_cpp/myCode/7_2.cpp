#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
  char ch;
  while (cin >> ch)
  {
    if (isupper(ch)) ch = tolower(ch);
    cout << ch;
  }
  return 0;
}