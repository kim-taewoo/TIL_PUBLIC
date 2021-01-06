[프론트엔드 면접 질문 모음](https://realmojo.tistory.com/300?fbclid=IwAR2QHO9BeoWCFB4SGYoD_7Qxx_6MLB7qNPjcVuTPXJm9Xm0Qh3wwH85wkiw)

[What the heck is the event loop anyway? | Philip Roberts | JSConf EU](https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=emb_title)

[Jake Archibald: In The Loop - JSConf.Asia](https://www.youtube.com/watch?v=cCOL7MC4Pl0&t=3s)
위 영상을 보면 알 수 있지만, `Promise` 가 `microtask queue` 라는 별도의 큐를 내부적으로 사용하고 있음을 알 수 있다. 즉 `Promise`는 execution context stack, 흔히 call stack 이라고 부르는 스택이 막 task queue 에서 가져온 task 를 해결하고 **비었을 때**, microtask queue 의 모든 내역이 **전부 빌 때까지** main thread 를 점유한다는 걸 알 수 있다. 즉, Promise 도 인피니티뤂 에 빠지면 모든 것을 멈추게 할 수 있다. 다만 실행시점이 task queue 가 남아있는 건 상관없지만 execution context stack 이 비어있을 때다.