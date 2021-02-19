[NodeJS single thread JS runtime and thread pool explained](https://medium.com/@chaolu_dev/nodejs-single-thread-js-runtime-and-thread-pool-explained-bd991f2ae730)

Node.js 는 싱글 스레드가 맞지만, 기본적으로 내부적으로 C++ 로 구현된 4개의 스레드풀를 가지고 있다. 이 스레드들은 disk I/O 에 쓰인다.

하지만 C++ 4개 스레드풀을 우선적으로 사용하지는 않는다. 최대한 OS 커널의 비동기 모듈을 활용해서 작업을 처리하고, 그 처리 결과를 받아서 사용한다. 이 방법이 실패하거나 성능이 모자란 경우에만 스레드풀을 사용하게 되는 것이다. 

[자바스크립트 작동 설명 글](https://frarizzi.science/journal/web-engineering/javascript-main-thread-dissected)

브라우저의 경우, 메인 스레드에 콜스택, 각종 큐들(잡큐(microtask 큐), 메시지 큐(이벤트 큐, task queue), 렌더 큐), 이벤트 루프가 Browser APIs 들과 함께 존재하는 것은 사실이다. 하지만 메인 스레드 외에도 Parser Thread, Statistics collector Thread, Optimizer Thread, Garbage Collector Thread, Rasterizer Thread 등이 존재한다. 