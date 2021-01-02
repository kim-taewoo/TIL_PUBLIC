[NodeJS single thread JS runtime and thread pool explained](https://medium.com/@chaolu_dev/nodejs-single-thread-js-runtime-and-thread-pool-explained-bd991f2ae730)

Node.js 는 싱글 스레드가 맞지만, 기본적으로 내부적으로 C++ 로 구현된 4개의 스레드풀를 가지고 있다. 이 스레드들은 disk I/O 에 쓰인다.