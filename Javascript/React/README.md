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