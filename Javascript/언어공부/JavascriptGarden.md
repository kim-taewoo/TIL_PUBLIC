# this의 동작 원리
다른 프로그래밍 언어에서 this가 가리키는 것과 JavaScript에서 this가 가리키는 것과는 좀 다르다. this가 가리킬 수 있는 객체는 정확히 5종류나 된다.

1. Global Scope에서도 this가 사용될 수 있고 이때에는 Global 객체를 가리킨다.

2. 함수를 호출할 때
```js
foo();
```
이때에도 this는 Global 객체를 가리킨다. 
> 개인적인 생각으로는 그냥 .(dot) 의 '왼쪽' 에 있는 게 `this` 라고 생각할 수 있고, global scope 에서 호출하는 건 앞에 `global.`(혹은 `window`) 이 생략된거라고 생각해도 되지 않나 싶다.

3. 메소드로 호출할 때
```js
test.foo();
```
이 경우에는 `this` 가 `test` 를 가리킨다.

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


# 클로져(Closure)와 참조(Reference)

*클로져*는 JavaScript의 특장점 중 하나다. 클로저를 만들면 클로저 스코프 안에서 클로저를 만든 외부 스코프(Scope)에 항상 접근할 수 있다. JavaScript에서 스코프는 함수 스코프밖에 없기 때문에 기본적으로 모든 함수는 클로저가 될 수 있다.

## private 변수 만들기

```js
function Counter(start) {
    var count = start;
    return {
        increment: function() {
            count++;
        },

        get: function() {
            return count;
        }
    }
}

var foo = Counter(4);
foo.increment();
foo.get(); // 5
```

여기서 Counter는 increment 클로저와 get 클로저 두 개를 반환한다. 이 두 클로저는 Counter 함수 스코프에 대한 참조를 유지하고 있기 때문에 이 함수 스코프에 있는 count 변수에 계속 접근할 수 있다.

## Private 변수의 동작 원리

JavaScript에서는 스코프(Scope)를 어딘가에 할당해두거나 참조할수 없기 때문에 스코프 밖에서는 count 변수에 직접 접근할 수 없다. 접근할수 있는 유일한 방법은 스코프 안에 정의한 두 클로저를 이용하는 방법밖에 없다.

```js
var foo = new Counter(4);
foo.hack = function() {
    count = 1337;
};
```

위 코드에서 foo.hack 함수는 Counter 함수 안에서 정의되지 않았기 때문에 이 함수가 실행되더라도 Counter 함수 스코프 안에 있는 count 값은 변하지 않는다. 대신 foo.hack 함수의 count는 Global 스코프에 생성되거나 이미 만들어진 변수를 덮어쓴다. (앞에 `var`, `const` 등 없으니까.)


## 반복문에서 클로저 사용하기
사람들이 반복문에서 클로저를 사용할 때 자주 **실수**를 하는 부분이 있는데 바로 인덱스 변수를 복사할때 발생한다.

```js
for(var i = 0; i < 10; i++) {
    setTimeout(function() {
        console.log(i);  
    }, 1000);
}
```

이 코드는 0부터 9까지의 수를 출력하지 않고 **10**만 열 번 출력한다.

타이머에 설정된 익명 함수는 변수 i에 대한 참조를 들고 있다가 console.log가 호출되는 시점에 i의 값을 사용한다. console.log가 호출되는 시점에서 for loop는 이미 끝난 상태기 때문에 i 값은 10이 된다.

기대한 결과를 얻으려면 i 값을 복사해 두어야 한다.]

### 바로 위 문제(참조 문제) 해결법

반복문의 index 값을 복사하는 가장 좋은 방법은 **익명함수로 랩핑(Anonymous Wrapper)**하는 방법이다.

```js
for(var i = 0; i < 10; i++) {
    (function(e) {
        setTimeout(function() {
            console.log(e);  
        }, 1000);
    })(i);
}
```

