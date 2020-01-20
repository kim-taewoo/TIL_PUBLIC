#include <iostream>
#include <string>

using namespace std;

int main()
{
  char year[] = "1900";
  int age;
  char gender = 'M';
  char ch;
  int cnt = 0;
  while (cin >> ch)
  {
    if (cnt > 7)
      break;
    if (cnt == 0 || cnt == 1)
      year[cnt + 2] = ch;
    if (cnt == 7)
    {
      if (ch == '2' || ch == '4')
      {
        gender = 'W';
      }
      if (ch == '3' || ch == '4')
      {
        year[0] = '2';
        year[1] = '0';
      }
    }
    cnt++;
  }

  std::cout << 2019 - atoi(year) + 1 << " " << gender << std::endl;

  return 0;
}