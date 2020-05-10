function solution(arr) {
  let cnt = 0;
  let tmp = arr.slice();
  let nextTmp = [];
  while (true) {
    if (tmp.length === 1 && tmp[0] === 1) break;

    nextTmp = [];
    let accu = 1;
    for (let index = 1; index < tmp.length; index++) {
      const element = tmp[index];
      if (element === tmp[index - 1]) {
        accu++;
      } else {
        nextTmp.push(accu);
        accu = 1;
      }
    }
    nextTmp.push(accu);
    tmp = nextTmp.slice();
    cnt++;
  }
  return cnt;
}

const arr = [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3];
console.log(solution(arr));