이 익명 함수에 i를 인자로 넘기면 이 함수의 파라미터 e에 i의 값이 복사되어 넘어갈 것이다. 그리고 setTimeout는 익명 함수의 파라미터인 e에 대한 참조를 갖게 되고 e값은 복사되어 넘어왔으므로 loop의 상태에 따라 변하지 않는다.

또다른 방법으로 랩핑한 익명 함수에서 출력 함수를 반환하는 방법도 있다. 아래 코드는 위 코드와 동일하게 동작한다.

```js
for(var i = 0; i < 10; i++) {
    setTimeout((function(e) {
        return function() {
            console.log(e);
        }
    })(i), 1000)
}
```

즐겨 쓰이는 또 하나의 방법은 setTimeout 함수에 세번째 인자를 추가하는 방법이다. 추가된 인자는 콜백 함수에 전달된다.

```js
for(var i = 0; i < 10; i++) {
    setTimeout(function(e) {
        console.log(e);  
    }, 1000, i);
}
```

`.bind`를 사용하는 방법도 있다. .bind는 this 컨텍스트와 인자들을 함수에 결속(bind)시킨다. 아래 코드는 위 코드와 동일하게 동작한다.

```js
for(var i = 0; i < 10; i++) {
    setTimeout(console.log.bind(console, i), 1000);
}
```

# arguments 객체
JavaScript의 모든 함수 스코프에는 arguments라는 특별한 변수가 있다. 이 변수는 함수에 넘겨진 모든 인자에 대한 정보가 담겨 있다.

> Note: arguments 변수는 Function 안에서 다시 정의할 수 없다. var 구문이나 파라미터에 arguments라는 이름으로 변수를 정의해도 변수가 재정의되지 않는다.

arguments 객체는 Array가 아니다. 물론 length 프로퍼티도 있고 여러모로 Array와 비슷하게 생겼지만 Array.prototype을 상속받지는 않았다.

그래서 arguments에는 push, pop, slice 같은 표준 메소드가 없다. 일반 for문을 이용해 순회는 할수 있지만, Array의 메소드를 이용하려면 arguments를 Array로 변환해야 한다.

## Array로 변환하기
다음 코드는 arguments에 있는 객체를 새로운 Array에 담아 반환한다.

`Array.prototype.slice.call(arguments);`

## arguemnts 객체 넘기기
어떤 함수에서 다른 함수로 arguments 객체를 넘길 때에는 다음과 같은 방법을 권한다. (역주: foo 함수는 bar 함수 한번 랩핑한 함수다. )
```js
function foo() {
    bar.apply(null, arguments);
}
function bar(a, b, c) {
    // 내곡동에 땅이라도 산다.
}
```

## 일반 파라미터와 arguments 객체의 인덱스
일반 파라미터와 arguments 객체의 프로퍼티는 모두 getter와 setter를 가진다.

그래서 파라미터나 arguments 객체의 프로퍼티의 값을 바꾸면 **둘 다 바뀐다.**
```js
function foo(a, b, c) {
    arguments[0] = 2;
    a; // 2

    b = 4;
    arguments[1]; // 4

    var d = c;
    d = 9;
    c; // 3
}
foo(1, 2, 3);
```

# 생성자
JavaScript의 생성자는 다른 언어들과 다르게 new 키워드로 호출되는 함수가 생성자가 된다.

생성자로 호출된 함수의 `this` 객체는 **새로 생성된 객체**를 가리키고, **새로 만든 객체의 prototype**에는 **생성자의 prototype이 할당**된다.

그리고 생성자에 **명시적인 return 구문이 없으면 this가 가리키는 객체를 반환**한다.
```js
function Person(name) {
    this.name = name;
}

Person.prototype.logName = function() {
    console.log(this.name);
};

var sean = new Person();
```
위 코드는 **Person을 생성자로** 호출하고 **새로 생성된 객체의 prototype을 Person.prototype으로 설정**한다.

