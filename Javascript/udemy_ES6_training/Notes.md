# CHAPTER1. Syntax Changes & Additions

## Let vs Var
1. Block Scope 의 개념없이 모든 게 전역변수로 만들어졌던 Var 과 달리, Let 은 Block Scope 가 적용된다. 즉, 선언된 스코프를 벗어난 곳에서 Let 변수를 호출하려하면 에러가 발생한다.
1. Let 변수는 Hoisting 되지 않는다. 

> Hoisting : 모든 변수 선언이 파일 맨 앞쪽에서 선언된 것처럼 끌어올리는 자바스크립트 특유의 작동방식. `var age = 13` 와 같은 변수 선언이 해당 변수의 호출보다 아래에 있어도 이상없이 작동한다.

## const
- 한 번 정의된 변수가 가리키는 메모리 주소가 바뀌는 일이 없도록 막는다. 값 이 아닌 메모리 주소 라고 굳이 말한 이유는, const 를 쓴다고 해서 Array 나 Object 의 값을 수정하지 못하는 게 아니기 때문이다. 물론 단순 정수, 문자 같은 애초에 고정된 메모리만을 차지하는 변수면 값도 수정하지 못한다.

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

# CHAPTER2. Modules & Classes

## 작업환경 세팅
이 강의에서는 편의를 위해 Plunker 라는 웹 에디터 사용. 그러나 한글 지원도 잘 안 되고 사용도 뭔가 불편해서 vscode 에서 쓸 방법을 찾아보았다.  
[Plunker](https://plnkr.co)  
로컬 vscode 에서 node.js 와 express 에서 ES6 를 쓰기 위한 가이드는 아래 내용을 참고했다.
[가이드](https://www.freecodecamp.org/news/how-to-enable-es6-and-beyond-syntax-with-node-and-express-68d3e11fe1ab)  
위 가이드를 따라 로컬 서버환경을 구성하고, udemy 코드를 불러다 쓸 수 있게 추가적인 세팅을 하면 된다. 다만 위 글을 쓴 사람의 작업환경은 리눅스로, 윈도우 머신에서는 정상 작동하지 않는 부분이 있다. 추가적으로 `npm install cross-env` 를 하고, `package.json` 파일의 `scripts` 의 dev, prod 명령어 앞에 **cross-env** 를 붙여주어야 한다.

## Modules 기본개념
1. 변수나 함수 값을 '복사' 해서 가져오는 것이 아니라 참조만 하는 것이기 때문에, `import` 된 파일 내의 변수 값이 동적으로 바뀌면, 그 변수를 가지고 온 파일에서도 해당 변수가 가진 값은 바뀌어 있다.
1. ES6에서 모든 모듈은 무조건 **Strinct Mode** 이다. 따라서 별개로 `"use strict"` 같은 정의를 해주지 않아도 된다. 
1. 모듈은 shared 나 global 스코프를 가지지 않고 각각 별개의 스코프를 가진다. 

## import & export 문법
1. 한 파일 내에 여러 개의 `export` 를 쓸 수 있다. 다만 `export default` 는 단 한 개만 쓸 수 있다.
1. `import` 할 때 `as` 키워드를 이용해 원본 변수 or 함수명과 다른 이름으로 쓸 수 있다. 
    ```javascript
    import {keyValue as key} from 'externalFile';
    ```
1. `*` 을 이용해 모든 `export` 를 한 번에 가져올 수 있다. 이렇게 한 번에 가져올 때는 반드시 `as` 키워드로 이름을 붙여주어야 한다. 이 이름은 가져온 모든 것을 담고 있는 **object** 가 된다. 

## Class Basics
- ES5 에서도 Prototype 과 같은 Class 와 유사한 문법이 존재했지만(내부적으로 거의 동일하게 동작한다.), ES6 의 Class 문법을 통해 Class 문법이 보다 명확해지고 활용도가 좋아졌다. 

- 다른 프로그래밍 언어의 클래스처럼, 자바스크립트의 클래스도, `class` 로 정의된 블루프린트를 이용해 새로운 object 를 `new` 키워드로 찍어낼 수 있게 한다. 클래스의 메서드는 따로 `function` 키워드 없이 곧바로 정의하면 된다. (일반 object 에서도 가능했다.) Constructor 를 따로 명시해 클래스 property 를 초기화할 수 있다.

- 클래스 인스턴스의 prototype 은 해당 클래스의 프로토타입과 같다. [링크::프로토타입공부](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)

- 클래스 인스턴스의 prototype 은 자바스크립트 기본 객체의 prototype과 같지 않다. 즉 클래스마다 구분되는 prototype을 가진다.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    console.log("Hello, my name is " + this.name);
  }
}

