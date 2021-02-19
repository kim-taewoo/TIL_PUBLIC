let answer = 0
const combs = new Set()

const isPrime = (number) => {
  if (number < 2) return false
  if (number === 2) return true
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) return false
  }
  return true
}

const go = (now, numbers, chk) => {
  const nowNumber = Number(now)
  if (!combs.has(nowNumber)) {
    combs.add(nowNumber)
    if (isPrime(Number(now))) {
      answer += 1
    }
  }

  numbers.forEach((el, i) => {
    if (!chk[i]) {
      chk[i] = 1
      const newNow = now + el
      go(newNow, numbers, chk)
      chk[i] = 0
    }
  })
}

function solution(numbers) {
  const numbersArray = numbers.split("")
  const chk = [...Array(numbersArray.length)].map(() => 0)
  go("", numbersArray, chk)
  return answer
}

const numbers = "011"
console.log(solution(numbers))