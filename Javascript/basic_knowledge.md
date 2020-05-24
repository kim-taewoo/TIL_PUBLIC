## 기본 지식

1. `let` 은 block scope, `var` 은 function scope. 즉, `var` 변수는 `if` 나 `for` 문 내에서 선언되어도 그 밖에서 접근 가능하다.
1. `var` 은 hoisted 된다.
1. `const` 와 `let` 의 차이는 `const` 는 값의 재할당이 불가능하단 것이다. `const` 는 반드시 변수 선언시점에 초기화까지 진행해야만 에러가 발생하지 않는다.

1. `==`, `===` 의 차이는 `==` 는 값만 비교하고 `===` 는 형변환까지 해서 type 까지 비교한다.
1. `null` 과 `undefined` 는 둘 다 빈 값을 의미하지만, `undefined` 는 자바스크립트가 자동으로 배정해주는 것이라면 `null` 은 개발자가 직접 비었다고 명시해주는 값이다. 또 이것은 언어 설계상 실수지만, `typeof undefined` 는 "undefined" 이지만, `typeof null` 은 "object" 이다.

1. `instanceof` 는 연산자다. 따라서 `newCar instanceof Car` 같이 쓴다.

1. `Object.freeze()`, `Object.seal()`. 뒤에건 수정은 가능. 앞에건 추가 수정 모두 불가. 

특정 property 의 수정만 막고 싶다면, 
`Object.defineProperty(profile, 'age', {
  value: 3,
  writable: fale
})`
같은 메서드를 사용해야 한다.

`freeze` 됐는지의 여부를 `Object.isFrozen(object)` 로 Boolean 값으로 받아볼 수 있다. `isSealed()` 로 `seal` 여부도 체크 가능하다.

## Tricky Questions

1. `console.log([] + [])` === ""
   - 설명: number 나 string 이 아닌 것들끼리 `+` 더하기 연산자로 더하면, 먼저 string 으로 형변환해서 더하게 된다. 배열의 string 형 변환은 빈 문자열이기 때문에 결과는 빈 문자열이 된다.
1. `console.log({1:2,2:3} + {2:4,3:5})` === "[object Object][object object]"
   - 설명: 위와 마찬가지의 이유로 문자열로 형변환되고, 객체의 형변환은 위와 같다.
1. ```javascript
    function hello(name){
      return `hello ` + name 
    }
    console.log(hello `taewoo`);
   ````
      - 위와 같은 코드의 결과물은 `hello taewoo` 이다.. `tagged template string` 이라는 개념으로, 함수 바로 옆 template string 은 인자로 취급된다.
1. ```javascript
    const x = 'constructor';
    console.log(x[x](01)); // "1"
   ```
      - 'constructor' 라는 string 객체에서 'constructor' 를 찾는데, 본래 'constructor' 는 그 객체를 생성할 때 쓰인 함수이므로, 결국 'string' 형변환 함수다. 즉, 01 을 string 형변환한 1 이 출력된다. 



1. `console.log(Math.max());` 의 출력값은 '-infinity' 이다. 왜냐하면 값을 비교하기 위한 초기값이 -infinity 인데, 그것과 비교할 값들을 주지 않았기 때문에, 초기값이 그대로 출련된다. 

## 약간 깊이 있는 질문들

### This 키워드

When the context and scope of program changes, this at that particular point changes accordingly.

1. global context 에서는 브라우저에서는 `window`, nodejs 에서는 `process` 가 되겠지

1. call, apply, bind 같은 메서드를 쓰지 않는다면, 일반 함수에서의 `this` 역시 `window` 다. 부모의 scope 가 자식에게 상속되기 때문. 다만 Object, 객체 내에서는 객체 자기 자신을 가리킨다. 

```javascript
var person = {
    name: "Stranger",
    age: 24,
    get identity() {
        return {who: this.name, howOld: this.age};
    }
}
person.identity; // returns {who: "Stranger", howOld: 24}
```

자신이 현재 속해있는 스코프를 지칭하는 것으로, 쉽게 생각하면, 그냥 . 앞에 있는 거라고 생각하면 된다. 글로벌 스코프이면, `window.` 이니까 window 가 this 가 된다. 글로벌 스코프가 전체 집이라고 생각하면, 어떤 객체는 하나의 방이라고 생각할 수 있다. 방 안에 있는 것에 접근하려면 `window.room.xx` 같이 한 단계를 더 써줘야 하는거겠지? `xx`가 속한 곳이 `room` 이므로, `xx`의 this 는 `room` 일 것이다. 

### What is a closure and how do you use it?

**A closure is a function that returns another function and wraps data.** The above string generator qualifies for a closure. The index value is preserved between multiple function calls. The internal function defined can access the variables defined in the parent function. This is a different scope. If you defined one more function in the second level function, that can access all parent’s variables.
JavaScript Scope can throw a lot of problems at you! understand it thoroughly

"Closures are nothing but FUNCTIONS WITH PRESERVED DATA"
어떤 함수가 다른 함수를 반환할 때, 그 반환되는 함수는, 자신이 필요한 모든 환경 변수들을 다 가지고 있다는 것. 이 특성을 이용해, 함수형 프로그래밍이 가능하다. 함수를 자기가 원하는 값을 지닌 것으로 커스텀 해서 체이닝해서 쓸 수 있는 것이다.

### what is prototype base inheritance?

모든 객체는 `prototype` 라고 불리는 property 를 가지고 있다. 그 프로토타입에 메서드나 property 를 추가할 수 있다. 어떤 객체로부터 `new` 키워드로 새로운 객체를 만들면, 부모 객체의 property 를 상속받는데, 그 자식 객체 자신의 property 에 직접 포함하는 방식이 아닌, 부모 프로토타입에 있는 것을 참조로 사용한다.

#### Understand Prototypical Inheritance well
In traditional JavaScript, there is the concept of inheritance in a camouflage. It is by using a technique of prototyping. All the new class syntax you see in ES5, ES6 is just a **syntactical sugar coating** for the underlying prototypical OOP. Creating a class is done using a function in JavaScript.


I defined one more specific function called Dog. Here, in order to inherit the Animal class, we need to perform call function(we discussed it earlier) with passing this and other arguments. We can instantiate a German Shepard like this.

```javascript
function Dog(name, type) {
   Animal.call(this, name, type);
   this.sound = "bow";
}
```

### Arrow Function

## function declaration vs function expression

function declaration 은 hoisted 된다.
