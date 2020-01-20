#include <iostream>
#include <regex>
#include <string>

// 시간초과 뜸.
using namespace std;

int main()
{
  // regex re("([0-9]{2})[0-9]+ - ([0-9])"); // regex_search() 사용시
  regex re("([0-9]{2})[0-9]+ - ([0-9])[0-9]+");
  smatch matches;
  string str;
  int year = 1900;
  char gender = 'M';

  getline(cin, str);
  regex_match(str, matches, re);

  if ((matches[2]) == '3' || matches[2] == '4')
  {
    year = 2000 + stoi(matches[1]);
  }
  else
  {
    year = year + stoi(matches[1]);
  }
  int age = 2019 - year + 1;

  if (matches[2] == '2' || matches[2] == '4')
  {
    gender = 'W';
  }

  cout << age << " " << gender << endl;

  return 0;
}