let person = new Person();
person.greet();

console.log(person.__proto__); // [object Object]
console.log(person.__proto__ == Object.prototype); // false
console.log(person.__proto__ == Object); // false
console.log(person.__proto__ == Person.prototype); // true
console.log(person.__proto__ === Person.prototype); // true
```

## Inheritance
- 다른 언어처럼 상속이 가능하다.
- 부모와 프로토타입이 동일하지는 않다. 

```javascript
class Max extends Person {
  constructor(age) {
    super('Max'); // 부모 클래스의 constructor 를 호출
    this.age = age;
  },
  greetTwice() {
    this.greet();
    this.greet();
    // super.greet() 으로도 가능. 물론 자식 클래스에 같은 이름의 함수가 새로 정의되어 덮어 씌워진다면 this 와 super 은 다른 함수를 가리킨다.
  }
}
let max = new Max(27);
max.greetTwice();
console.log(max.__proto__ === Person.prototype); // false
console.log(person.__proto__ === Person); // false
```

## static method
클래스의 method 정의 때 앞에 `static` 키워드를 붙여 static method 를 만들 수 있다. static method 는 클래스의 instantiation 없이 쓸 수 있어, 함수의 번들을 만들기 좋다.

```javascript
class Helper {
  static logTwice(message) {
    console.log(message);
    console.log(message);
  }
}
Helper.logTwice('Logged!');
```

## Classes & Modules
- 클래스도 당연히 `export` 가능하다.

## Getters & Setters
앞에 `_` 언더스코어를 써서 property 를 private property 로 만들어 getters 와 setters 를 통해서만 조회 및 수정 가능하도록 할 수 있다. 물론 `person._name` 같이 아예 언더스코어까지 쳐서 접근하면 접근되기 때문에 진정한 캡슐화라고는 할 수 없지만, 어느정도의 틀을 제공한다.

```javascript
class Person {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name.toUpperCase();
  }

  set name(value) {
    if (value.length > 2) {
      this._name = value;
    }
    else {
      console.log("Rejected");
    }
  }
}
let person = new Person("Max");
console.log(person)
```

## Extending Built-in Objects

- Subclassing 이란, 자바스크립트 built-in 클래스를 본인의 입맛에 맞게 수정해서 쓰는 것이다.

```javascript
class ConvertableArray extends Array {
  convert() {
    let returnArray = [];
    this.forEach(value => returnArray.push('Converted!' + value));
    return returnArray;
  }
}

let numberArray = new ConvertableArray();
numberArray.push(1);
numberArray.push(2);
numberArray.push(3);

console.log(numberArray.convert());
```

# CHAPTER3. Symbols

## Basics
- 심볼이란 Number, String 과 같은 자료형(Primitive)의 일종이다.
- 심볼은 유니크하고, Not iterable 한 특징을 가지고 있다.
- 위 특징 덕분에 무언가를 실수로 덮어쓰거나 수정하는 일을 방지할 수 있다.
- 직접 접근하는 방법 외의 iterator 를 통해 출력이 안되기 때문에, meta 정보를 기입해 놓는 데 많이 쓰인다.

```javascript
// 생성시 new 가 필요 없음에 주의
let symbol = Symbol('debug'); // debug 는 그냥 이름 붙인 것일 뿐 unique id 는 따로 가진다.
console.log(symbol) // [object Symbol] {...}
console.log(symbol.toString()) // "Symbol(debug)"
console.log(typeof symbol); // "symbol"

let anotherSymbol = Symbol('debug');

console.log(symbol == anotherSymbol); // false

// 활용
let obj = {
  name: 'Max',
  [symbol]: 22 // 이전에 배운 '변수가 담고 있는 값' 으로 객체 property 를 만들 수 있는 문법
}
console.log(obj[symbol]); // 직접 접근으로는 출력가능.
```

## Shared Symbols 
- `Symbol.for()` 문법으로 유니크한 id 를 공유하는 두 개 이상의 Symbol 을 만들 수 있다. 

```javascript
let symbol1 = Symbol.for('age');
let symbol2 = Symbol.for('age');
console.log(symbol1 == symbol2); // true

let person = {
  name: 'Max',
  age: 30
};