아래 코드와 같이 생성자에 명시적인 return 문이 있는 경우에는 **반환하는 값이 객체인 경우에만** 그 값을 반환한다.
```js
function Car() {
    return 'ford';
}
new Car(); // 'ford'가 아닌 새로운 객체를 반환

function Person() {
    this.someValue = 2;

    return {
        name: 'Charles'
    };
}
new Person(); // someValue가 포함되지 않은 ({name:'Charles'}) 객체 반환
```
new 키워드가 없으면 그 함수는 객체를 반환하지 않는다.
```js
function Pirate() {
    this.hasEyePatch = true; // 전역 객체를 준비!
}

var somePirate = Pirate(); // somePirate = undefined
```
위 예제는 그때그때 다르게 동작한다. 그리고 this 객체의 동작 원리에 따라서 Pirate 함수안의 this의 값은 Global 객체를 가리키게된다. (역주: 결국 **new 키워드를 빼고, 코드를 작성할 경우 원치 않은 this 참조 오류가 발생할 수 있다.**)

## 팩토리
**생성자가 객체를 반환하면 new 키워드를 생략**할 수 있다.
```js
function Robot() {
    var color = 'gray';
    return {
        getColor: function() {
            return color;
        }
    }
}
Robot.prototype = {
    someFunction: function() {}
};

new Robot();
Robot();
```

생성자에 객체를 만들어 명시적으로 반환하면 new 키워드에 관계없이 잘 동작하는 생성자를 만들수있다. 즉, new 키워드가 빠졌을때 발생하는 this 참조 오류를 방어해준다.

## 팩토리로 객체 만들기
new 키워드를 빼먹었을 때 버그가 생긴다는 이유로 아예 new를 사용하지 말 것을 권하기도 한다.

객체를 만들고 반환해주는 팩토리를 사용하여 new 키워드 문제를 회피할 수 있다.
```js
function CarFactory() {
    var car = {};
    car.owner = 'nobody';

    var milesPerGallon = 2;

    car.setOwner = function(newOwner) {
        this.owner = newOwner;
    }

    car.getMPG = function() {
        return milesPerGallon;
    }

    return car;
}
```
new 키워드가 없어도 잘 동작하고 private 변수를 사용하기도 쉽다. 그렇지만, 단점도 있다.

prototype으로 메소드를 공유하지 않으므로 메모리를 좀 더 사용한다.
팩토리를 상속하려면 모든 메소드를 복사하거나 객체의 prototype에 객체를 할당해 주어야 한다.
new 키워드를 누락시켜서 prototype chain을 끊어버리는 것은 아무래도 언어의 의도에 어긋난다.

### 결론
new 키워드가 생략되면 버그가 생길 수 있지만 그렇다고 prototype을 사용하지 않을 이유가 되지 않는다. 애플리케이션에 맞는 방법을 선택하는 것이 나을 거고 어떤 방법이든 *엄격하고 한결같이* 지켜야 한다.

# 스코프와 네임스페이스

JavaScript는 '{}' Block이 배배 꼬여 있어도 문법적으로는 잘 처리하지만, Block Scope은 지원하지 않는다. 그래서 JavaScript에서는 항상 함수 스코프를 사용한다.

```js
function test() { // Scope
    for(var i = 0; i < 10; i++) { // Scope이 아님
        // count
    }
    console.log(i); // 10
}
```

> Note: 할당할 때, 반환할 때, Function 인자에서 사용되는 것을 제외하면 {...}는 모두 객체 리터럴이 아니라 Block 구문으로 해석된다. 그래서 세미콜론을 자동으로 넣어주면 에러가 생길 수 있다.

그리고 JavaScript에는 Namepspace 개념이 없기 때문에 모든 값이 하나의 전역 스코프에 정의된다.

변수를 참조 할 때마다 JavaScript는 해당 변수를 찾을 때까지 상위 방향으로 스코프를 탐색한다. 변수 탐색하다가 전역 스코프에서도 찾지 못하면 ReferenceError를 발생시킨다.

