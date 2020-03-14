# FUCNTIONAL PROGRAMMING BASICS IN ES6

> [참고영상:"Functional Programming Basics in ES6"](https://youtu.be/FYXpOjwYzcs)

자바스크립트의 가장 큰 특징 중 하나는 **First class functions** 이다. 쉽게 말하면, 모든 함수는 다른 일반적인 객체처럼 *first class citizen* 이고, 따라서 함수도 변수에 저장되거나, 인자로 전달되거나, `return` 될 수 있다. 이 유연한 특징 덕분에 OOP 뿐 아니라 Functional Programming 방식으로 자바스크립트를 사용할 수 있다. (어떻게 생각하면 반OOP 세력이라고 볼 수 있다. 클래스 사용보다 explicit 하게 함수들을 공개하는 스타일을 더 좋아한다.)
> [참고글:"An Introduction to First-Class Functions"](https://medium.com/launch-school/javascript-weekly-an-introduction-to-first-class-functions-9d069e6fb137)

- Functional programming 은, 
    1. Predictable
    1. Safe
    1. Transparent
    1. Modular

1. 배열이 Immutable 함을 보장하고자 `Object.freeze()` 같은 메서드를 사용한다.

## CLOSURES 를 이용한 Encapsulation
함수가 함수를 리턴할 수 있는 자바스크립트의 유연함을 이용해 작은 pure 함수들을 레고블록을 쌓듯이 쌓아 쓰면, 깔끔한 코드를 작성할 수 있다. (Higher order 함수를 작은 조각들로부터 쌓아올린다.)  

함수를 리턴함으로써 계산은 미뤄지지만, 더 큰 계산을 위한 블럭조각처럼 이용될 수 있다. 

아래 예시에서, `createAdder(3)` 이라는 함수를 실행시키면 **x** 매개변수 자리를 closing 한다. 즉, 계산에 사용할 인자 중 하나가 '변화(mutate)'될 여지를 차단(close) 하는 Closure 이 이용되었다. 
```javascript
const createAdder = (x) => {
  return (y) => x + y;
};
const add3 = createAdder(3);
add3(2) === 5;
add3(3) === 6;
```

### 좀 더 실용적인 예제

아래 일반적인 request 를 덜 반복적으로 개선해보자.
```javascript
const request = (options) => {
  return fetch(options.url, options)
    .then(response => response.json());
};

// 아래 두 개의 요청이 Repetitive 하다. 
const usersPromise = request({
  url: '/users',
  headers: {'X-Custom': 'mykey'}
});

const tasksPromise = request({
  url: '/tasks',
  headers: {'X-Custom': 'mykey'}
});
```

개선본은 다음과 같다.
```javascript
const request = (options) => {
  return fetch(options.url, options)
    .then(response => response.json());
};

const createRequester = (options) => {
  return (otherOptions) => {
    return request(Object.assign(
      {}, options, otherOptions
    ));
  };
};

const customRequest = createRequester({
  headers: {'X-Custom': 'mykey'}
});

const usersPromise = customRequest({url:'/users'});
const tasksPromise = customRequest({url:'/tasks'});
```

## FIRST CLASS CLOSURES - Foundation for Higher Order Patterns

### Partial Application
위 두 예시는 모두 매개변수 중 하나를 확정짓는 역할을 하기에 `partial` 이라는 함수로 통일할 수 있다. 

```javascript
const add = (x,y) => x + y;
const add3 = partial(add, 3);
add3(2) === 5;
```

```javascript
const request = (defaults, options) => {
  options = Object.assign({}, defaults, options);

  return fetch(options.url, options)
    .then(response => response.json());
};

const customRequest = partial(request, {
  headers: {'X-Custom': 'mykey'}
});

const usersPromise = customRequest({url: '/users'});
const tasksPromise = customRequest({url: '/tasks'});
```

그럼 이 `partial` 이라는 함수를 어떻게 만들어야 할지 보자.
```javascript
// 첫번째 방법
const partialFromBind = (fn, ...args) => {
  return fn.bind(null, ...args);
};
// .bind 는 함수를 pre-configure 하는 메서드다. 첫번째 인자는 그 함수 내에서 *this* 가 될 객체고, 두번째 인자부터는 그 함수의 인자다.

// 두번째 방법
const partial = (fn, ...args) => {
  return (...otherArgs) => {
    return fn(...args, ...otherArgs)
  };
};
```

### CURRYING
위의 `partial` 함수조차도 따로 작성하지 않고 그냥 원하는 인자의 개수를 다 받을 때까지 실행하지 않다가 개수가 만족되면 결과를 반환하게 할 수 있다.

> Currying : Creating a copy of a function but **with** some preset parameters 

```javascript
const add = x => y => x + y;
const add3 = add(3);
add3(2) === 5;

// ES5 version currying
function add(x) {
  return function(y) {
    return x + y;
  };
}


const request = defaults => options => {
  options = Object.assign(
    {}, defaults, options
  );

  return fetch(options.url, options)
    .then(resp => resp.json());
}


// default 옵션인 headers 는 미리 받아놓고
const customRequest = request({
  headers: {'X-Custom':'mykey'}
});
// endpoint 를 추가로 받아서 실행시키는 customRequest 함수
const usersPromise = customRequest({url:'/users'});
const tasksPromise = customRequest({url:'/tasks'});
```

## PIECING IT TOGETHER
좀 더 실무에 쓸법한 building blocks 예시를 만들어 보자.  
아래는 쇼핑몰에서 쓸법한 함수 블럭들이다.

```javascript
// 적용할 함수, 적용당할 배열을 순차적으로 받아 mapping
const map = fn => array => array.map(fn);
// Tax 계산에 응용될 곱셈함수블럭
const multiply = x => y => x * y;
const pluck = key => object => object[key];

// 곱할 값을 미리 인자로 넣어두기.
const discount = multiply(0.98); // 할인용
const tax = multiply(1.0925); // 세금계산용

const request = defaults => options => {
  options = Object.assign(
    {}, defaults, options
  );
  return fetch(options.url, options)
    .then(resp => resp.json());
}

const customRequest = request({
  headers: {'X-Custom' : 'mykey'}
});

/*

[
  {price: 5},
  {price: 10},
  {price: 3},
]
*/
customRequest({url: '/cart/itmes'})
  .then(map(pluck('price')))
  .then(map(discount))
  .then(map(tax));
```

마지막 부분 코드를 보면, customRequest 의 Promise 가 Resolve 되면, *price* property 를 가진 객체의 배열이 주어지고, `map` 함수는 `pluck('price')` 를 그 배열에 mapping 한다. 그리고 순차적으로 discount 와 tax 를 또 배열에 mapping 한다.

## COMPOSING CLOSURES
위 방식처럼 여러번 `map` 으로 iteration 하는 것도 아깝다면, `composing closures` 기법을 이용할 수 있다. 직접 구현하는 것보다는 lodash, flow 등 다양한 라이브러리에 구현되어 있는 걸 쓰곤 한다. 위 예시를 single iteration 으로 처리하는 코드는 다음과 같다.

```javascript
customRequest({url:'/cart/items'})
  .then(map(
    compose(
      tax,
      discount,
      pluck('price')
    )
  ));
```

## Recursion 으로 looping 문제 처리하기.
Functional programming 은 계속해서 어떤 객체의 상태를 변화시키며 task 를 진행하는 looping 을 좋아하지 않지만, looping 이 꼭 필요한 문제가 있다면 recursion 을 이용한다. 에를 들어 factorial 문제를 일반적인 loop 을 이용해서 푼다면 다음과 같다.
```javascript
const factorial = (n) => {
  let result = 1;
  while (n > 1) {
    result *= n;
    n--;
  }
  
  return result;
};
```
functional programming 의 취지에 맞게 보다 declarative 하게 팩토리얼 문제를 푼다면 다음과 같다.
```javascript
const factorial = (n) => {
  if (n < 2) {
    return 1;
  }

  return n * factorial(n-1);
};
```

그런데 재귀의 특성상 깊이가 깊어질수록 일반적인 스택사이즈인 1MB 를 넘어버려서 문제를 해결할 수 없어진다. 이 문제를 해결하기 위해 **TAIL CALL OPTIMIZATION(ES2015)** 를 이용할 수 있다.  
위 예시에서 `return` 문을 살펴보면, `return` 문의 `n *` 는  `factorial(n-1);` 이 다 해결되기만을 기다렸다가 반환한다. 즉, 함수 콜 스택 사이즈는 커져갈 수밖에 없다. 아래와 같이 수정해주면, 다 해결되기 기다리지 않고 값을 누적해서 계산해 인자에 넣어줌으로써 스택이 쌓야면 가는 것을 줄일 수 있다. 

```javascript
const factorial = (n, accum = 1) => {
  if (n < 2) {
    return accum;
  }

  return factorial(n-1, n * accum);
};
```

# Practical Functional Promgramming in Jaascript

> [참고영상](https://youtu.be/zeZOPB9uxdE)

```javascript
function add(a,b) {return a + b;}
var mAdd = memoize(add);
mAdd(2,3) === 5 // add() called
mAdd(1,3) === 4 // add() called
mAdd(2,3) === 5 // add() **Not** called
```

# 유인동 - ES6+ 비동기 프로그래밍과 실전 에러 핸들링

> [참고영상](https://youtu.be/o9JnT4sneAQ)

