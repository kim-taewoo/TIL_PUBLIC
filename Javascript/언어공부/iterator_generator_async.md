[아래 링크들을 모아서 추천하고 있는 글](https://medium.com/@la.place/async-await%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94%EA%B0%80-fa08a3157647)
[Javascript Iterator(generator포함)](https://medium.com/@la.place/javascript-iterator-b16ca3c51af2)
[TOAST 정리글(좋아)](https://meetup.toast.com/posts/73)
[자바스크립트 제너레이터의 재미(잘 쓴 글이다.)](https://medium.com/@jooyunghan/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%9E%AC%EB%AF%B8-246553cadfbd)

아래는 위 3번째 글 내용이 마음에 들어서 옮긴 quotes

> 제너레이터는 쉽게 말해 Iterator의 반대쪽이다. 어떤 의미의 반대쪽이냐면 Iterator가 값을 읽어오기 위한 인터페이스라면 Generator는 값을 쓰기 위한 인터페이스란 측면 때문이다.

> 제너레이터 함수는 동작이 특이하다. 일반적인 함수와 다르다. 호출하면 제너레이터 객체만 생성하고 반환한다. 제너레이터 객체의 next()가 호출되면(for..of에 사용된 경우도 마찬가지) 그제서야 실행을 시작하여 처음 만나는 yield 에서 호출자에 값을 전달하면서 실행을 멈춘다(pause/suspend). 다시 next()가 호출되면 아까 멈춘 위치에서 실행을 시작(resume)하여 다음 yield까지 실행되고 또 멈춘다. Java의 **멀티쓰레딩 환경이라면 모를까 함수가 실행 중에 멈췄다가 그 위치에서 실행을 계속하다니…**

> 게다가 일반적인 이터레이터의 next() 와 다르게 제너레이터 객체의 next()는 인자를 받을 수도 있다. next() 로 전달한 인자는 제너레이터 함수가 yield 문의 결과로 받아갈 수 있다. 잠깐! 제너레이터 함수가 값을 쓰고 제너레이터 객체의 이터레이터 인터페이스로 값을 읽는 것뿐만 아니라, 제너레이터 객체에 값을 쓰고 제너레이터 함수가 값을 읽어갈 수도 있다고?
> 제너레이터의 이런 특성은 쓰레드를 사용하지 않으면서 **자바스크립트에서 동시성 프로그래밍**을 가능하게 해준다. 이른바 **“협력적 멀티태스킹(cooperative multitasking)"**!

## iterator

```javascript
function TreeNode(val, left = EMPTY, right = EMPTY) {
  this.val = val
  this.left = left
  this.right = right
}

// yield* 역할은 아래 generator 에서 확인
TreeNode.prototype[Symbol.iterator] = function* iterator() {
  yield* this.left
  yield  this.val
  yield* this.right
}
```

## 코루틴
[코루틴 소개](https://medium.com/@jooyunghan/%EC%BD%94%EB%A3%A8%ED%8B%B4-%EC%86%8C%EA%B0%9C-504cecc89407#:~:text=%EC%BD%94%EB%A3%A8%ED%8B%B4%EC%9D%B4%EB%9E%80,%EC%8B%A4%ED%96%89%EC%9D%84%20%EC%9D%B4%EC%96%B4%EA%B0%88%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)

코루틴은 `suspend/resume` 가능하다. 함수가 `call/return`되는 것과 비교하면 더 일반화된 형태라 할 수 있다. (함수는 suspend/resume이 빠진 코루틴인 셈이다.)

컨텍스트(변수 값) 은 출입 과정에서 저장된 상태로 남는다. 

## 제너레이터
[generator 객체1](https://valuefactory.tistory.com/209)

Iterator를 쉽게 만들 수 있는 문법으로 잘 알려진 **Generator는 사실 코루틴의 한 형태**이다. Iterator 인터페이스를 이용하는 쪽에서 다음 값을 요청하면 Generator는 값을 계산하여 yield한다. Iterator 인터페이스를 직접 구현하는 것 보다 Generator를 이용하여 구현하는 것이 훨씬 편리하다.

Iterator의 `next()` 메서드를 호출하면 Generator 함수가 실행되어 yield 문을 만날 때까지 진행하고, 해당 표현식이 명시하는 Iterator로부터의 반환값을 반환한다. `yield*` 표현식을 마주칠 경우, 다른 Generator 함수가 위임(delegate)되어 진행된다.

이후 `next()` 메서드가 호출되면 진행이 멈췄던 위치에서부터 재실행합니다. `next()` 가 반환하는 객체는 yield문이 반환할 값(yielded value)을 나타내는 value 속성과, Generator 함수 안의 모든 yield 문의 실행 여부를 표시하는 boolean 타입의 done 속성을 갖습니다. `next()` 를 인자값과 함께 호출할 경우, 진행을 멈췄던 위치의 `yield` 문을  `next()` 메서드에서 **받은 인자값으로 치환**하고 그 위치에서 다시 실행하게 됩니다.

generator와 yield는 promise와는 아무런 관련이 없다. yield는 그 자체만으로는 비동기 요청을 동기처리로 변환해주는 마법의 도구가 아니다. 결국 동기처리를 위해서는 promise가 필요하며, 중지와 재개라는 성격을 가진 generator-yield는 promise처리를 보기 쉽게 도와주는 기능만 할 뿐이다.

generator 는 생성자로 쓸 수 없다. (`new` 키워드 안 됨)

```javascript
// yield*를 사용한 예제

function* anotherGenerator(i) {
  yield i + 1;
  yield i + 2;
  yield i + 3;
}

function* generator(i){
  yield i;
  yield* anotherGenerator(i);
  yield i + 10;
}

var gen = generator(10);

console.log(gen.next().value); 
// 10

console.log(gen.next().value); 
// 11

console.log(gen.next().value); 
// 12

console.log(gen.next().value); 
// 13

console.log(gen.next().value); 
// 20
```

## Promise 와 yield