function makeAge(person) {
  let ageSymbol = Symbol.for('age');
  person[ageSymbol] = 27;
}

makeAge(person);

console.log(person[symbol1]); // 27
// 원래라면 함수 내 변수 + 심볼(ageSymbol)이어서 접근 불가능했겠지만, 
// 바깥 스코프에 만들어 놓은 심볼 변수(symbol1 or symbol2)가 같은 심볼을 공유하고 있기 때문에 접근 가능.

console.log(person["age"]); // 30  , 이건 심볼 아님.
// object 에 "age" 라는 이름의 property 가 있어도, 심볼은 별개로 접근 가능함을 확인.
```

## Well-known Symbols
이미 정의되어 있는 심볼들이 있다.

아래 예시는 클래스 인스턴스를 출력할 때, [Object object] 대신 그 클래스명이 나오도록 심볼을 바꾸는 과정을 보여준다. 
```javascript
class Person {

}
Person.prototype[Symbol.toStringTag] = 'Person';
let person = new Person();
console.log(person); // [obejct Person] { ... }
```

어떤 default behaviour 을 덮어씌우는 함수를 작성할 수도 있다.
```javascript
let numbers = [1,2,3];
numbers[Symbol.toPrimitive] = function() {
  return 999;
}
console.log(numbers + 1); // 원래라면 "1,2,31" 같은 거야 하는데 1000.
```
더 많은 Well known symbols 에 관해서는 아래 가이드를 참고하자.  
[MDN Well known Symbols 문서](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)

# CHAPTER 4. Iterators & Generators

## Iterator Basics
- Javascript 에서 Iterateable 한 객체는(Array 등등), built-in well-known symbol 이 있다. `console.log(typeof array[Symbol.iterator])` 같은 방식으로 그 심볼의 존재유무를 확인할 수 있다.
- Array 의 `Symbol.iterator` 을 출력해보면 'function' 이라고 뜨는데, 함수임을 짐작하고 호출해보면 `[object Array iterator]` 이라고 출력된다. 이 객체는 오직 `next()` 메서드만을 가진 객체다. 이 `next()` 메서드를 호출할 때마다 Array 의 원소가 하나씩 value 값으로 사용되고, 본래 가진 개수보다 많이 `next()` 가 호출되면 `undefined` 를 마지막 value 로 종료된다. ("done" property 가 true 가 되어 종료를 알린다.)

```js
let array = [1,2,3];
let it = array[Symbol.iterator]();
console.log(it.next()); // done:false, value: 1
console.log(it.next());
console.log(it.next());
console.log(it.next()); // done:true, value: undefined
```

## Iterators in Action
- 위에서 살펴보았던 iterator 심볼 내용을 덮어씌워 내가 원하는 방식으로 객체를 순회하도록 할 수 있다. 

- 아래 예시는 기존 Array 와는 아예 관계없이 iterator를 덮어씌운 대로 for 반복문이 실행되는 모습을 보여준다. 

```javascript
let array = [1,2,3];
array[Symbol.iterator] = function() {
  let nextValue = 10;
  return {
    next: function() {
      nextValue++;
      return {
        done: nextValue > 15 ? true : false,
        value: nextValue
      }
    }
  }
}

for (let element of array) {
  console.log(element);
} // 11, 12, 13, 14, 15 출력

console.log(array); // [1,2,3]. 즉 원본이 수정된 것은 아님!
```

> 정리: iterateable 한 객체는 iterator 심볼(함수)을 가지고 있고, 그 함수는 next 라는 메서드를 가진 객체를 반환한다. 잘 덮어 씌우면 원하는대로 객체 순회 규칙을 짤 수 있다.

## Creating a custom, iterateable Object
- 위에서는 원래 iterateable 한 Array 의 iterator 를 조작했다면, 이제 평범한 객체를 iterateable 하게 만들어보자. `done` property 를 조건에 맞게 true 로 변화시켜 주어야 무한 루프에 빠지지 않는다.

```javascript
let person = {
  name: 'Josh',
  hobbies: ['Sports', 'Cooking'],
  [Symbol.iterator]: () => {
    let i = 0;
    let hobbies = this.hobbies;
    return {
      next: function() {
        let value = hobbies[i];
        i++;
        return {
          done: i > hobbies.length ? true : false;
          value: value
        };
      }
    };
  }
};

