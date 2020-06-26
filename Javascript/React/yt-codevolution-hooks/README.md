[출처](https://youtu.be/cF2lQ_gZeA8)

[Hooks공식문서(여기 다 있어)](https://reactjs.org/docs/hooks-reference.html)

# Why Hooks?

## 기존의 React 문제점 1

1. Understand how `this` keyword works in Javascript
1. Remember to bind event handlers in class components
1. Classes don't minify very well and make hot reloading very unreliable

## 기존의 React 문제점 2

1. There is no particular way to reuse stateful component logic
1. 위 문제를 해결하기 위해 HOC and render props patterns do address this problem 를 도입하지만, 한 컴포넌트를 다른 여러 컴포넌트로 감싸는 등 이상하고 복잡해짐
1. Hooks 를 사용함으로써 더 나은 방법으로 stateful logic 을 공유할 수 있음.

## 기존의 React 문제점 3

1. Create components for complex scenarios such as data fetching and subscribing to events Related code is not organized in one place -> 무슨 말이냐면, Data fetching 이나 Event listener 부착, 탈착시 각각 componentDidMount 와 componentDidUpdate, componentWillUnmount 같이 여러 생명주기에 나눠서 따로따로 작성해야 하는 문제가 있음. 같은 일을 하고자 해도 여러 곳에 산개되어 작성되는 것... 가장 큰 문제는 클래스 기반 컴포넌트의 자체 stateful logic 을 지키기 위해선 이 상황을 **쪼갤 수도 없다**는 것.. 즉, 구조 자체 문제다.

# Rules of Hooks
1. Only call Hooks at the Top Level. 
    Don't call Hooks inside loops, conditions, or nested functions
1. Only call Hooks from React Functions
    Call them from within React functional components and not just any regular Javascript function


# useState

## useState with previous state

`setState` 는 기본적으로 **async** 작업이기 때문에, 작성한 그대로 이전 값을 기준으로 업데이트 될 것이라 생각하면 안 된다. 즉, `for loop` 같은 데서 `setState` 를 하면 생각했던 것처럼 각 단계에서 전 단계의 결과값을 기다려주지 않는다. 이럴 때는 `setState` 의 인자로 업데이트할 값이 아닌 **함수**를 넘겨주는데, 그 함수는 인자로 이전 값을 받아온다. `prevState` 가 자동으로 인자로 들어오고, 그걸 기반으로 업데이트 하면 되는 것이다. 

```js
// const incrementFive = () => {
//   for (let i = 0; i < 5; i++) {
//     setCount(count + 1)
//   }
// }
const incrementFive = () => {
  for (let i = 0; i < 5; i++) {
    setCount((prevCount) => prevCount + 1);
  }
};
```

## useState with object and with Array

Hooks 의 `useState` 에서 Object 를 사용하면, class based Component 에서의 `this.setState` 와 달리 객체의 어떤 속성을 업데이트 할 때 자동으로 그 업데이트된 속성과 나머지 속성을 merge 해서 update 해주지 않는다. 즉, 알아서 spread operator 를 이용해서 객체를 합체 완성시켜 줘야 한다(즉 hook 의 setState 는 update 가 아니라 replace 가 발생한다.). Array 일 때도 마찬가지..

# useEffect

1. The Effect Hook lets you perform side effects in functional components
1. It is a close replacement for `componentDidMount`, `componentDidUpdate` and `componentWillUnmount`

## cleanup
`useEffect` 의 첫번째 인자 함수가 `return` 하는 또다른 **함수** 는 클래스 컴포넌트의 생명주기 중 `componentWillUnmount` 때 실행될 것들을 작성하는 곳이다. 주로 `componentDidMount` 때 등록했던 이벤트 listener 들을 제거하는 용도로 많이 사용한다.