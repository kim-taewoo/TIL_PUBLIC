# CHAPTER1. Syntax Changes & Additions

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

# CAHPTER3. Symbols

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