for (let hobby of person) {
  console.log(hobby);
}
```

## Generators Basics
- Generator 는 마치 위에서 배운 iterator 심볼을 따로 떼낸 것처럼 동작한다. 문법적으로는 `*` 이 붙은 함수처럼 생겼는데, `return` 대신 `yield` 를 여러 개 가지고 있고, `next()` 가 호출될 때마다 자신이 가지고 있는 `yield` 를 반환한다.

```javascript
function *select() {
  yield 'House';
  yield 'Garage';
}

let it = select();
console.log(it.next()); // done: false, value: 'House'
console.log(it.next());
console.log(it.next()); // done: true, value:undefined
```

## Generators in Action
- 앞서 말한대로, generator 는 마치 iterator 를 아웃소싱 한 것처럼 사용한다. 
- 이 방법이 좋은 이유는, yield 를 쓰는 것이 무엇을 반환할 지 관리하기 편하기 때문이다. (각 단계마다 api 호출을 하거나 db 를 쿼리하거나 등등 다양한 행동을 편하게 지정해놓을 수 있다.)

```javascript
let obj = {
  [Symbol.iterator]: gen // out-sourcing iterator
}
function *gen() {
  yield 1;
  yield 2;
}

for (let element of obj) {
  console.log(element)
}
```

- 아예 generator 만의 순회방식을 지정할 수도 있다.

```javascript
function *gen(end) {
  for (let i = 0; i < end; i++) {
    yield i;
  }
}
let it = gen(2);
console.log(it.next());
console.log(it.next());
console.log(it.next()); // undefined
console.log(it.next());
```

## throw, return
- `next` 대신 `throw` 를 써서 강제로 에러를 발생시킬 수 있다.
- `next` 대신 `return` 을 써서 강제로 값을(해당 순서의 값) 덮어씌울 수 있다.

# CHAPTER5. Promises

Promise 는 자바스크립트가 욕을 먹게 하던 주범 중 하나인 **callback 지옥** 을 벗어날 수 있게 해준다. Promise 를 쓰기 전에는 비동기(asynchronous) 작업을 처리하기 위해 *callback 함수 안에 callback 함수 안에 callback 함수 안에 callback 함수...* 같이 끊없이 파고드는 callback 함수를 작성해야 했다. 하지만 Promise 의 등장으로, 보다 간편하게 비동기 작업을 chaining 해서 쓸 수 있게 되었다. 

## Promise Basics
promise 객체가 resolve 로 넘겨준 값을 `then()` 함수의 첫번째 함수 인자에 받아다 쓴다. `then()` 함수의 두 번째 함수 인자는 reject 로 넘겨준 값을 받는다.

```javascript
let promise = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve('Done!');
    // reject('Failed!');
  } ,1500)
});

promise.then(function(value) {
  console.log(value);
}, function(value) {
  console.log(value); // reject 용
});
```

## Chaining Promises

여러 Promise 를 체이닝할 수 있고, `.catch()` 로 에러(reject) 관리도 가능하다. 

```javascript
function waitASecond(seconds) {
  return new Promise(function(resolve, reject) {
    if (seconds > 2) {
      reject("Rejected!");
    } else {
      setTimeout(function() {
        seconds++;
        resolve(seconds);
      }, 1000);
    }
  });
}

waitASecond(1)
  .then(waitASecond) // 곧바로 다른 Promise 실행토록 할 수 있음. (호출을 해놓는 게 아니라 함수를 가리키기만 하는 것임에 주의!)
  .then(function(seconds) {
    console.log(seconds);
  })
  .catch(function(error) {
    console.log(error)
  });
```

## Built-in Methods - All 과 Race
Promise 에는 유용하게 쓸 수 있는 built-in 메서드들이 있다.

1. Promise.all([promise1, promise2])
    - 배열로 받은 모든 promise 가 resolve 되면 각각의 결과값을 배열에 담아 반환하고, 하나라도 reject 되면 reject 값을 반환한다.
2. Promise.race([promise1, promise2])
    - `.all()` 과 달리, 가장 빨리 resolve 혹은 reject 된 것을 반환한다. 그 외 다른 것들이 resolve 되든 reject 되든 신경쓰지 않는다. 

```javascript
let promise1 = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve('Resolved!');
  }, 1000);
});

let promise2 = new Promise(function(resolve, reject) {
  setTimeout(function() {
    reject('Rejected!');
  }, 2000);
});

// Promise.race([promise1, promise2])
Promise.all([promise1, promise2])
  .then(function(success) {
    console.log(success);
  })
  .catch(function(error) {
    console.log(error);
  });
