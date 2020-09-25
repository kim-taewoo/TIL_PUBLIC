const solution = (numbers, target) => {
  let answer = 0;
  const queue = [[numbers[0], 0], [-numbers[0], 0]];
  while (queue.length) {
    const now = queue.shift()
    if (now[1] === numbers.length - 1) {
      if (now[0] === target) {
        answer += 1
      }
      continue
    }
    queue.push([now[0] + numbers[now[1] + 1], now[1] + 1]);
    queue.push([now[0] - numbers[now[1] + 1], now[1] + 1]);
  }
  return answer;
};

const numbers = [1, 1, 1, 1, 1];
target = 3;
console.log(solution(numbers, target));