// 자바스크립트에서 함수.length 를 하면, 그 함수의 인자 개수를 반환한다.

const unary = (fn) => (fn.length === 1 ? fn : (arg) => fn(arg));