```

# CHAPTER6. Extensions of Built-in Objects
ES6 는 객체를 다루는 데 유용한 몇가지 방식들이 추가됐다.

## Object 관련

### Object.assign()

1. `Object.assign()` 은 여러 개의 객체를 받아 하나의 객체로 만들어준다. 
1. 만약 각 객체의 프로토타입이 다르다면(서로 다른 클래스의 인스턴스인 경우 등등), **첫번째 인자의 프로토타입**이 새로 만들어진 객체의 프로토타입이 된다. 즉, 마치 첫번째 객체에, 그 뒤 객체들을 하나씩 추가하거나 덮어씌우는 것처럼 동작한다.
1. 따라서 아예 새로운 객체에 여러 객체들을 합치고 싶은 것이면 첫번째 인자로 빈 객체를 넣어야 한다.  
`Object.assign({}, obj1, obj2);`

```javascript
// 일반 객체끼리의 통합(merge)
var obj1 = {
  a:1
}
var obj2 = {
  b:2
}
var obj = Object.assign(obj1, obj2);
console.log(obj)
// [object Object] {
  a: 1,
  b: 2
}
```

```javascript
class Obj1 {
  constructor() {
    this.a = 1;
  }
}
class Obj2 {
  constructor() {
    this.b = 2;
  }
}

var obj1 = new Obj1();
var obj2 = new Obj2();

var obj = Object.assign(obj1, obj2); // 첫번째 인자인 obj1 의 프로토타입 계승
console.log(obj.__proto__ === Obj1.prototype) // true
```

### Object.setPrototypeOf()

어떤 객체가 이미 생성된 이후에 그 객체의 prototype 을 바꿀 수 있다. `Object.create()` 라는 메서드도 있지만, `create()` 는 객체가 생성되는 시점에 설정하는 것이었다면, `setPrototypeOf()` 는 언제든 가능하다.

이걸 어디다 쓰냐 싶겠지만, 아래 예시처럼, 어떤 객체 자기자신에게 특정 property 가 없다면 그 객체의 prototype 까지 가서 더 찾아보게 되는데, 그 추가적인 검색 범위를 지정할 수 있다는 데서 유용하다.

```javascript
let person = {
};

let boss = {
  name: 'Anne'
};

console.log(person.__proto__ === Object.prototype); // true
Object.setPrototypeOf(person, boss); // person 객체의 prototype 을 boss 로 바꿈.
console.log(person.__proto__ === Object.prototype); // false
console.log(person.__proto__ === boss); // true
console.log(person.name); // 'Anne' , prototype 인 boss 까지 가서 찾아냄.
```

## Strings 관련
1. startsWith() : 시작 문자열 체크 (대소문자 구분)
    ```javascript
    let name = 'Joshua';
    console.log(name.startsWith('Jos')); // true
    ```
1. endsWith() : 끝부분 문자열 체크
1. includes() : 문자열 포함 체크 (대소문자 구분)
    ```javascript
    let name = 'Joshua';
    console.log(name.includes('sh')); // true
    ```
## Numbers 관련
1. isNan
1. isFinite
1. isInteger

## Arrays 관련
1. Array.of : 그냥 Array(5) 라고 하면, **길이**가 5이고, 원소는 undefined 로 채워진 배열을 반환한다. Array.of 를 쓰면, 괄호 안에 인자로 넣은 값들로 채워진 배열을 반환한다. (물론 그냥 [5,10,11] 같이 직접 써서 만들어도 된다.)

    ```javascript
    let array = Array.of(5,10,11);
    console.log(array); // [5,10,11]
    ```

1. Array.from : 이미 존재하는 배열을 베이스로 새로운 배열을 만들 수 있다. 어떻게 변형할지 두번째 인자에 함수를 넣는다.
    ```javascript
    let array = [10,11,12];
    let newArray = Array.from(array, val => val*2);
    console.log(newArray); // [20,22,24]
    ```

1. array.fill(value, start_index, end_index) : 이미 존재하는 배열의 원소 값을 바꾼다. 시작과 끝 인덱스를 지정하는 인자는 생략가능하고, 끝 인덱스 -1 까지 바뀐다.

1. array.find(conditional function) : 조건에 맞는 **첫번째** 원소만을 반환한다. 함수 가리키는 포인터만 넣으면 알아서 배열의 각 원소를 함수 인자로 대입하며 조건을 체크하기 때문에, 복잡한 조건 매칭 함수도 사용할 수 있다.
    ```javascript
    // 기본 사례
    let array = [10,12,15];
    console.log(array.find(val => val >= 12)); // 12

    // 유용한 활용
    var inventory = {
      {name: 'apples', quantity: 2},
      {name: 'pineapples', quantity: 5},
      {name: 'watermelons', quantity: 9},
    };
    function findWatermelon(fruit) {
      return fruit.name === 'watermelons';
    }
    console.log(inventory.find(findWatermelon)); // watermelons 객체반환
    ```

1. array.copyWithin() : 배열 안의 특정 값을 복사해 다른 인덱스에도 적용할 수 있다. 첫번째 인자는 바꾸고 싶은 인덱스, 두 번째 인자는 복사해올 원소의 인덱스를 넣는다. 옵션으로 세 번째 인자도 있으나, 사용하기 헷갈린다...

1. array.entries() : 배열의 각 원소의 인덱스와 값을 배열로 묶어서 반환하는 Iterator 를 반환한다 python 의 enumerate 와 비슷하다고 생각하면 된다.
    ```javascript
    let array = [1,2,3];
    let it = array.entries();
    for (let element of it) {
      console.log(element);
    }
    // [0, 1]
    // [1, 2]
    // [2, 3]
    ```

# CHAPTER7. Maps & Sets 
ES6 에서 새로 도입된 대표적인 객체유형들

## Maps
다른 프로그래밍 언어에서도 자주 쓰이는 key-value 쌍의 자료형으로 Map 객체를 쓸 수 있다. 

### Map 객체 생성
`set()` 을 이용하거나, 인자로 이중 배열형태로 key-value 를 넣어 Map 객체를 생성할 수 있다. 같은 key 로 또다시 Map 에 객체를 넣으면 에러가 뜨지 않고 덮어씌워진다.

```javascript
let cardAce = {
  name: 'Ace of Spades'
};
let cardKing = {
  name: 'King of Clubs'
};
// 초기화 방법 1
let deck = new Map();
deck.set('as', cardAce);
deck.set('kc', cardKing);