## 전역 변수 문제.
```js
// script A
foo = '42';

// script B
var foo = '42'
```
이 두 스크립트는 전혀 다르다. Script A는 전역 스코프에 foo라는 변수를 정의하는 것이고 Script B는 현 스코프에 변수 foo를 정의하는 것이다.

다시 말하지만, 이 둘은 전혀 다르고 var가 없을 때 특별한 의미가 있다.
```js
// Global Scope
var foo = 42;
function test() {
    // local Scope
    foo = 21;
}
test();
foo; // 21
```
test 함수 안에 있는 'foo' 변수에 var 구문을 빼버리면 Global Scope의 foo의 값을 바꿔버린다. '뭐 이게 뭐가 문제야'라고 생각될 수 있지만 수천 줄인 JavaScript 코드에서 var를 빼먹어서 생긴 버그를 해결하는 것은 정말 어렵다.

```js
// Global Scope
var items = [/* some list */];
for(var i = 0; i < 10; i++) {
    subLoop();
}

function subLoop() {
    // Scope of subLoop
    for(i = 0; i < 10; i++) { // var가 없다.
        // 내가 for문도 해봐서 아는데...
    }
}
```
subLoop 함수는 전역 변수 i의 값을 변경해버리기 때문에 외부에 있는 for문은 subLoop을 한번 호출하고 나면 종료된다.(첫 루프 후 전역 i 가 11이 되기 때문) 두 번째 for문에 var를 사용하여 i를 정의하면 이 문제는 생기지 않는다. 즉, 의도적으로 외부 스코프의 변수를 사용하는 것이 아니라면 var를 꼭 넣어야 한다.

## 지역 변수
JavaScript에서 지역 변수는 함수의 **파라미터**와 **var로 정의한 변수**밖에 없다.

// 전역 공간 var foo = 1; var bar = 2; var i = 2;
```js
function test(i) {
    // test 함수의 지역 공간
    i = 5;

    var foo = 3;
    bar = 4;
}
test(10);
```
foo 변수와 i 변수는 test함수 스코프에 있는 지역 변수라서 전역 공간에 있는 foo, i 값은 바뀌지 않는다. 하지만 bar는 전역 변수이기 때문에 전역 공간에 있는 bar의 값이 변경된다.

## 호이스팅(Hoisting)

JavaScript는 선언문을 모두 호이스트(Hoist)한다. 호이스트란 var 구문이나 function 선언문을 **해당 스코프의 맨 위**로 옮기는 것을 말한다.
```js
bar();
var bar = function() {};
var someValue = 42;

test();
function test(data) {
    if (false) {
        goo = 1;

    } else {
        var goo = 2;
    }
    for(var i = 0; i < 100; i++) {
        var e = data[i];
    }
}
```
코드를 본격적으로 실행하기 전에 JavaScript는 `var` 구문과 function 선언문을 **해당 스코프의** 맨위로 옮긴다.
```js
// var 구문이 여기로 옮겨짐.
var bar, someValue; // default to 'undefined'

// function 선언문도 여기로 옮겨짐
function test(data) {
    var goo, i, e; // Block Scope은 없으므로 local 변수들은 여기로 옮겨짐
    if (false) {
        goo = 1;

    } else {
        goo = 2;
    }
    for(i = 0; i < 100; i++) {
        e = data[i];
    }
}

bar(); // bar()가 아직 'undefined'이기 때문에 TypeError가 남
someValue = 42; // Hoisting은 할당문은 옮기지 않는다.
bar = function() {};

test();
```
블록 스코프(Block Scope)는 없으므로 for문과 if문 안에 있는 var 구문들까지도 모두 함수 스코프 앞쪽으로 옮겨진다. 그래서 **if Block의 결과는 좀 이상해진다.**

원래 코드에서 if Block은 **전역 변수 goo를 바꾸는 것처럼 보였지만 호이스팅(Hoisting) 후에는 지역 변수를 바꾼다.**

