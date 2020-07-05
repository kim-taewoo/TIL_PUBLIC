[출처](https://youtu.be/cF2lQ_gZeA8)

[Hooks공식문서(여기 다 있어)](https://reactjs.org/docs/hooks-reference.html)

# Why Hooks?

## 기존의 React 문제점 1

1. Need to understand how `this` keyword works in Javascript
1. Remember to bind event handlers in class components
1. Classes don't minify very well and make hot reloading very unreliable

## 기존의 React 문제점 2

1. There is no particular way to reuse stateful component logic
1. 위 문제를 해결하기 위해 HOC and render props patterns do address this problem 를 도입하지만, 한 컴포넌트를 다른 여러 컴포넌트로 감싸고 또 감싸는 등 이상하고 복잡해짐
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

## useState with Object and with Array

Hooks 의 `useState` 에서 Object 를 사용하면, class based Component 에서의 `this.setState` 와 달리 객체의 어떤 속성을 업데이트 할 때 자동으로 그 업데이트된 속성과 나머지 속성을 merge 해서 update 해주지 않는다. 즉, 알아서 spread operator 를 이용해서 객체를 합체 완성시켜 줘야 한다(즉 hook 의 setState 는 update 가 아니라 replace 가 발생한다.). Array 일 때도 마찬가지.. (리덕스의 리듀서를 생각하면 된다.)

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

1. useReducer is a hook that is used for state management. (즉, useState 나 useReducer 나 state management 를 위한 것이므로 대체재? 로 볼 수 있다.)
1. It is an **alternative** to useState
1. What's the difference?
1. useState is built using useReducer. 즉, useState 보다 더 primitive 한 hook 이다.
1. When to use `useReducer` vs `useState`? 좀 더 배우고 나서 답을 알아보도록 하자.

## What is reducers?
꼭 Redux 를 알아야 할 필요는 없지만 도움은 된다.

바닐라 자바스크립트의 `Array.prototype.reduce()` 의 설명을 보면, 아래와 같다.

> The `reduce()` method executes a **reducer** function (that you provide) on each element of the array, resulting in a single output value

즉, reducer 라는 건 reducer function 과 initial value 라는 두가지 매개변수를 가지고, 결과적으로 하나의 결과값을 반환하는 것이다. 

vanilla JS 의 `reduce()` 의 형태와도 거의 동일하다. `accumulator` 보다는 `currentState`, `currentValue` 보다는 `action` 이라는 용어가 쓰이긴 해도 조금 확장해서 생각하면 작동 방식이 거의 동일하다.

```js
// vanilla JS reduce method
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

console.log(array1.reduce(reducer, 0));
```



### useReducer 사용 예

마치 `action creator` 가 생략된, 간소화된 redux reducer 처럼 작성된다.

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



## Fetching data with useReducer

`useState` 보다 `useReducer` 가 보기 좋을 때는, 관련된 데이터를 하나의 object 로 묶어 관리하기 더 좋아진다는 것이다. 어떤 상황(action) 에 따라 여러 개의 `state` 들이 변해야 하는 상황이라면, 하나의 `reducer` 함수 내의 하나의 `case` 내에서 변화하는 게 보기 간편하다. (결국 소형화된 redux 이다.)

```js
import React, { useEffect, useReducer } from 'react';
import axios from 'axios';

const initialState = {
  loading: true,
  error: '',
  post: {},
};

const reducer = (state, action) => {
  switch (action.type) {
    case 'FETCH_SUCCESS':
      return {
        loading: false,
        post: action.payload,
        error: '',
      };
    case 'FETCH_ERROR':
      return {
        loading: false,
        post: {},
        error: 'Something went wrong!',
      };
    default:
      return state;
  }
};

function DataFetchingTwo() {
  // 보통 state 로 묶어서 state.loading 과 같이 접근하나, 그냥 destructuring 해봤다.
  const [{loading, error, post}, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    (async function () {
      try {
        const response = await axios.get(
          'https://jsonplaceholder.typicode.com/posts/1'
        );
        dispatch({ type: 'FETCH_SUCCESS', payload: response.data });
      } catch (error) {
        dispatch({ type: 'FETCH_ERROR' });
      }
    })();
  }, []);

  return (
    <div>
      {loading ? 'Loading...' : post.title}
      {error ? error : null}
    </div>
  );
}

export default DataFetchingTwo;
```



## Again, `useState` vs `useReducer`

| 시나리오                    | useState                | useReducer             |
| --------------------------- | ----------------------- | ---------------------- |
| Type of state               | Number, String, Boolean | Object or Array        |
| Number of state transitions | One or two              | Too many               |
| Related state transitions   | No                      | Yes                    |
| Business Logic              | No business logic       | Complex business logic |
| Local vs global             | Local                   | Global                 |



# useCallback

## Performance Optimization

리액트의 컴포넌트들은 기본적으로 화면의 어떤 요소가 변하면 그 변화가 자신과 관계가 없어도 모두 **rerendering** 된다. 이 것을 막기 위해서는, 컴포넌트를 `export` 할 때 `React.memo` 로 감싸 주어야 한다. 그러나 이 경우에도 상위 컴포넌트(부모 컴포넌트) 가 props 로 넘겨주는 **함수 **(callback 함수) 는 마치 그 때마다 재정의되는 것으로 여겨지기 때문에, 해당 함수를 prop (callback 함수) 으로 받고 있는 경우엔 실질적으로 함수의 내용이 바뀌지 않았어도 마치 새로운 함수처럼 여겨 자식 컴포넌트가 **rerender** 되어 버린다. 

위 문제를 해결하기 해서 사용하는 것이 `useCallback` 이다. 



> `useCallback` 어디까지나 callback 함수에 관련된 것이다. 즉, 자식 컴포넌트에게 넘겨주는 콜백함수와 연관있을 뿐, 컴포넌트 자체의 `state` 나 `context` 와 관련된 상황에선 당연히 rerender 된다. 또한, `React.memo` 와 같이 애초에 최적화를 노린 컴포넌트에만 사용하도록 하자. 



## What is useCallback?

`useCallback` is a hook that will return a memoized version of the callback function that only changes if one of the dependencies has changed.

## Why useCallback?

It is useful when passing callbacks to optimized(React.memo) child components that rely on reference equality yo prevent unnecessary renders.

## How to use useCallback?

**부모 컴포넌트** 에서 callback 함수를 정의할 때,  function expression 의 바디 부분을 `useCallback` 으로 주고, 그 첫번째 인자로 원하는 함수 정의, 두번째 정의로 dependency 를 준다.



# useMemo

캐싱할 `return` 값을 반환하는 함수를 첫번째 인자로 가진다. 두 번째 인자로는, 언제 다시 계산할 지, 즉 어떤 값이 변했을 때 다시 계산할지를 결정하는 **dependency** 를 배열 안에 넣는다. 그리고 이런 인자를 가진 `useMemo` 전체를 어떤 변수에 할당한다. 그러면 그 변수는 `useMemo` 가 캐싱했거나, 때에 따라 새로 계산한 값을 가지게 된다. 즉, 원래 **함수** 여서 JSX 상에서 `()` 로 호출하며 결과값을 얻었던 것이, `useMemo` 를 사용함으로써 함수가 아닌 변수가 된다는 점에 유의하자.



## useCallback vs useMemo

`useCallback` 은 콜백 함수 자체를 (함수 instance 라고 하는 게 더 옳은 표현이다.)  캐싱한다면, `useMemo` 는 어쨋거나 함수는 invoke 시키고, 그 계산 **결과값만**을 캐싱한다. 



# useRef

useRef 는 그냥 그 html 요소를 가리키기 위해서도 쓰이지만, 재렌더링 없이 어떤 특성을 변형할 때도 쓰인다. 특히나 `useEffect` 와 함께 쓰이는데, `componentDidMount` 시점에 `ref.current` 에 어떤 속성을 부여하고, 이후 어떤 이벤트 발생시 그 속성에 변화, 제거 등을 할 수 있다. 대표적인 사례는 `clearInterval` 이다.  즉, 굳이 `ref` 키워드를 html 요소에 붙이지 않은 상태(`null` 초기값만을 가진 상태) 에서도, `useRef` 는 아주 쓸만한 훅이다. `ref.current` 에 원하는 특성을 넣어두고, 특정 이벤트 때 그것을 변형시킬 수 있다.



# Custom Hooks

Share logic 이 주 목적이며, HOC 와 Render Props 의 대체재라고 할 수 있다.