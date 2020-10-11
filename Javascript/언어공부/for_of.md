# for in, for of 차이점
1. prototype chain 에 의한 iterable 을 대상으로 포함하는가?

`for in`은 iterable object라면 모두 반복의 대상이 됩니다.  
prototype chain에 의해서 Array 객체가 foo 함수를 갖기 때문에 foo함수가 반복의 대상이 된 것입니다.  
반면 `for of`는 prototype chain에 의한 프로퍼티는 신경쓰지 않습니다.  
따라서 순수한 arr배열의 원소만 출력합니다.

> for of 가 내부적으로 `hasOwnProperty` 체킹을 한다기 보다는, 애초에 구현 방식이 `someObj[Symbol.iterator]` 처럼 어떤 객체가 가진 iterator 속성에 따른 것이기 때문에 대체적으로 깊이 연관있는 것만을 iterate 하기 때문이라고 보면 된다.

2. 변수의 값이 다르다.
arr 배열의 각 원소를 임시 변수로 담을 value에는 몇 번 째 반복되고 있는지 `index`가 담겨있습니다.  
반면 `for of`에서 value에는 실제 원소의 값만 순서대로 담깁니다. 