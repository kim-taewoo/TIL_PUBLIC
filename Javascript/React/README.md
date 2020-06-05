## JSX vs HTML

- JSX === Javascript XML

### Inline Styling in JSX

  기존 HTML 에서는 `style="background-color: blue"` 같이 인라인 스타일링을 했지만, JSX 에서는 몇단계 변화를 거쳐야만 제대로 스타일링이 가능하다. 

  1. 스타일 속성을 감싸고 있는 큰따옴표 대신, 자바스크립트 문법을 쓰겠다는 의미로 `{ }` 중괄호를 쓴다.
  1. 중괄호 안에 또다시 중괄호를 넣어 자바스크립트 객체 안에 css 스타일링 key-value 를 작성할 것임을 알린다.
  1. key 를 기존 `-` 하이픈을 지우고, CamelCase 로 재작성한다.
  1. value 를 작은 따옴표로 감싼다. (작은 따옴표를 쓸지, 큰 따옴표를 쓸지는 팀 의견을 따른다.)

  변환 결과는 다음과 같다.

  `style={{ backgroundColor: 'blue' }}`

  JSX 내에서 자바스크립트 객체를 사용할 수 있기 때문에, 원한다면 JSX 밖에 따로 스타일링에 관련된 객체를 변수에 저장한 후, 위 style 속성 안에서 reference 해도 된다.

  ```javascript
  const style = { backgroundColor: 'blue', color: 'white' };
  // jsx
  return (
    <button style={style}>BUTTON</button>
  );
  ```

### className

자바스크립트 문법의 `class` 키워드와 충돌하는 것을 막기 위해 `className` 을 쓴다. 하지만 이제 리액트가 발전해서 굳이 `className` 으로 변환하지 않아도 된다는 말이 나오고 있다.

### JSX easily reference JS variable 

inline styling 을 할 때 중괄호를 사용해서 자바스크립트를 사용할 것임을 알렸듯이, JSX 내에서 중괄호를 쓰면 자바스크립트 문법을 작성할 수 있다. (변수, 함수실행 결과물 등등)


## React Componenet Tenets (컴포넌트 교리)

1. **Component Nesting**: A component can be shown inside of another
1. **Component Reusability**: We want to make componentse that can be easily reused through out application
1. **Component Configuration**: We should be able to configure a component when it is created

## Rules of Class Components

1. Must be a Javascript Class
1. Must extend (subclass) React.Component
1. Must define a `render` method that returns some amount of JSX

## Rules of State

1. Only usable with class components
1. You will confuse props with state :(
1. 'state' is a JS object that contains data relevant to a component
1. Updating 'state' on a component causes the component to (almost) instantly rerender
1. State must be initialized when a component is created
1. State can only be updated using the function `setState`

### Default Props
functional Component 의 경우, 컴포넌트 함수 밖에 `defaultProps` 를 따로 선언해줌으로써 props 의 기본값을 설정할 수 있다.

```javascript
Spinner.defaultProps = {
  message: 'Loading...'
}
```

### Helper Method
`render()` 메서드에 조건 분기가 많아지는 것은 나쁘다. 따라서 만약 조건분기에 따라 다른 화면을 그려줘야 하는 상황이라면, 따로 helper method 를 만들어서, 그곳에서 조건분기를 처리하고, 결과값만을 return 받아 `render` 메서드 내에서 사용하는 것이 맞다.



## Redux

### Redux Cycle

1. Action Creator : `Action` 이라고 부를 Javascript Object 를 반환한다.
2. Action : `type`, 와 `payload` property 를 가진 자바스크립트 객체다. `type` 키의 값은 대문자와 언더스코어만을 쓰는 것이 convention 이다.
3. dispatch : `Action` 을 받아서, 복사한 후, `Reducer` 들에게  뿌린다.
4. Reducers :  현재 state 상태를 가지고와서, `Action` 에 따라 변형한 후, 다시 state 를 되돌려주어 업데이트한다.  이때 돌려주는 state 는 반드시 **새로 만들어진** 것이어야 한다. 즉, 기존의 state 를 변형하는 게 아니라 복사해서 업데이트 된 새로운 것으로 만들어 되돌려 주어야 한다.(물론 `type` 이 아예 자신과 상관없는 것일 경우, `if` 문에서 걸러지지 않았을 테고, 그럼 맨 마지막에 그냥 가져왔던 state 를 그대로 반환하며, 이때는 굳이 새로 만들지 않는다.)   또, 처음에 `undefined` 상태로 state 가 존재할 수 있기 때문에, 매개변수로 받을 현재 상태 state 에 **default value** 를 주어야 한다..
5. State

### Redux Store

위의 Redux Cycle 각각을 구현하는 데는 `Redux` 가 전혀 필요하지 않은 단순 자바스크립트 코드다. 리덕스가 필요한 시점은, 그렇게 용도에 따라 만든 `Reducers` 를 모아서 **하나의 `Store` 를 만드는 데**있다. 즉, 리덕스 객체에서 `createStore`, `combineReducers` 라는 메서드를 가져와서, 만들어놨던 `Reducer` 들을 합쳐 `Store` 를 만든다. 이렇게 `Store`를 만들면, 리덕스가 제공하는 `Dispatch`나, `getState` 등을 사용할 수 있다. 



```javascript
const {createStore, combineReducers} = Redux;

// 기존에 만들어놨던 Reducer 들을 합친다.
const outDepartments = combineReducers({
    accounting,
    claimsHistory,
    policies
})

// 합친 Reducer 모음으로 하나의 Store 를 만든다. 중앙 저장소처럼 생각하자.
const store = createStore(ourDepartments)

// 사용 예
// createPolicy 라는 미리 정의해놨던 Action Creator 로, Action 을 하나 만든다.
const action = createPolicy('Joshua', 27)
// 리덕스가 제공하는 dispatch 를 사용해 dispatch 하자.
store.dispatch(action) // store.dispatch(createPolicy('Joshua', 27)) 처럼 줄여서 사용해도 된다.
// 업데이트 된 store 상태를 확인할 수 있다.
console.log(store.getState())
```

