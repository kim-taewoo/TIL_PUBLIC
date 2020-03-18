# Section 2. Setting up Environment
1. vscode
1. npm
1. yarn : `npm install -g yarn`

# Section 3. Hello React
작은 프로젝트를 만들면서 React 를 배운다.

> 완성버전 : http://indecision.mead.io
> 완성버전 소스코드 : http://links.mead.io/indecision

- **live-server** 를 vscode 확장프로그램으로 설치하거나 `yarn global add` 혹은 `npm install -g` 로 설치한다. 

- 아직 Webpack 사용법을 안 배웠으니, CDN 으로 React 와 ReactDOM (companion library) 을 받아온다.

- JSX 는 브라우저가 이해하지 못하는 문법이므로, ES6 코드를 ES5 로 변환할 때처럼 **Babel** 을 사용해야 한다. 

## Babel
- Babel 자체는 컴파일러일 뿐, 아무 기능이 없다.
- 따라서 컴파일러를 위한 *Plugins* 혹은 *Presets* 를 추가해야 한다. *Preset* 은 여러 *Plugin* 을 모아둔 것일 뿐이다.

### Babel 설치
1. Babel-커멘드라인인터페이스 글로벌 설치하기 : `yarn global add babel-cli@6.24.1`
1. 위 설치가 제대로 되었는지 `babel --help` 로 확인 가능하다.
1. 이제 로컬 프로젝트에 `yarn init` 으로 저장소를 만든다. (커멘드 경로 확인 필수)
1. React 를 위한 babel `preset` 과, ES6, ES7을 ES5 로 변환해주는 `env` 를 프로젝트에 추가해준다. : `yarn add babel-preset-react@6.24.1 babel-preset-env@1.5.2`
1. 위 설치가 잘되면 `package.json` 와 `yarn.lock` 이 생긴다.
1. 우리가 편하게 작성하는 코드들을 `/src` 폴더에 두고, babel 이 컴파일해 변환된 파일이 `/public/scripts` 에 들어갈 수 있도록 세팅한다.
1. 폴더 구조를 만들었다면, 어떤 타겟 파일을 변환해서 어디에 넣을 것인지 babel 명령어를 실행한다. 마지막 인자는, 어떤 *preset* 을 사용할 것인지 콤마로 분리해 작성한다.
    1. `babel src/app.js --out-file=public/scripts/app.js --presets=env,react`
1. 위 명령어를 시행하면, `scripts/app.js` 파일이 변환된 자바스크립트 코드임을 확인할 수 있다.
1. 그런데 코드를 수정할 때마다 매번 위 길고 긴 babel 명령어를 칠 순 없기 때문에, 마지막에 `--watch` 만 추가해주면, 파일을 수정할 때마다 자동으로 인식해서 babel 을 실행시켜 변환시켜준다. (터미널 하나를 계속 돌리고 있어야 한다.)

> `yarn` 도 `npm` 과 마찬가지로 `yarn install` 로 `package.json` 내 라이브러리를 재설치해준다.

## Exploring JSX
1. JSX - Javascript XML
1. Root element 는 하나여야 한다. 
1. Root element 가 하나기만 하면 줄바꿈과 상관없이 html 작성하듯 변수에 넣으면 되지만, 보통 괄호 안에 넣어주어서 여전히 자바스크립트 변수인 느낌을 준다.
1. JSX 는 `undefined`, `null`, `boolean` 값을 무시한다.

## JSX expressions
중괄호 안에 자바스크립트 expression 을 넣어 템플릿 뷰를 업데이트 할 수 있다. 

## Conditional Rendering in JSX
1. 일반적인 if 문은, if **statement** 이기 때문에 단순히 중괄호 안에 if 문을 넣으면 JSX 가 이해하지 못한다. 그래서 따로 함수를 만들어 if 문은 그곳에 작성하고, 중괄호 안에서 함수를 호출해 `return` 값을 반환한다. 이 때, `return` 값이 html 태그를 포함할 수 있기 때문에 중괄호를 굳이 태그 안에만 넣을 필요 없이 그냥 원하는 위치에 넣어서 태그 통째로 그리거나 말거나 할 수 있다. 

