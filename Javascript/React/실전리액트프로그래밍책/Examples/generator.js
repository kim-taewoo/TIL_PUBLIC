const arr1 = [10, 20, 30];
const iter = arr1[Symbol.iterator]();
console.log(iter.next());

function* f1() {
  yield 10;
  yield 20;
  yield 30;
}

// 제너레이터인 f1 의 반환값은 반복자.
// for of 는 반복자의 next 메서드를 호출하면서 done 속성값이 참이 될 때까지 반복한다.
for (const v of f1()) {
  console.log(v);
}
// 전개 연산자도 마찬가지다.
const arr = [...f1()];
console.log(arr);