호이스팅을 모르면 다음과 같은 코드는 ReferenceError를 낼 것으로 생각할 것이다.
```js
// SomeImportantThing이 초기화됐는지 검사한다.
if (!SomeImportantThing) {
    var SomeImportantThing = {};
}
```
var 구문은 전역 스코프의 맨위로 옮겨지기 때문에 이 코드는 잘 동작한다.
```js
var SomeImportantThing;

// SomeImportantThing을 여기서 초기화하거나 말거나...

// SomeImportantThing는 선언돼 있다.
if (!SomeImportantThing) {
    SomeImportantThing = {};
}
```

## 이름 찾는 순서
JavaScript의 모든 Scope은 현 객체를 가리키는 this를 가지고 있다. 전역 스코프에도 this가 있다.

함수 스코프에는 arguments라는 변수가 하나 더 있다. 이 변수는 함수에 인자로 넘겨진 값들이 담겨 있다.

예를 들어 함수 스코프에서 foo라는 변수에 접근할 때 JavaScript는 다음과 같은 순서로 찾는다.

1. 해당 Scope에서 `var foo` 구문으로 선언된 것을 찾는다.
2. Function 파라미터에서 `foo`라는 것을 찾는다.
3. 해당 Function 이름이 `foo`인지 찾는다.
4. 상위 Scope으로 있는지 확인하고 있으면 #1부터 다시 한다.

# 네임스페이스
JavaScript에서는 전역 공간(Namepspace) 하나밖에 없어서 변수 이름이 중복되기 쉽다. 하지만 이름없는 랩퍼(Anonymous Wrappers)를 통해 쉽게 피해갈 수 있다.
```js
(function() {
    // 일종의 네임스페이스라고 할 수 있다.

    window.foo = function() {
        // 이 클로저는 전역 스코프에 노출된다.
    };

})(); // 함수를 정의하자마자 실행한다.
```
이름없는 함수는 **표현식(expressions)**이기 때문에 호출되려면 먼저 평가(Evaluate)돼야 한다.
```js
( // 소괄호 안에 있는 것을 먼저 평가한다.
function() {}
) // 그리고 함수 객체를 반환한다.
() // 평가된 결과를 호출한다.
```
함수를 평가하고 바로 호출하는 방법이 몇가지 더 있다. 문법은 다르지만 똑같다.

```js
// 함수를 평가하자마자 호출하는 방법들...
!function(){}();
+function(){}();
(function(){}());
// 등등...
```
## 결론
코드를 캡슐화할 때는 항상 이름없는 랩퍼(Anonymous Wrapper)로 네임스페이스를 만들어 사용할 것을 추천한다. 이 래퍼(Wrapper)는 이름이 중복되는 것을 막아 주고 더 쉽게 모듈화할 수 있도록 해준다.

그리고 전역 변수를 사용하는 것은 좋지 못한 습관이다. 이유야 어쨌든 에러 나기 쉽고 관리하기도 어렵다.

# 타입

## 타입 캐스팅

1. 스트링으로 변환하기  
`'' + 10 === '10'; // true`  
숫자를 빈 스트링과 더하면 쉽게 스트링으로 변환할 수 있다.

2. 숫자로 변환하기
`+'10' === 10; // true`  
+ 연산자만 앞에 붙여주면 스트링을 쉽게 숫자로 변환할 수 있다.

3. Boolean으로 변환하기
'!' 연산자를 두 번 사용하면 쉽게 Boolean으로 변환할 수 있다.

```js
!!'foo';   // true
!!'';      // false
!!'0';     // true
!!'1';     // true
!!'-1'     // true
!!{};      // true
!!true;    // true
```

# undefined

**undefined도 변수**  
undefined는 undefined라는 값을 가지는 데이터 형식이다.

undefined는 상수도 아니고 JavaScript의 키워드도 아니다. 그냥 undefined라는 이름의 Global 변수이고 이 변수에는 undefined라고 할당돼 있다. 그래서 이 Global 변수의 값을 쉽게 바꿀 수 있다.