1. 삼항 연산자를 이용해 2가지 조건 중 하나를 골라 그릴 수 있다. 
    ```jsx
      <p>{app.options.length > 0 ? '입력된 선택지 리스트' : '선택지가 없습니다.'}</p>
    ```
1. *&&* logical operator 의 특성을 이용해 모든 조건을 만족하는 경우에만 마지막 부분의 html 태그를 그릴 수 있다. 
    ```jsx
      {!props.options.length && <p>"Please add an option to get started"</p>}
    ```

```javascript
var user = {
  name: 'Taewoo Kim',
  age: 27,
  location: 'Seoul'
};
function getLocation(location) {
  if (location) {
    return <p>Location: {location}</p>;
  }
}
var template = (
  <div>
    {user.name ? <h5>user.name</h5> : <h5>"Anonymous"</h5>}
    {(user.age && user.age >= 18) && <p>Age: {user.age}</p>}
    {getLocation(user.location)}
  </div>
);

var appRoot = document.getElementById('app');
ReactDOM.render(template, appRoot);
```

## var 의 문제점 && let 과 const 로 개선하기

> Define 은 `var a = 3` 같이 새로운 변수를 새로 선언하는 과정이다.  

Assign 은 이미 정의(define) 된 변수가 가진 값을 다른 값으로 바꾸는 과정이다.
1. Re-Assign 뿐만 아니라 Re-Define 까지 가능하기 때문에, 문제가 생기기도 쉽고 문제가 발생했을 때 찾기 매우 어렵다. `let` 을 쓰면 Re-Define 하면 에러가 발생한다. `const` 는 Re-Assign 까지 막는다.

```javascript
var name = 'Josh';
var name = 'Lee'; // 에러가 발생하지 않음. 
```

2. `var` 은 function scope 이고, `let` 과 `const` 도 function scope 이다. 그런데 `let` 과 `const` 는 추가적으로 **Block Scope** 특성을 가진다. 즉, 함수 뿐 아니라 for 문이나 if 문 같은 statement block 안에서 변수가 정의되었다면 밖에서 접근되지 않는다. (var 은 접근 가능하다.)

## Arrow Function
1. 모든 arrow function 은 익명함수다. 따라서 이름을 붙이려면 변수에 따로 저장해서 쓰는 수밖에 없다. 
1. 한 줄로 나타낼 수 있는 경우에는, `return` 문 없는 expression 이 된다.(!statement)
1. Arrow Function 은 일반 함수와 달리 `arguments` 를 이용해 인자 리스트를 불러오지 못한다. 
1. Arrow Function 은 자기 자신의 `this` 를 갖지 않고(bind 하지 않고) 자신이 선언된 부모의 `this` 를 이용한다. 즉 일반 함수와 달리 부모의 `this` context 를 이용하기 위해 `var that = this` 같은 짓을 하지 않아도 된다. 

