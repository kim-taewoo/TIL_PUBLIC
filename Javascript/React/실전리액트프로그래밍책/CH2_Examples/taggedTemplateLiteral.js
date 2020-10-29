function highlight(strings, ...expressions) {
  console.log(strings);
  console.log(expressions);
  return strings.reduce(
    (prevValue, str, i) =>
      expressions.length === i // 너무 복잡하게 생각하지 말고, 걍 expressions 가 존재하는 인덱스인 경우임.
        ? `${prevValue}${str}`
        : `${prevValue}${str}<strong>${expressions[i]}</strong>`,
    ''
  );
}

const v1 = 10;
const v2 = 20
const result = highlight`a ${v1} b ${v2}`;
console.log(result);
