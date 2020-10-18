# 해시

`std::unordered_map` 은 *O(1)* 이지만 `std::map` 은 *O(logN)* 임을 알고 있어야 한다. 언뜻 보기에는 `map` 이 해시 테이블 자료형인 것 같지만, 사실 내부적으로 바이너리 서치 트리를 사용하고 있기 때문에 `unordered_map` 을 사용해야 한다.

## C++ STL std::unordered_map

```c++
#include<unordered_map>
// <키, 값> 의 자료형 기재
std::unordered_map<string, int> d;
// 존재하지 않는 키에 대한 값은 해당 자료형의 기본값으로 인식한다.
// 예를 들어 int 면 0, 문자열이면 빈 문자열로 본다.
cout << d["leo"] << endl;
d["leo"] = 3; // 값 없데이트
cout << d["leo"] << endl;

// `auto` 키워드를 사용하면 순회를 하는 데 알맞은 자료형을 추론한다.
// 아래의 경우에는 `pair` 로 인식할 것이다.
for (auto& i:d)
  cout << i.first << "-" << i.second << endl;
```
