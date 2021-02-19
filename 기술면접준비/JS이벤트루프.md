[Must Read](https://tk-one.github.io/2019/02/07/nodejs-event-loop/)

- ES6 에서 추가된 Promise 를 처리하는 microtask queue(job queue 라고도 함) 는, 일반 message queue(task queue, callback queue, event queue 라고도 부름) 보다 높은 우선순위를 갖는다. 즉, call stack 이 비었을 때, microtask queue 가 빌 때까지 우선적으로 처리된 후에야 message queue 가 callback queue 에 들어갈 수 있다. 

[자세한 설명 추가된 글](https://frarizzi.science/journal/web-engineering/javascript-main-thread-dissected)

위 블로그에서는 `next tick` 개념을 추가해서 설명하고 있다. event loop 은 call stack 이 빌 때마다 이 `next tick` 에 있는 일을 call stack 으로 옮겨서 처리하는데, 이 `next tick` 에는 콜백 **하나**, **모든** job queue, **가능한 정도** 의 render queue 가 들어가게 된다.  