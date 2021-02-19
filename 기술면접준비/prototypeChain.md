[MDN Prototype Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain#using_prototypes_in_javascript)
[설명 잘하는 유튜브](https://youtu.be/XskMWBXNbp0)
1. 객체의 프로토타입은 `Object.getPrototypeOf()` 나, non-standard 이지만 de-facto 방법인 `object.__proto__` 로 접근한다.
1. 객체의 프로토타입 체인은 `null` 이 끝이다. `null` 은 프로토타입을 가지지 않기 때문.
1. 자바스크립트에서 함수도 객체이기 때문에, 객체의 프로토타입 접근 방식으로 접근하면 결국 Function -> Object -> null 으로 결론난다. 
1. 하지만 `function.prototype` 로 접근해서 얻는 객체는 위의 객체의 프로토타입과 다른 것이다! 저 방식으로 접근하는 함수의 프로토타입은 프로토타입식 상속을 위한 것으로, `new` 키워드로 생성된(함수가 constructor 로 쓰였을 때) 자식 인스턴스들에게 할당할 프로토타입을 말한다. `function.prototype` 로 계속해서 접근하다보면 `undefined` 가 나온다. 
1. Arrow function doesn't have a default prototype property (즉, 화살표 함수는 constructor 로 쓰일 수 없다!)
1. 참고로, `Object.prototype` 은 `Object` 를 가리킨다. 즉, `Object.getPrototypeOf(Object.prototype)` 하면 `null` 이 나온다. 비슷한 느낌으로, `Array.prototype` 은 `Array` 를 가리키고 `Function.prototype` 은 `Function` 을 가리킨다. 생각해보면, 객체, 배열, 함수를 생성한다는 건 `new` 가 생략된 거라고도 할 수 있으니, 위에서 설명한 논리가 일치한다.

```
So, when you call

var o = new Foo();
JavaScript actually just does

var o = new Object();
o.[[Prototype]] = Foo.prototype;
Foo.call(o);
(or something like that) and when you later do

o.someProp;
it checks whether o has a property someProp. If not, it checks Object.getPrototypeOf(o).someProp, and if that doesn't exist it checks Object.getPrototypeOf(Object.getPrototypeOf(o)).someProp, and so on.
```