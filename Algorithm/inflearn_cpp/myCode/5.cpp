#include <iostream>

using namespace std;

int main()
{
  char str[11];
  int year;
  char gender = 'M';

  cin.getline(str, 11);
  if (str[9] == '1' || str[9] == '2')
  {
    year = 1900 + (str[0] - 48) * 10 + str[1] - 48;
  }
  else
  {
    year = 2000 + (str[0] - 48) * 10 + str[1] - 48;
  }

  if (str[9] == '2' || str[9] == '4')
  {
    gender = 'W';
  }
  cout << 2019 - year + 1 << " " << gender << endl;
  return 0;
}