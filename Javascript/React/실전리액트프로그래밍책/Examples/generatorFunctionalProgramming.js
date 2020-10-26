function* map(iter, mapper) {
  for (const v of iter) {
    yield mapper(v);
  }
}

function* filter(iter, test) {
  for (const v of iter) {
    if (test(v)) {
      yield v;
    }
  }
}

function* take(n, iter) {
  for (const v of iter) {
    if (n <= 0) {
      return;
    }
    yield v;
    n--;
  }
}

const values = [...Array(10)].map((_, i) => i + 1);
const result = take(
  3,
  map(
    filter(values, (n) => n % 2 === 0),
    (n) => n * 10
  )
); // 여기까지는 실제 연산은 이루어지지 않고 제너레이터 객체만 생성된다.

console.log([...result]); // 값이 필요한 이 순간에 연산을 한다. 이런 방식을 지연 평가(lazy evaluation) 라고 부른다.
// 심지어 이 경우에도 6까지만 연산이 수행되고 take 함수가 종료된다.

// for (const v of result) {
//   console.log(v);
// }

// 자연수의 집합을 표현한 제너레이터 함수를 보여준다. 제너레이터를 쓰지 않았다면 먹통이 되었을 것이다.
function* naturalNumbers() {
  let v = 1;
  while (1) {
    yield v++;
  }
}

(() => {
  const values = naturalNumbers();
  const result = take(
    3,
    map(
      filter(values, (n) => n % 2 === 0),
      (n) => n * 10
    )
  );
  console.log([...result]);
})();

// 제너레이터 함수끼리 호출하기
// 제너레이터 함수에서 다른 제너레이터 함수를 호출할 때는 yield* 키워드를 이용한다.
// yield* 키워드 오른쪽에는 제너레이터 객체뿐만 아니라 반복 가능한 모든 객체가 올 수 있다.
function* g1() {
  yield 2;
  yield 3;
}

function* g2() {
  yield 1;
  yield* g1();
  yield 4;
}

console.log(...g2());

// yield* 와 동일한 역할
function* g2_second() {
  yield 1;
  for (const value of g1()) {
    yield value;
  }
  yield 4;
}
// yield* 뒤에는 반복 가능한 모든 객체가 올 수 있다.
function* g2_third() {
  yield 1;
  yield* [2, 3];
  yield 4;
}

// next 메서드를 호출하는 쪽에서 제너레이터 함수로 데이터를 전달할 수 있다. 
// 다음과 같이 next 메서드의 데이터를 전달할 수 있다. (기본값 덮어씌우는 느낌)
function* f1() {
  const data1 = yield; // 아예 안 써도 됨.
  // const data1 = yield 3;
  console.log(data1);
  const data2 = yield 5;
  console.log(data2);
}
const gen = f1();
gen.next(); // 단순히 제너레이터 함수의 실행이 시작하도록 하는 역할만 수행 (yield 까지니까?)
gen.next(10);
gen.next(20);

// 협업 멀티태스킹
// 멀티태스킹은 여러 개의 태스크를 실행할 때 하나의 태스크가 종료되기 전에 멈추고 다른 태스크가 실행되는 것을 말함.
// 제너레이터는 실행을 멈추고 재개할 수 있기 때문에 멀티태스킹이 가능하다. 
// 협업이라고 하는 이유는 자발적으로 실행을 멈추는 시점을 고르기 때문. 못 고른다면 `선점형` 멀티태스킹이었을 것.

function* minsu() {
  const myMsgList = [
    '안녕 나는 민수야',
    '만나서 반가워',
    '내일 영화 볼래?',
    '시간 안 되니?',
    '내일 모레는 어때?',
  ];
  for (const msg of myMsgList) {
    console.log('수지:', yield msg);
  }
}

function suji() {
  const myMsgList = ['', '안녕 나는 수지야','그래 반가워','...'];
  const gen = minsu();
  for (const msg of myMsgList) {
    console.log('민수:', gen.next(msg).value);
  }
}
suji();

// 제너레이터에서 발생한 예외는 next 메서드를 호출하는 외부 함수에 영향을 준다. 즉, 외부 함수에서 trycatch 가 가능하다.