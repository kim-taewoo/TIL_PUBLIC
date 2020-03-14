


// arr.map(fn) 이 없던 ES5 시절 직접 만들어 쓴 mapping 함수
function mapForEach(arr, fn) {
  let newArr = [];
  for (let index = 0; index < arr.length; index++) {
    newArr.push(fn(arr[index]));
  };
  return newArr;
}

let log = console.log;
let arr1 = [1, 2, 3];
log(arr1);

let arr2 = mapForEach(arr1, function (item) {
  return item * 2;
});

log(arr2);

let arr3 = arr1.map((i) => i * 2)
log(arr3)
log(arr1)

let checkPastLimit = (limiter) => (item) => item > limiter;
log(mapForEach(arr1, checkPastLimit(1)))

let checkPastLimit2 = function (limiter) {
  return function (item) {
    return item > limiter;
  }
}

let arr4 = mapForEach(arr1, checkPastLimit2(1));
log(arr4)
let arr5 = arr1.map(checkPastLimit2(1))
log(arr5)