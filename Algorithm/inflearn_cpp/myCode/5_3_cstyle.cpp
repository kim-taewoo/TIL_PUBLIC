#include <iostream>
int main()
{
  unsigned first, second, age;
  char gender = 'M';
  scanf("%d %*c %d", &first, &second);
  unsigned generation = second / 1000000;
  unsigned year_to_add = first / 10000;

  if (generation == 1 || generation == 2)
    age = 2019 - (1900 + year_to_add) + 1;
  else
    age = 2019 - (2000 + year_to_add) + 1;
  
  if (generation % 2 == 0)
    gender = 'W';

  printf("%u %c", age, gender);

  return 0;
}