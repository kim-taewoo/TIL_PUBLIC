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

## 자주하는 실수

`setInterval` 과 같이 이벤트 등록, 제거 자체는 한 번만 하고 한 번만 제거하면 되지만 지속해서 값의 변화를 관찰해주어야 하는 경우에는, `setState` 에 이전 값을 참조해주는 함수형태의 인자를 넣는 것이 실수 방지에 도움이 된다.

```javascript
const tick = () => {
  // setCount(count + 1)
  setCount(prevCount => prevCount + 1)
}

useEffect(() => {
  const interval = setInterval(tick, 1000);
  return () => {
    clearInterval(interval)
  }
}, [])
```

## Fetching data with useEffect

가까운 시일 내에 `suspense` 라는 게 데이터 fetch 를 도맡게 되겠지만, 현재엔 `useEffect` 를 잘 쓰는 게 도움이 된다.

# Context API
Context provides a way to pass data through the component tree without having to pass props down manually at every level.

## 사용법
1. createContext
1. Provider 로 자식 컴포넌트 감싸기
1. 자식 컴포넌트에서 Consumer 로 이용하기

근데 단순히 이렇게 이용하면 너무 지저분하고 품이 많이 든다. 그래서 context hook 을 이용한다. hook 을 써도 앞 2단계는 동일하다. 다만 comsumer 단계가 간소화된다.

`import` 해야되는 것은 동일하지만, 마치 `useState` 를 쓰듯이, `useContext` 의 인자로 `import` 해 온 Context 를 넣고 변수로 받기만 하면 해당 Context 가 가지고 있는 데이터를 받아서 쓸 수 있다. 

### 사용예시
```javascript
// App.js
import React, { createContext } from 'react';
import ComponentA from 'components/contextAPI/ComponentA';

export const UserContext = createContext()

function App() {
  return (
    <div className="App">
      <UserContext.Provider value={{name: 'Taewoo', age: 27}}>
        <ComponentA />
      </UserContext.Provider>
    </div>
  );
}

export default App;
```

```javascript
import React, {useContext} from 'react'
import {UserContext} from 'App'

function ComponentA() {
  const user = useContext(UserContext)
  return (
    <div>
      {JSON.stringify(user)}
    </div>
  )
}

export default ComponentA
```

# useReducer

1. useReducer is a hook that is used for state management.
1. It is an **alternative** to useState
1. What's the difference?
1. useState is built using useReducer. 즉, useState 보다 더 primitive 한 hook 이다.
1. When to use `useReducer` vs `useState`? 좀 더 배우고 나서 답을 알아보도록 하자.

## What is reducers?
꼭 Redux 를 알아야 할 필요는 없지만 도움은 된다.

바닐라 자바스크립트의 `Array.prototype.reduce()` 의 설명을 보면, 아래와 같다.

> The `reduce()` method executes a **reducer** function (that you provide) on each element of the array, resulting in a single output value

즉, reducer 라는 건 reducer function 과 initial value 라는 두가지 매개변수를 가지고, 결과적으로 하나의 결과값을 반환하는 것이다. 

### useReducer 사용 예

마치 간소화된 redux reducer 처럼 작성된다.

```javascript
import React, { useReducer } from 'react'

const initialState = 0
const reducer = (currentState, action) => {
  switch (action) {
    case 'increment':
      return currentState + 1
    case 'decrement':
      return currentState - 1
    case 'reset':
      return initialState
    default:
      return currentState
  }
}

function CounterOne() {
  const [count, dispatch] = useReducer(reducer, initialState)
  return (
    <div>
      <div>Count : {count}</div>
      <button onClick={() => dispatch('increment')}>Increment</button>
      <button onClick={() => dispatch('decrement')}>Decrement</button>
      <button onClick={() => dispatch('reset')}>Reset</button>
    </div>
  );
}

export default CounterOne
```

