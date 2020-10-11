# this의 동작 원리
다른 프로그래밍 언어에서 this가 가리키는 것과 JavaScript에서 this가 가리키는 것과는 좀 다르다. this가 가리킬 수 있는 객체는 정확히 5종류나 된다.

1. Global Scope에서도 this가 사용될 수 있고 이때에는 Global 객체를 가리킨다.

2. 함수를 호출할 때
```js
foo();
```
이때에도 this는 **Global** 객체를 가리킨다.  

즉, 함수를 어디에서 선언했느냐는 중요치 않고, **호출** 시점에 어떤 방식으로 호출되고 있느냐가 중요하다. (물론 ES6 이후 등장한 화살표 함수 같은 건 예외.)

> 개인적인 생각으로는 그냥 .(dot) 의 '왼쪽' 에 있는 게 `this` 라고 생각할 수 있고, global scope 에서 호출하는 건 앞에 `global.`(혹은 `window`) 이 생략된거라고 생각해도 되지 않나 싶다.

3. 메소드로 호출할 때
```js
test.foo();
```
이 경우에는 `this` 가 `test` 를 가리킨다. (. 왼쪽) 

> Note: 브라우저 이벤트가 발생했을 때, 이벤트를 발생한 객체가 this가 되는데, 이것도 결국엔 `obj.onClick` 같이 호출된 것으로 생각하자.

4. 생성자를 호출할 때
```js
new foo();
```
new 키워드로 생성자를 실행시키는 경우에 이 생성자 안에서 this는 새로 만들어진 객체를 가리킨다.

5. `this` 가 가리키는 객체 정해주기
```js
function foo(a, b, c) {}

var bar = {};
foo.apply(bar, [1, 2, 3]); // a = 1, b = 2, c = 3으로 넘어간다.
foo.call(bar, 1, 2, 3); // 이것도... 
```
`Function.prototype`의 `call`이나 `apply` 메소드를 호출하면 this가 무엇을 가리킬지 정해줄 수 있다. 호출할 때 첫 번째 인자로 this가 가리켜야 할 객체를 넘겨준다.

> Note: 객체 리터럴에서 this는 그 객체를 가리키지 않는다. 예를 들어 `var obj= {me:this}`에서 me가 obj를 가리키는 것이 아니라 위에 설명한 5가지 객체 중 하나를 가리킨다.

> 개인적인 의견으로, `this` 는 언제나 상대적인 것으로, **호출 시점**에 무엇을 가르킬지 결정된다고 본다. 그리고 따로 설정하지 않는 이상 `.` 의 왼쪽에 있는 것을 가리킨다. 

# 대표적인 함정

1. `this`가 `Global` 객체를 가리키는 것도 잘못 설계된 부분 중 하나다. 괜찮아 보이지만 실제로는 전혀 사용하지 않는다.

```js
Foo.method = function() {
    function test() {
        // 여기에서 this는 Global 객체를 가리킨다.
    }
    test();
}
```

`.bind()` 를 쓰거나, `var self = this` 를 쓰거나, 화살표 함수를 써서 제대로 `this` 를 할당할 수 있다.

2. Method 할당하기

JavaScript의 또다른 함정은 바로 함수의 별칭을 만들수 없다는 점이다. 별칭을 만들기 위해 메소드를 변수에 넣으면 자바스크립트는 별칭을 만들지 않고 바로 할당해 버린다. (즉, 일반 함수가 되고, 따라서 `this` 가 달라진다.)

```js
var test = someObject.methodTest;
test();
```

이렇게 this를 늦게 바인딩해서 나타나는 약점때문에 늦은 바인딩이 나쁜 거라고 생각할수도 있지만, 사실 이런 특징으로 인해 프로토타입 상속(prototypal inheritance)도 가능해진다.

```js
function Foo() {}
Foo.prototype.method = function() { console.log(this) };

function Bar() {}
Bar.prototype = Foo.prototype;

new Bar().method(); // Bar {}
```
Bar 인스턴스에서 method를 호출하면 method에서 this는 바로 그 인스턴스를 가리킨다.
