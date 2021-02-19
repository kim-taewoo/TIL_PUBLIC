## callback 의 단점
1. callback 은 순서대로 해석할 수 없는 비직관적인 작성법을 가지고 있다.
1. callback 을 다른 함수에 넘겨준다는 건, 그 callback 에 대한 컨트롤을 그 함수에게 넘겨주는 것과 같다. (inversion of control) 특히 외부라이브러리의 함수에 callback을 넘겨주게 되면, 그 내부에서 callback 에 대해 어떻게 처리를 하는지 알기가 어렵다. 즉, 컨트롤을 넘겨준다는 것에 심각한 단점이 있다.

## Promise 의 단점
1. 여전히 synchronouse 코드와 다른 특별한 문법을 써야 한다. (then, catch)
1. then 이 길어졌을 때, 그 이전 Promise 결과 값을 그 이후의 then 에서 쓰려면, 일부러 그 값을 상위에서부터 만들어서 내려줘야 한다. (손자에게 넘겨주려면 귀찮다.)

## async await 의 주의점
1. await 을 막 사용하다보면 병렬적으로 처리할 수 있는 일을 쓸데없이 blocking 하는 코드를 짤 수 있으니 주의해야 한다. 