> `this` 에 대해서 자세히 알고 싶다면 다음 문서를 참고하자 (꼭 제대로 공부해보자.)  
[Github문서](https://github.com/FEDevelopers/tech.description/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%EB%90%98%EB%8A%94-this%EC%97%90-%EB%8C%80%ED%95%9C-%EC%84%A4%EB%AA%85-1#1-this%EC%97%90-%EB%8C%80%ED%95%9C-%EB%AF%B8%EC%8A%A4%ED%84%B0%EB%A6%AC)

## Events and Attributes
1. JSX 으로 html 을 작성할 때, class 대신 className 을 써야 한다. 그냥 class 는 ES6 Javascript 의 class 와 겹치기 때문이다. JSX 에서 쓸 수 있는 html events, attributes 목록은 **React Dom Element** 등으로 검색해서 찾아보자.

1. `onClick={}` 문법으로 클릭시 호출할 자바스크립트 함수를 참조할 수 있다. 
1. 어떤 이벤트로 변수 값이 변화하고, 따라서 화면도 새로 그려야 하는 상황에서, JSX 는 자동으로 데이터 변화를 binding 하는 기능은 없다. 즉, 화면을 새로 그려야 하는 이벤트가 발생할 때마다, 화면을 그리는 함수를 다시 호출해 주어야 한다. 끔찍하게 비효율적일 것 같지만, **그렇지 않다.** React 는 React 만의 가상 DOM 알고리즘을 가지고 있고, 이 알고리즘을 이용해 새로 그릴 필요가 있는 부분만을 찾아내 그 부분만 업데이트 한다. 따라서 화면 전체를 새로 그리지 않고, 효율적으로 필요한 부분만을 바꾼다. 화면을 새로 그리는 이벤트가 발생할 때마다 크롬 개발자 도구의 element 탭을 보면, 필요한 부분만이 반짝이며 바뀌는 것을 확인할 수 있다. 

## Forms and Inputs
다른 자바스크립트 프로그래밍과 마찬가지로, `form` 태그를 이용하고, `onSubmit` 이벤트 핸들러로 어떤 함수를 호출할지 설정한다. `e.preventDefault()` 로 새로고침을 막는다.

## Arrays in JSX
JSX 가 Object 는 다루지 못하지만, Array 는 가능하다. 

- 기본적으로 Array 의 원소 하나하나를 다 출력해 화면에 그려준다. 
- 물론 `undefined`, `null`, `boolean` 은 Array 에 있더라도 여전히 무시된다.
- `.map()` 함수로 배열의 각 원소를 어떤 html 태그에 넣어서 JSX 에 입력할 지 간편하게 만들 수 있다.

```jsx
<ol>
  {
    app.options.map((option) => <li key={option}>{option}</li>)
  }
</ol>
```

## ES6 Classes
1. Class 내에서는 `constructor()` 와 메서드들 사이에 콤마(,) 를 쓰지 않는다.
1. 자식 클래스에서 부모 클래스 메서드를 오버라이딩 할 수 있다. 
1. Arrow Function 으로 메서드를 만들면 현재 클래스를 제대로 가리키지 못하기 때문에, ES5 기존 함수 정의 방식이 개선된 방법으로 메서드를 정의해야 한다. (`function` 생략)

## Class Based React Components
1. 일반적인 html 태그와의 구분을 위해 React Component Class 의 이름은 반드시 대문자로 시작하도록 한다.
1. React Component Class 는 반드시 `render` 메서드를 가지고 있어야 하며, jsx 를 반환한다.
1. 일반적인 html 태그에 key="value" 로 속성을 부여하듯이 컴포넌트에 속성을 넣으면, 그 컴포넌트는 `this.props` 로 자신이 받은 속성들에 접근할 수 있다. 이 부여하는 값, 또 접근한 값을 자바스크립트로 유연하게 설정할 수 있다.
1. 일반적인 자바스크립트 class 처럼 `constructor` 와 메서드를 만들어 `this` 로 접근할 수 있다. 다만 `constructor` 를 사용할 때, `super()` 를 맨 위에 반드시 넣고 시작해야 한다. (상속받은 것이니 당연.)

## Method Binding
`onClick` 이벤트는 해당 이벤트가 발생한 html element 를 `this` 로 받아오기 때문에, 이벤트가 발생했을 때 호출되는 클래스 메서드가 그 컴포넌트 클래스의 `this` 에 접근하지 못한다. 즉, `this.props` 같은 컴포넌트 객체에 접근할 수 없다. 따라서 따로 해당 메서드가 호출될 때의 `this` context 를 binding 해주어야 하는데, 

    1. `render` 메서드에서 onClick 연결메서드가 호출될 때마다 `.bind(this)` 해주거나,
    2. `constructor` 에서 아예 `.bind()` 를 미리 해놓는 방법이 있다.

성능상의 이슈로 2번 방법을 더 많이 쓴다. 아예 화살표 함수로 만들면 안되냐는 의견이 있고, 실제로 그 실험적인 방식을 많이 쓰기도 하지만, 정식 지원되는 기능이 아니다.

## Component State
헷갈리는 부분.  
지금까지 배운 내용으로는, 어떤 이벤트 발생으로 인한 데이터 변화로 화면을 다시 그려야 할 때는, 일일이 미리 정해둔 rendering 함수를 호출해주어야 했다. 그럼 ReactDOM 라이브러리가 변해야 하는 부분을 추적해 업데이트 했다. 그러나 `state` 를 이용하면, 컴포넌트 내의 변화를 인지해 알아서 새로 rendering 해준다.

- state 자체는 그냥 `constructor` 에 하나의 object 를 만들고, 상태를 관리하고자 하는 key, value 를 모아둔다.
- 이벤트가 발생했을 때 호출되는 메서드에서, `this.setState()` 라는 상속받은 메서드를 호출함으로써 값을 변화시키는 동시에 다시 렌더링한다.
- `setState` 는 콜백 함수를 호출하는데, 그 콜백 함수에서 변화되기 이전 상태인 약칭 `prevState` 을 인자로 사용해 접근할 수 있다.
- setState 가 반환하는 객체는 기존 State 를 replace 하는 게 아니라 업데이트 한다. 따라서 관리하는 state 의 일부만 return 한다고 해서 덮어씌워질까 걱정하지 않아도 된다.

## Alternative setState Syntax
`setState` 에서 다른 콜백함수를 호출하지 않고 곧바로 객체를 `return` 하는 방식으로도 State 업데이트가 가능하다. 하지만 이 방식은 권장되지 않고, 이후 삭제될 것이라는 말도 있다. 왜냐하면, `setState` 는 비동기적으로 작동하는 메서드인데(상황을 체크하고 DOM을 업데이트 하는 등 해야할 일이 많아 비동기 방식으로 작동한다.), 콜백함수 호출이 아닌 방법으로 업데이트 하면 그 업데이트 시점이 꼬이면서 원하지 않는 결과로 이어질 수 있기 때문이다. **결론: 쓰지말자**

## 자식에게서 부모로 이벤트 발생 전달하기. - Prop 으로 함수 전달하기
데이터의 흐름은 부모 -> 자식 컴포넌트 이지만, 자식 컴포넌트에서 발생한 이벤트를 부모가 알아야 하는 경우에는 그 흐름을 역으로 올라가야 한다. React 에서는, 부모가 가진 메서드를 자식 컴포넌트에게 prop 으로 넘기고, 자식이 그 메서드를 필요에 따라 호출함으로써 이 문제를 해결한다.

## The Stateless Functional Component
*State* 같은 추가 기능을 사용하지 못하는 제약이 있지만, 단순히 `render` 메서드만 있으면 되는 컴포넌트라면 `Class` 보다 일반 함수를 쓰는 것이 가독성도 좋고, 테스트 하기도 좋으며 약간 더 빠르기까지 하다. 일반 클래스 기반 컴포넌트에서의 `render()` 메서드 내용만을 따로 뺀 듯한 형태로 만들어지며, `this.props` 대신 인자로 `props` 를 받고 사용한다는 점에 주의하자.

## React Devtool
크롬이나 파이어폭스에서 React dev tool 을 설치해서 사용하면, React 의 컴포넌트 구조를 한 눈에 보고 각 컴포넌트의 State 나 Prop 등을 살펴보기 좋다. React Devtool 에서 어떤 컴포넌트를 클릭한 상태로, console 탭으로 돌아가 `$r` 을 치면, 그 컴포넌트에 대한 자세한 정보를 확인할 수 있다.

## Default Props values
컴포넌트에서 사용할 props 의 default 값들을 설정해놓을 수 있다.  
컴포넌트 밖에서 해당 컴포넌트 클래스 혹은 함수(functional component인 경우) 의 `defaultProps` 속성에 접근해 객체를 할당해놓으면 된다.

```javascript
Count.defaultProps = {
  count: 0
};
```

## LifeCycle Methods 
오직 Class based component 에서만 가능하다.  
이미 정의되어 있는 메서드들을 사용하며, 크게 
1. Mounting
1. Updating
1. Unmounting
세 단계로 나누어 각각 몇가지 메서드들을 가지고 있다. 아래는 대표적으로 알아두어야 할 몇가지.

1. componentDidMount()
1. componentDidUpdate(prevProps, prevState)
1. componentWillUnmount()

## LocalStorage
- 모든 게 문자열로 저장된다.
    1. 숫자로 set 해도 문제 없이 저장되지만, 나중에 get 해보면 문자열로 변환되어 저장된 것을 확인할 수 있다. 
    1. 배열이나 객체를 localStorage에 저장하고 싶다면 `JSON.stringify()` 을 이용하고 나중에 get 했을 때 `JSON.parse()` 로 다시 변환해주어야 한다.

# Webpack
asset bundler

1. third part library 관리
1. js 파일을 여러 개의 파일로 나누어 관리 가능 (organize js files). Webpack 을 통해 앱을 실행시키면, 결국 하나의 자바스크립트 파일이 됨 (bundle.js).
1. `ES6 Import` 를 통해 다른 js 파일 내용을 가져오거나, npm 을 통해 설치된 외부 라이브러리를 쓰기 편하게 해줌. 
1. Babel 도 대신 돌려줌.

## Avoid Global Modules
라이브러리를 Global 로 설치하면, 이 프로젝트를 다른 사람이 받았을 때, 필요한 모든 의존 라이브러리를 알 수 없게된다. 그리고, 만약 각 프로젝트마다 다른 버전의 라이브러리를 쓰고 싶을 때도 문제가 된다. 따라서 최대한 Global 모듈은 설치하지 않는 게 좋다.

1. yarn 으로 설치한 글로벌 모듈 제거 (live-server 와 babel-cli 를 제거할 때)
`yarn global remove live-server babel-cli`
1. npm 으로 설치한 글로벌 모듈 제거
`npm uninstall -g babel-cli`

그런데 이렇게 글로벌이 아닌 프로젝트별 로컬 설치를 하게 되면, 터미널 창에서 `babel ~ ` 같이 곧바로 접근할 수 없게 된다. 따라서 `package.json` 파일에 따로 `"scripts"` 를 작성해서 원하는 모듈을 돌리는 명령어를 만들어야 한다.

```json
"scripts": {
  "serve": "live-server public/",
  "build-babel": "babel src/app.js --out-file=public/scripts/app.js --presets=env,react --watch"
},
```

명령어를 만들었다면 `yarn run build` 혹은 `npm run build` 같이 마지막에 명령어를 붙인 `run` 커멘드로 실행할 수 있다.

## installing & configuring Webpack

> 주의!: jsx 가 포함된 기존 react 자바스크립트 코드를 곧바로 webpack 으로 돌릴 수 없으니, 단순 console.log 만 있는 새로운 파일을 만들고 그 파일을 대상으로 해야된다.

1. webpack 설치: `yarn add webpack@3.1.0`
2. **webpack.config.js** 파일을 project root 경로에 만들기
3. 설정 파일 채우기
    1. entry
    2. output
        1. path : 앞의 두 속성과 달리, 상대경로가 아닌 **절대경로**를 입력해야 함에 주의. 자바스크립트의 built-in 속성인 `__dirname` 으로 현재 경로를 구하고, 그 경로를 `node.js` 가 지원하는 `path.join()` 으로 원하는 경로로 조합해서 쓸 수 있다. 물론 `path.join()`대신 ES6 template string 으로 만들어도 된다. 

## ES6 Import/Export
Webpack 에서는 ES6 import 와 export 를 사용해 여러 .js 파일을 한 파일로(주로 메인 파일인 app.js 파일.) 불러와 사용할 수 있다. import/export 방식은, 변수와 함수 등의 이름이 겹쳐서 생기는 문제를 피하기 위해 파일별로 각각 별도의 scope 를 가지고 있다. 따라서 어떤 함수,클래스,변수를 내보낼 지 export 로 따로 명시해야 하고, import 하는 파일에서도 어떤 걸 가져올 지 명시해야 한다.

1. named export
    1. 변수마다 각각 export 할 때: `export const name1 = ...`
    1. 모아서 한 번에 export 할 때: `export {name1, name2}`
1. default export
    1. 다른 named export 가 없을 때: `export default xx`
    1. 다른 named export 가 있을 때: `export {name1, name2, xx as default}`
1. named import
    1. `import {name1, name2} from 'path'`
1. default import
    1. 다른 named import 가 없을 때: `import xx from 'path'`
    1. 다른 named import 가 있을 때: `import xx, {name1, name2} from 'path'`

- import 할 때 이름을 바꾸고 싶다면, default 는 그냥 원하는 이름으로 import 하면 되고, named 는 as 키워드를 써야 한다.
- default export 는 named export 처럼 변수 정의 앞에 export default 붙여서 export 할 수 없다. 다만 익명 함수이거나, 클래스라면 가능하다.

## importing npm Modules
- `./` 를 붙이지 않고 곧바로 경로를 입력하면 webpack 이 알아서 `node_modules` 에서 찾아본다.

- 3rd party library 의 경우, npm 공식 사이트에서 ES6 방식의 import 를 어떻게 해야하는지 설명하지 않는 경우가 있다. 그럴 경우에는 해당 라이브러리의 docs 를 직접 찾아가서 named import 를 쓸 지, default import 를 쓸 지 찾아보는 게 좋다.

- React 의 경우, 제대로 import 하면 바로 쓸 수는 있지만, jsx 해석을 위한 babel 설정은 다시 해줘야 한다.

## Setting up Babel with Webpack
1. **babel-core** 설치
    - babel-cli 가 command-line 으로 babel 을 실행시켜주는 것이었다면, **babel-core** 은 babel 을 webpack 과 같은 다른 도구에서 쓸 수 있도록 도와준다.
1. **babel-loader** 설치
    - webpack plugin 이며, webpack 이 어떤 파일을 봤을 때 babel 을 실행시켜야 하는 지 webpack 에게 알리는 역할을 한다.
1. webpack.config.js 파일에 `module` 부분을 작성해 어떻게 loader 를 사용할지 설정한다.
    - [공식webpack 문서](https://webpack.js.org)
    - `test` 부분에는 어떤 파일에 loader 를 적용시킬지 정규표현식으로 작성한다.
    - `exclude` 부분에는 어떤 파일을 제외할지 정규표현식으로 작성한다.
1. 위까지의 과정으로 Babel 을 어떤 파일을 대상으로 실행할지는 설정했지만, 어떤 presets 을 가지고 Babel 을 돌릴 지는 프로젝트 root 경로에 `.babelrc` 라는 파일을 만들어 설정해주어야 한다. 
    ```json
    // .babelrc 파일
    {
      "presets": [
        "env",
        "react"
      ]
    }
    ```

1. 모든 설정을 마치고 다시 webpack 을 돌리면 (`yarn run build`) 이제 JSX 도 잘 해석하는 것을 알 수 있다. 변환된 파일의 길이가 상당히 긴 것은, production mode 로 갔을 때 개선될 수 있음을 알고 있자.

## Source Maps with Webpack
소스 코드에서 어떤 에러가 발생하면, 브라우저의 개발자 도구만으로는 에러를 파악하기 힘들다. 왜냐하면 브라우저가 인식하는 자바스크립트 파일은 webpack 을 거쳐 변환된 파일이고, 우리는 변환 전 파일들만을 코딩했기 때문이다. webpack 설정 파일에 `devtool` 이라는 속성을 추가해서 이 부분에 도움 받을 수 있다. (어떤 devtool 을 사용할 수 있는지는 공식 webpack document 를 참고하자. 이 프로젝트에서는 `devtool: 'cheap-module-eval-source-map'` 을 사용했다.)

## Webpack devServer
live-server 대신 webpack 자체 라이브 업데이트 서버를 돌리면 `index.html` 과 webpack 을 동시에 실행시키고 라이브 업데이트 할 수 있다. `devServer` 라는 속성을 사용한다. 
> Webpack devServer 를 이용하면, 빠른 대신 물리적인 `bundle.js` 파일을 볼 수 없게 된다. 파일을 생성하고 싶다면 따로 `build` 관련 세팅을 해야할 것이고, 그게 나중에 배울 production 모드의 빌드파일이 될 것이다.

## ES6 Class properties
`yarn add babel-plugin-transform-class-properties@6.24.1` (버전은 다를 수 있음.)

최신 webpack 플러그인 for Class Syntax  
[babeljs.io](babeljs.io) 의 문서에서 볼 수 있는 State 2 preset 의 `transform-class-properties` 플러그인이다.  

1. `consturctor()` 없이 그냥 클래스 내에서 instance Property 를 만들고, 원래 못쓰던 화살표 함수를 이용해 따로 `constructor` 내에서 `.bind(this)` 해줄 필요없이 메서드를 만들 수 있다. 