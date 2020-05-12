let apples = 5;
apples = 10;

let speed: string = 'fast';
let hasName: boolean = true;

let nothingMuch: null = null;
let nothing: undefined = undefined;

// built in objects
let now: Date = new Date();

// Array
let colors: string[] = ['red', 'green', 'blue'];
let myNumbers: number[] = [1, 2, 3];
let truths: boolean[] = [true, true, false];

// Classes
class Car {}
let car: Car = new Car();

// Object literal
let point: { x: number; y: number } = {
  x: 10,
  y: 20,
};

// Function
// = 를 기준으로 구분하자.
const logNumber: (i: number) => void = (i: number) => {
  console.log(i);
};

// When to use annotations
// 1) Function that returns the 'any' type
const json = '{"x":10, "y":20}';
const coordinates: { x: number; y: number } = JSON.parse(json);
console.log(coordinates); // {x:10, y:20};
// JSON.parse() 는 상황에 따라 다양한 Type 을 리턴하므로 `any` 타입을 반환한다고 뜬다.

// any 타입은 타입스크립트가 전혀 에러체킹이나 추천을 해줄수가 없기 때문에, 가능한한 any 타입을 그대로 사용하지 않도록 최선을 다해야 한다.

// 2) When we declare a variable on one line
// and initialize it later
let words = ['red', 'green', 'blud'];
let foundWord: boolean;
// let foundWord = false; 같이 inference 를 유도하는 게 사실 더 좋은 코드다.

for (let i = 0; i < words.length; i++) {
  if (words[i] === 'green') {
    foundWord = true;
  }
}

// 3) Variable whose type cannot be inferred correctly
let numbers = [-10, -1, 12];
let numberAboveZero: boolean | number = false;

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] > 0) {
    numberAboveZero = numbers[i];
  }
}