> ES5 Note: ECMAScript 5의 strict 모드에서는 undefined를 더는 바꿀 수 없도록 했다. 하지만 undefined라는 함수를 만들면 여전히 할당할 수 있다.

undefined 값이 반환될 때:

1. `global` 변수 `undefined`에 접근할 때.
1. 선언은 했지만 아직 초기화하지 않은 변수에 접근할 때.
1. `return` 구문이 없는 함수는 암묵적으로 undefined를 반환함.
1. `return` 구문으로 아무것도 반환하지 않을 때.
1. 없는 프로퍼티를 찾을 때.
1. 함수 인자가 생략될 때.
1. `undefined`가 할당된 모든 것.
1. `void(expression)` 형식으로 된 표현


# setTimeout과 setInterval
JavaScript는 setTimeout과 setInterval함수를 이용해 비동기로 함수를 실행시킬수있다.

```js
function foo() {}
var id = setTimeout(foo, 1000); // 0보다 큰 수를 반환한다.
```
setTimeout을 호출하면 타이머의 ID를 반환하고 대략 1,000밀리 초 후에 foo를 실행시킨다. foo는 딱 한 번만 실행한다.

JS엔진은 타이머에 설정한 시간(timer resolution)에 따라서 코드를 실행하지만 단일 쓰레드이기 때문에 특정 코드는 실행이 지연 될수도 있다. 따라서 setTimeout으로 코드가 실행돼야 할 시간을 정해줘도 정확하게 그 시간에 실행되지 않을수도 있다..

첫 번째 인자로 넘긴 함수는 전역 객체가 실행시킨다. 따라서 인자로 넘겨진 함수 내부의 `this`는 전역 객체를 가리키게 된다.

```js
function Foo() {
    this.value = 42;
    this.method = function() {
        // this는 전역 객체를 가리키기 때문에 
        console.log(this.value); // undefined를 출력한다.
    };
    setTimeout(this.method, 500);
}
new Foo();
```

## 함수 호출을 쌓는(Stacking) setInterval함수.
setTimeout은 딱 한 번 함수를 호출하지만 setInterval은 이름처럼 지정한 시간마다 함수를 실행시켜준다. 하지만 이 함수의 사용은 좀 생각해봐야한다.

setInterval은 실행하는 코드가 일정시간 동안 블럭되도 계속해서 함수를 호출하기 때문에 주기가 짧은 경우 함수 호출이 쉽게 쌓여버린다.

```js
function foo(){
    // 1초 동안 블럭함.
}
setInterval(foo, 100);
```

위 코드에서 foo함수는 호출될 때마다 1초씩 실행을 지연시킨다.

하지만 foo함수가 블럭되더라도 setInterval함수는 계속해서 함수 호출을 쌓기 때문에 foo함수 호출이 끝나면 10번 이상의 함수 호출이 쌓여서 대기하고 있을수도 있다. (역주: **따라서 함수 호출이 쌓이게 되면 원래 기대했던 실행 주기를 보장받지 못한다.**)

블럭되는 코드 해결법
앞에 문제를 해결하는 가장 쉽고 일반적인 방법은 setTimeout 함수에서 자기 자신을 다시 호출하는 방법이다.

```js
function foo(){
    // something that blocks for 1 second
    setTimeout(foo, 100);
}
foo();
```

이 방법은 함수 호출이 쌓이지도 않을 뿐만 아니라 setTimeout 호출을 해당 함수 안에서 관리하기 때문에 foo 함수에서 계속 실행할지 말지도 조절할 수 있다.

## 타이머 없애기

`clearTimeout`과 `clearInterval` 함수로 `setTimeout`과 `setInterval`로 등록한 timeout과 interval을 삭제할 수 있다. set 함수들이 반환한 id를 저장했다가 clear 함수를 호출해서 삭제한다.
```js
var id = setTimeout(foo, 1000);
clearTimeout(id);
```

