let answer = 0;

const go = (now, numbers, target, idx) => {
  if (idx == numbers.length) {
    if (now === target) {
      console.log(now, target, answer)
      answer += 1};
    return;
  }

  go(now + numbers[idx], numbers, target, idx + 1);
  go(now - numbers[idx], numbers, target, idx + 1);
};

const solution = (numbers, target) => {
  go(0, numbers, target, 0);
  return answer;
};

const numbers = [1,1,1,1,1]
target = 3
console.log(solution(numbers, target))