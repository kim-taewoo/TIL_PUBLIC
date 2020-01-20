#include <iostream>

using namespace std;

int main()
{
  char str[51];
  char num_str[10];
  int idx = 0;
  int num_factors = 2;

  cin >> str;

  // for (size_t i = 0; str[i] != '\0'; i++) // 이 방식도 가능.
  for (size_t i = 0; i < 51; i++)
  {
    int e = str[i];
    if (e == '\0')
      break;

    if (e >= 48 && e <= 57)
    {
      // int num=0; 를 선언해놓고, 숫자가 추가될 때마다 * 10 해가며 키우는 게 가능하다.
      // num = num * 10 + (str[i] - 48);
      // 처음에는 0 이니까 그냥 한자리수가 되기에 완벽히 작동한다.
      // 신박하네.. 굳이 내 방식처럼 쓸데없는 배열을 만들 필요가 없다.
      // 변수 개수도 여러 개 줄일 수 있고...
      num_str[idx] = e;
      idx++;
    }
  }

  int num = atoi(num_str); // 위에 읽어보면 알겠지만 이럴 필요가 없다.

  for (size_t i = 2; i < num / 2 + 1; i++)
  {
    if (!(num % i))
    {
      num_factors++;
    }
  }

  cout << num << endl
       << num_factors << endl;

  return 0;
}