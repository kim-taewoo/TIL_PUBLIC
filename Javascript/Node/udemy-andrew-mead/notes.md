- WEB Browser 에서는 `window` 가 전역객체였다면, node.js 에서는 `process` 가 전역객체

- `process.argv` 로 명령어 인자들을 받아오는 방법도 있지만, `yargs` 같은 외부 라이브러리를 이용해 더 편하게 작업하는 게 좋다.