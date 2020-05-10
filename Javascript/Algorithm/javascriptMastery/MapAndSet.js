const myArray = [1, 2, 3, 4];
const mySet = new Set(myArray);

console.log(myArray);
console.log(mySet);

const uniqueArray = [...mySet];
console.log(uniqueArray);

const myMap = new Map([
  ['name', 'John'],
  ['surname', 'Doe'],
]);

myMap.set({}, 'c');
myMap.delete('name');

console.log(myMap);

myMap.has('surname');
myMap.clear();
myMap.size();
myMap.clear();

// 일반 obj 에 함께 넣어두면 덮어씌워져버리는 같은 형태의 obj 도 Map 자료형에 넣으면 구분된다.
const a = {};
const b = {};

const myMap2 = new Map([
  [a, 'a'],
  [b, 'b'],
]);
console.log(myMap2);
