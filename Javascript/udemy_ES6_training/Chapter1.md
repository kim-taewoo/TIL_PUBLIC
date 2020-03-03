## Let vs Var
1. Block Scope 의 개념없이 모든 게 전역변수로 만들어졌던 Var 과 달리, Let 은 Block Scope 가 적용된다. 즉, 선언된 스코프를 벗어난 곳에서 Let 변수를 호출하려하면 에러가 발생한다.
1. Let 변수는 Hoisting 되지 않는다. 

> Hoisting : 모든 변수 선언이 파일 맨 앞쪽에서 선언된 것처럼 끌어올리는 자바스크립트 특유의 작동방식. `var age = 13` 와 같은 변수 선언이 해당 변수의 호출보다 아래에 있어도 이상없이 작동한다.

## Arrow Functions
```javascript
// 기존 함수 정의 방식
function fn() {
  console.log('Hello!');
}
// Arrow Function
var fn = () => {
  console.log('Hello!');
}
// Arrorw Function Oneliner
var fn = () => console.log('Hello!');
```

### Arrow Function 의 특이사항
1. Oneliner 로 쓸 수 있는 경우, `return` 키워드를 생략할 수 있다.
1. 매개변수가 한 개인 경우, 괄호를 생략할 수 있다. (매개변수가 0 개일 때는 빈 괄호를 써주어야 한다.)
1. 익명함수처럼 사용 가능하다.
    ```javascript
    setTimeout(() => console.log('Hello'), 1000)
    ```

## this 키워드와 Arrow Function
기존 함수 정의 방식은, 그 함수를 어디서 '호출'했냐에 따라 `this` 가 가리키는 context 가 달라진다. 그러나 Arrow Function 은 함수가 '정의' 되었던 때의 context 를 '유지' 한다(keep context). 

예를 들어 전역 스코프에 함수를 정의했다면, 기존 함수 정의 방식으로는 전역 스코프에서 그 함수를 호출했다면 `window` 객체를, 어떤 html `<button>` 에서 그 함수를 이벤트로 호출했다면 해당 버튼 객체를 출력한다. 그러나 Arrow Function 이라면 어디서 호출하든 `window` 객체를 출력한다.

## Default Parameter (매개변수 기본값)
매개변수에 기본값을 설정할 수 있다. 기본값으로 앞서 선언된 변수를 넣을 수도 있다는 걸 알고 있자!

```javascript
function isEqualTo(number = 10, compare = number) {
  return number == compare;
}
console.log(isEqualTo());
```

## Object Literal Extensions
이게 되나? 싶은 방식으로 객체를 만들 수 있다...
1. 객체를 만들 때 property name, value 를 일일이 쓰지 않아도, 외부에 이미 선언된 변수가 있다면 그 변수명을 property name 으로만 넣으면 알아서 그 변수가 가진 값을 value 로 넣어준다.
```javascript
let name = 'Josh';
let age = '27';

let obj = {
  // name : 'Josh',
  // age : 27
  name,
  age
}
```
2. object 내에 함수를 정의할 때, property name:value 형태가 아닌 형태로 곧바로 선언해도 문제없이 쓸 수 있다.
```javascript
let obj = {
  name,
  age,
  // greet : function() {}
  greet() {
    console.log(this.name + ', ' + this.age);
  }
};
obj.greet();
```
3. 심지어 함수명이 String 인 것처럼 쓸 수도 있다. (당연히 띄어쓰기도 된다.)
```javascript
let obj = {
  name,
  age,
  // greet : function() {}
  "greet me"() {
    console.log(this.name + ', ' + this.age);
  }
};
obj["greet me"]();
```
4. 동적으로 Property name 을 만들 수 있다. 즉, 어떤 변수가 담고 있는 값을 property name 으로 쓸 수 있다.
대괄호 [] 로 감싸는 문법을 쓰며, value 는 따로 써줘야 한다. 동적으로 property 를 생성하면서 다양한 방식으로 접근 가능한 유연함이 있다.
```javascript
let ageField = "age";
let obj = {
  [ageField]: 28
}
// 아래 3개 모두 가능.
console.log(obj.age)
console.log(obj["age"])
console.log(obj[ageField]);
```

