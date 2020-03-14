## Types
- `typeof` 는 항상 string 자료형으로 결과를 반환한다.
- `typeof null` 은 obj 이다. (언어 설계상 실수.)
- `null` 과 `undefined` 의 차이점은, `null` 은 **의도적**으로 비어있는 값이라고 명시할 때 쓰고, `undefined` 는 선언은 됐는데 값이 할당되지 않았을 때 자동으로 초기화되는 값이다. 
- Primitive Values 빼고는 자바스크립트 내 다른 모든 건 OBJCET 이다.

## Type conversion
Number() 로 형변환 했을 때, `null` 은 0 이지만 `undefined` 는 NaN 이다.

- `toFixed(n)` : 소수점 표시 자리 n 까지

## Type coersion
int + string 이면 string 으로 형변환되어 더해진다. (계산 없이 그냥 서로 붙음.)

## Math
### Math.random();
기본범위가 0부터 1사이의 값이기 때문에, 1부터 20 사이의 정수 랜덤을 원하면 아래처럼 수정해서 써야 한다.

```javascript
let val = Math.floor(Math.random() * 20 + 1)

console.log(val);
```
## String Methods

- .indexof(val) : 찾는 문자가 있다면 그 문자의 index 값을, 없다면 -1 반환
- .charAt(index) : 해당 인덱스에 있는 값 변환. 불가능한 인덱스라면 빈 문자열 반환
- .substring(start_index, end_index) : end_index 까지의 부분 문자열 반환 (end_index - 1 까지)
- .slice(start_index, end_index) : .substring 과 유사하나, slice 는 음수값을 넣으면 뒤에서부터도 자르는 것이 가능하다.

## Array Methods

### .sort(func)
Array 와 Obj 에서 쓰이는 .sort() 메서드는 기본적으로 모든 원소가 string 이라 간주하고, 맨 앞 문자부터 ASCII 순서를 기준으로 오름차순 정렬한다. 숫자의 크기 순서대로 정렬하거나 object 정렬은 .sort() 내에 어떻게 sort 할 지 compare function 을 작성해주어야 한다. 

첫 번째 인수가 두 번째 인수보다 작을 경우 음수가 반환되고, 첫 번째 인수가 두 번째 인수보다 클 경우 양수가 반환된다. 내림차순으로 하려면 - 부호를 붙여주면 된다. 
```javascript
const numbers = [5,1,2,19,3];
let val = numbers.sort(function(x,y) {
  return x - y;
}); // 오름차순
console.log(val)
let val = numbers.sort(function(x,y) {
  return -(x - y);
}); // 내림차순
console.log(val)
```

object 의 정렬은 아래 사이트를 참고해 보자.
> [참고블로그](http://dudmy.net/javascript/2015/11/16/javascript-sort/)

### .find(func)
.find(func) 는 func 의 조건에 맞는 값을 가진 첫번째 원소 값을 반환한다.

```javascript
const numbers = [10,55,32,52]
function over50(num) {
  return num > 50;
}
let val = numbers.find(over50);
console.log(val)
```

## Date
Date 의 타입은 object (const 로 선언해도 변경가능.)

1. date.getMonth() : 월. 0 부터 센다는 것 주의! 1월이 0 이다.
1. date.getDate() : 일. 이건 0부터 세지 않는다.
1. date.getDay() : 요일. 일요일을 0으로 잡고 증가.
1. date.getFullYear() : 연도.
1. date.getHours() : 시.
1. date.getMinutes() : 분.
1. date.getSeconds() : 초.
1. date.getMilliseconds() : 밀리초.
1. date.getTime() : 타임스탬프. 1970.1.1 부터의 시간경과

위 메서드의 get 을 set 으로 바꾸면 set 하는 메서드가 된다.

## Comparison Operators
`===` 로 비교해야 Type 까지 비교한다.

## Mouse Events

### `mouseenter`, `mouseleave` 와 `mouseover`, `mouseout` 의 차이점
`mouseenter`, `mouseleave` 는 해당 이벤트가 걸린 element 에 들어갈 때와 나갈 때 한 번씩만 발생하지만, `mouseover` 과 `mouseout` 은, 해당 element 의 자식 element 에 마우스가 진입하면, 전체적으로 봤을 때는 여전히 원래 element 안이라도 out 되고 자식 element 에서 나올 때 또다시 over 된다. 

## AJAX
Asynchronous Javascript XML 의 약자지만, 사실 요즘은 XML 을 거의 안 쓰고 JSON 을 쓴다..

## Fetch API
- Fetch 는 Axios 같은 외부 라이브러리와 달리, http error 를 자동으로 `.catch()` 로 넘겨주지 않는다. 따라서 수동으로 에러를 발생시켜 주어야 한다. http error 를 처리하는 전용함수를 만들어 쓰는 게 좋다.

    ```javascript
    fetch('https://example.com')
      .then(res => res.json())
      .then(res => {
        if (!res.ok) {
          throw new Error(res.error);
        }
        return res;
      })
      .catch(err => console.log(error));

    // 에러 처리 함수 만들기
    function handleError(res) {
      if (!res.ok) throw new Error(res.error);
      return res;
    }
    fetch('https://example.com')
      .then(res => res.json())
      .then(handleError)
      .then(res => console.log(res.data))
      .catch(err => console.log(err));
    ```


## Regex
1. i : `/regex/i` 처럼 정규표현식 슬래쉬 뒤에 i 를 붙이면 case insensitive, 즉 대소문자 구분을 안 하게 된다.
1. ^ : 원래 ^ 는 ^ 다음에 오는 문자로 시작해야 한다는 의미이지만, **대괄호 안**에 들어가면 대괄호 안에 있는 문자여선 안된다는 의미가 된다. (대괄호 안 문자들의 여집합)
1. {min_num, max_num} : quantifier 라고 부르며, 이 앞에 있는 문자가 몇번 반복되어야 하는지 숫자를 지정할 수 있다. 숫자를 하나만 넣으면 그 수만큼 반복되어야 한다는 뜻이 되고, 콤마를 중심으로 두 개를 넣으면 최소 반복, 최대 반복 수가 된다. 콤마만 찍고 뒤 숫자를 넣지 않으면, {최소 반복, 무한} 의 의미가 된다.
1. () : grouping

### Shorthand Character Classes :
역슬래쉬 (\\) 로 시작하는 정규식 기호.

1. `/\w/` : Word Characters (알파벳 혹은 언드스코어 _)
1. `/\w+/` : + 기호는 one or more 을 의미한다.
1. `/\W/` : 대문자 W 는 Non-Word Characters 를 뜻한다. 특수기호 등을 걸러낸다.
1. `/\d/` : digits, 숫자
1. `/\D/` : Non-digits
1. `/\s/` : whitespace
1. `/\S/` : non-whitespace
1. `/Hell\b/i` : Word Boundary. 왼쪽 예시의 경우, Hell 만을 걸러낼 뿐 Hello 는 걸러내지 않는다. 단어에 포함된 것이 아니라 그 단어 자체가 모두 일치할 때만 걸러내도록 하는 정규표현식.

### Assertions
1. `re = /x(?=y)/` : y 가 x 뒤에 있는 경우에만 걸러냄.
1. `re = /x(?!y)/` : y 가 x 뒤에 없는 경우에만 걸러냄.