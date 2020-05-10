function solution(reqs) {
  let res = [];
  const accounts = new Map();
  for (const iterator of reqs) {
    const msgs = iterator.split(' ');
    console.log(msgs);
    switch (msgs[0]) {
      case 'CREATE':
        if (accounts.has(msgs[1])) {
          res.push(403);
        } else {
          accounts.set(msgs[1], [0, -msgs[2]]);
          res.push(200);
        }
        break;

      case 'DEPOSIT':
        if (!accounts.has(msgs[1])) {
          res.push(404);
        } else {
          let now, limit;
          [now, limit] = accounts.get(msgs[1]);
          accounts.set(msgs[1], [now + msgs[2], limit]);
          res.push(200);
        }
        break;

      case 'WITHDRAW':
        if (!accounts.has(msgs[1])) {
          res.push(404);
        } else {
          let now, limit;
          [now, limit] = accounts.get(msgs[1]);
          if (msgs[2] <= (now + -limit)) {
            accounts.set(msgs[1], [now - msgs[2], limit]);
            res.push(200);
          } else {
            res.push(403);
          }
        }
        break;

      default:
        break;
    }
  }
  return res;
}

const reqs = [
  'DEPOSIT 3a 10000',
  'CREATE 3a 300000',
  'WITHDRAW 3a 150000',
  'WITHDRAW 3a 150001',
];
console.log(solution(reqs));
