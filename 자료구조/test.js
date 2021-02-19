function solution(next_student) {
  const students_n = next_student.length;
  const counter = Array.from(Array(students_n), () => 1);
  const isInCycle = Array.from(Array(students_n), () => 0);
  for (let i = 0; i < students_n; i++) {
    const visited = Array.from(Array(students_n), () => false);
    visited[i] = true;
    let nextIdx = i;
    while (1) {
      let next = next_student[nextIdx] - 1;
      if (visited[next]) {
        if (next === i) {
          visited.forEach((v, idx) => {
            if (v) {
              isInCycle[idx] = counter[i];
            }
          });
        }
        break;
      }
      if (next === -1) {
        break;
      }
      if (isInCycle[next]) {
        if (isInCycle[i]) {
          counter[i] = isInCycle[i];
        } else {
          counter[i] += counter[next];
        }
        break;
      }
      if (counter[next] > 1) {
        counter[i] += counter[next];
        break;
      }
      counter[i]++;
      visited[next] = true;
      nextIdx = next;
    }
  }

  const maxi = Math.max(...counter);
  console.log(counter);

  const maxis = [...counter.keys()].filter((v) => counter[v] === maxi);
  return maxis[maxis.length - 1] + 1;
}

const next_student = [5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2];
// const next_student = [6, 10, 8, 5, 8, 10, 5, 1, 6, 7];
console.log(solution(next_student));