// 초기화 방법 2
let deck = new Map([['as', cardAce],['kc', cardKing]]);
```

### Map 객체 사용법
1. map.size: 가지고 있는 원소 개수 반환
1. map.get(key): 해당 키의 값 반환. 없다면 undefined 반환
1. map.delete(key): 해당 키를 가진 쌍 삭제.
1. map.keys() 활용해 키 순회하기
    ```javascript
    for (key of map.keys()) {
      console.log(key);
    }
    ```
1. map.values() 활용해 값 순회하기
    ```javascript
    for (value of map.values()) {
      console.log(value);
    }
    ```
1. map.entries() 활용해 배열 행태의 [키, 값] 순회하기 (사실 `.entries()` 없이 그냥 Map 자체를 돌려도 같은 결과가 나온다.)
    ```javascript
    for (entry of map.entries()) {
      console.log(entry);
    }
    ```

## WeakMap
WeakMap 은 key 로 오직 reference type 만이 허용되는 특별한 형태의 Map 이다. 이런 객체를 만들어 쓰는 이유는 Garbage Collector 와 관련이 있다. key 가 reference type 이면, 자바스크립트 코드를 실행할 때 사용되지 않는 key-value 는 garbage collector 가 알아서 삭제해서 효율성을 높일 수 있다. reference type 의 키의 메모리 길이를 확정지을 수 없기 때문에 일반 Map 객체처럼 loop 을 도는 것은 불가능하다.

## Sets
유니크한 값만을 가지고 있는 collection 객체다.  
아래와 같은 메서드를 가지고 있다.
1. add(val) : val 추가하기
1. delete(val) : val 삭제. 없어도 에러가 발생하진 않는다.
1. clear() : 모두 비우기
1. has(val) : val 이 있는지 확인.
1. 이외에도 Map 객체처럼 keys, values, entries() 도 있지만 Set 을 위한 것이라기 보단 비슷한 구현구조를 가진 흔적으로 보인다.

```javascript
let set = new Set([1,1,1]);
set.add(2);
for (element for set){
  console.log(element); // 1, 2
}
```

## WeakSet
WeakMap 과 마찬가지로 오직 reference type 만이 허용되는 객체 유형이다. 사용되지 않는 객체를 Garbage Collector 가 제거할 수 있도록 한다. 다만 reference type 이기에 `let obj1 = {a:1}` 같이 따로 객체를 변수에 저장해서 key 로 쓰지 않으면 `{a:1} !== {a:1}` 임에 유의하자.