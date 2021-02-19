function solution(bridge_length, weight, truck_weights) {
  const N = truck_weights.length
  let truck_i = 0
  let time = 0;
  // [트럭 무게, 나가야 하는 시간]
  const queue = [[0, 0]];
  let weightOnBridge = 0

  while (queue.length || truck_i < N) {
    if (queue[0][1] === time) {
      weightOnBridge -= queue.shift()[0]
    }
    if (weightOnBridge + truck_weights[truck_i] <= weight) {
      weightOnBridge += truck_weights[truck_i]
      queue.push([truck_weights[truck_i++], time + bridge_length])
    } else {
      if (queue[0]) time = queue[0][1] - 1
    }
    time++
  }
  return time
}

const bridge_length = 2
const weight = 10
const truck_weights = [7,4,5,6]
console.log(solution(bridge_length, weight, truck_weights))