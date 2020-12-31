// 자바스크립트에서 (exp1, exp2) 를 반환하면 둘 다 실행한 뒤 두번째 것을 반환한다.
const result = tap('fun')((it) => console.log('value is', it))

console.log(result)