## The Rest Operator
매개변수가 몇 개인지 정해지지 않은 상태일 때, 들어오는 모든 인자들을 Array 로 묶어 쓸 수 있게 해준다. 점을 3개 찍는 문법을 사용한다. `...variable`
```javascript
function sumUp(...toAdd) {
  console.log(toAdd);
  let result = 0;
  for (let i = 0; i < toAdd.length; i++) {
    result += toAdd[i];
  }
  return result;
}
console.log(sumUp(100,10,"20"));
```

## The Spread Operator
Rest Operator 의 반대. 여러 인자들을 묶어서 Array 로 만들어주는 Rest Operator 와 달리, Spread Operator 은 Array 에 담긴 원소들을 여러 개의 인자로 만들어준다. 문법은 Rest Operator 와 동일한 점 3개인데, 사용하는 장소에 따라 Rest 인지, Spread 인지 구분할 수 있다. 함수를 정의할 때 매개변수 정의에 쓴다면 Rest, 함수를 호출할 때 인자를 넣을 때 쓴다면 Spread 이다.
```javascript
let numbers = [1,2,3,4,5]
console.log(Math.max(...numbers));
```

## The for-of Loop
```javascript
let nums = [1,2,3];
for (let num of nums) {
  console.log(num);
}
```

## Template Literals
String 과 비슷해보이지만 훨씬 많은 기능을 가지고 있는 문법. 물결표시와 같이 있는 따옴표 모양을 쓴다.

기존 String 으로는 할 수 없는 멀티라인 출력이나 변수 출력이 가능하다. 만약 변수출력 문법을 그대로 출력하고 싶다면 앞에 escape character 인 백슬래쉬를 넣어주면 된다.

```javascript
let name = 'Max';
let description = `
  Hello, my name is ${name + '!!!'}
`;
console.log(description)
```

## Destructuring - Arrays
변수 선언 때 왼쪽에 대괄호를 씌운 변수를 여러 개 둠으로써 오른쪽 Array 값들을 분배할 수 있다. 
1. Rest Operator 사용이 가능하며,
2. Default value 를 설정할 수 있기 때문에
마치 함수를 쓰는 것처럼도 볼 수 있다.
```javascript
let nums = [1,2,3];
let [a,b] = nums;
console.log(a);
console.log(b);
let [a, ...b] = nums
console.log(b);
let [a='Default', b, c, d = 'Default'] = nums;
console.log(a, d)
```
Destructuring 을 응용해서 **변수 swap** 을 편하게 할 수 있다. (swap 시에는 새로 변수를 초기화하는 게 아닌 할당만 다시 함에 주의!)
```javascript
let a = 5;
let b = 10;
[b, a] = [a, b];
console.log(b, a);
```

원하는 값만을 빼오기 위해 공백으로 생략도 가능하다.
```javascript
let numbers = [1,2,3];
let [a,,c] = numbers;
console.log(a,c)
```

이미 생성된 Array 가 아니어도 곧바로 destructuring 을 쓸 수 있다.
```javascript
let [a,b] = [1,2,3];
console.log(a,b);
```

## Destructuring - Objects
Array Destructuring 과 유사하나 좀 다른 게 있다.
1. 대괄호가 아닌 중괄호를 쓰며,
1. Array 와 달리 애초에 property name 으로 접근하기 때문에 원하는 property 만을 가져오고 싶을 때 필요없는 부분이라고 공백을 둘 필요가 없다. (애초에 object 는 Array 와 달리 정해진 position 이 없다.)
1. alias 를 사용해서 기존 property name 과 똑같지 않게 가져올 수 있다. ( : 문법 사용)
```javascript
let obj = {
  name: 'Josh',
  age: 27,
  greet : function() {
    console.log('Hello');
  }
};
let {name, greet} = obj;
// let {name, greet: hello} = obj // alias hello
greet();
```

