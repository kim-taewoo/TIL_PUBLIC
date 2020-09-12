function solution(new_id) {
  let answer;
  answer = new_id
    .toLowerCase()
    .replace(/[^(a-z|0-9|\-|\_|\.)]/g, '')
    .replace(/[\(\)]/g, '')
    .replace(/\.{2,}/g, '.')
    .replace(/^\./, '')
    .replace(/\.$/, '');
  answer = answer.length ? answer : 'a';
  answer = answer.length >= 16 ? answer.slice(0, 15) : answer;
  answer = answer.replace(/\.$/, '');
  if (answer.length <= 2) {
    const last = answer.substr(answer.length - 1);
    while (answer.length <= 2) {
      answer = answer + last;
    }
  }
  return answer;
}
// '-_.~!@#$%^&*()=+[{]}:?,<>';
console.log(solution('z-+.^.'));
