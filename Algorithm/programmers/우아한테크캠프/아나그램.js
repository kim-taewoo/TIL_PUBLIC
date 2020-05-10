function compareMaps(map1, map2) {
  if (map1.size !== map2.size) {
    return false;
  }
  let tmp;
  for (var [key, val] of map1) {
    tmp = map2.get(key);
    // in cases of an undefined value, make sure the key
    // actually exists on the object so there are no false positives
    if (tmp !== val || (tmp === undefined && !map2.has(key))) {
      return false;
    }
  }
  return true;
}

function solution(arr) {
  const allMaps = [];
  for (let index = 0; index < arr.length; index++) {
    const newMap = new Map();
    let element = arr[index];
    while (element > 0) {
      const q = Math.floor(element / 10);
      const r = element % 10;
      if (newMap.has(r)) {
        newMap.set(r, newMap.get(r) + 1);
      } else {
        newMap.set(r, 1);
      }
      element = q;
    }

    let flag = false;
    for (const iterator of allMaps) {
      if (compareMaps(iterator, newMap)) {
        flag = true;
        break;
      }
    }
    if (!flag) allMaps.push(newMap);
  }
  return allMaps.length;
}

let arr = [112, 1814, 121, 1481, 1184];
console.log(solution(arr));
