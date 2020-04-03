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

> 새로운 웹팩 버전에서는 devtool 을 쓰기 보다 `SourceMapDevToolPlugin` 영역을 사용하기를 권장하고 있다. 자세한 사항은 [공식문서](https://webpack.js.org/configuration/devtool/#root) 를 참고하자.

## Webpack devServer
live-server 대신 webpack 자체 라이브 업데이트 서버를 돌리면 `index.html` 과 webpack 을 동시에 실행시키고 라이브 업데이트 할 수 있다. `devServer` 라는 속성을 사용한다. 
> Webpack devServer 를 이용하면, 빠른 대신 물리적인 `bundle.js` 파일을 볼 수 없게 된다. 파일을 생성하고 싶다면 따로 `build` 관련 세팅을 해야할 것이고, 그게 나중에 배울 production 모드의 빌드파일이 될 것이다.

## ES6 Class properties
`yarn add babel-plugin-transform-class-properties@6.24.1` (버전은 다를 수 있음.)

최신 webpack 플러그인 for Class Syntax  
[babeljs.io](babeljs.io) 의 문서에서 볼 수 있는 State 2 preset 의 `transform-class-properties` 플러그인이다.  

1. `consturctor()` 없이 그냥 클래스 내에서 instance Property 를 만들고, 원래 못쓰던 화살표 함수를 이용해 따로 `constructor` 내에서 `.bind(this)` 해줄 필요없이 메서드를 만들 수 있다. 

# Using a Third-party Component

## Passing Children to Component

Child Component 를 `import` 해서 쓰는 방법 외에도, 어떤 컴포넌트에서 사용할 jsx 를 끼워넣는 방법이 더 있다.

1. `props` 에 jsx 형태를 통째로 넘기는 방법이 있다.

```jsx
const Layout = (props) => {
  return (
    <div>
      <p>header</p>
      {props.content}
      <p>footer</p>
    </div>
  );
};

const template = (
  <div>
    <h1>Page Title</h1>
    <p>This is my page</p>
  </div>
);

ReactDOM.render(<Layout content={template} />, document.getElementById('app'));
```

2. self closing tag 대신에, open, close tag 가 따로 있는 형태로 바꾼 후, 그 태그 사이에 jsx 를 통째로 넣으면 그 outer tag component 내에서 `{props.children}` 이라는 built-in props 로 접근, 렌더링이 가능하다. (Vue 에서의 slot 과 유사한 기능인듯.)

## React-Modal
```jsx
const OptionModal = (props) => (
  <Modal
    isOpen={!!props.selectedOption}
    contentLabel="Selected Option"
    onRequestClose={props.handleClearSelectedOption}
  >
    <h4>Selected option</h4>
    {props.selectedOption && <p>{props.selectedOption}</p>}
    <button onClick={props.handleClearSelectedOption}>Okay</button>
  </Modal>
);
```
- `!!props.selectedOption` 처럼 앞에 느낌표를 두 개 붙이면, 해당 변수가 가진 값을 적절한 boolean 값으로 변환시킬 수 있다. 예를 들어, `undefined` 는 `false` 로, 빈 문자열은 false, 그 외 문자열은 `true` 가 된다. 
- `onRequestClose` 속성은, 클라이언트 이용자가 ESC 키나, 모달밖 배경을 클릭했을 때 어떤 함수를 호출해야 하는 지 정할 수 있다. 즉, 주로 Modal 을 끌 수 있도록 도와준다. 

# Styling React

## Setting up Webpack with SCSS

### webpack 으로 css 파일 관리하기. 
2가지 라이브러리가 필요하다.
1. **style-loader**: 자바스크립트 안에 있는 css 내용을 DOM 에 `style` 태그로 넣어줌으로써 실질적으로 css 가 적용되도록 한다.
2. **css-loader**: css 파일들을 javascript 와 어울릴 수 있도록 변환해준다.
3. 위 라이브러리들을 `yarn add` 로 추가한다.
4. 그리고 webpack 설정 파일을 수정한다. 정규표현식으로 webpack 이 `.css` 파일을 보면 어떻게 처리할 지를 정하는데, CSS 파일에 적용할 라이브러리가 하나가 아니라 2개 이상이기 때문에, `loader` 가 아닌 `use` property 에 배열의 형태로 라이브러리를 넣어야 한다.
5. 그리고 나서, `app.js` 파일에 CSS 파일을 `import` 하면, webpack 이 설정에 따라 해석하게 된다. 

> 순서주의! : 사실 왜 그런지 이해하지 못했지만, style-loader 를 css-loader 보다 뒤 순서로 넣으면, 제대로 css 를 처리하지 못한다. 무조건 style-loader 가 먼저오도록 배열에 작성하자..

```json
module: {
  rules: [{
    loader: 'babel-loader',
    test: /\.js$/,
    exclude: /node_modules/
  }, {
    test: /\.css$/,
    use: [
      'style-loader',
      'css-loader'
    ]
  }]
},
```

## scss 사용
sass 와 scss 는 사용문법에서 약간 차이가 있을 뿐, 같은 거라고 보면 된다. scss 를 사용하면 프로그래밍 언어처럼 변수를 쓸 수 있고, 마치 javascript 처럼 다른 scss 파일 내용을 import 해서 합쳐 쓸 수 있다(모듈화). css 대신 scss 를 쓰기 위해 sass-loader 와 node-sass 를 설치하고 설정하자.

### 외부 라이브러리 갈아엎기.
> **scss 사용** 부분에서 라이브러리를 내 임의로 모두 갈아치웠다. sass-loader 와 node-sass 가 강사가 하는 것과 달리 기존 라이브러리들과 제대로 호환되지 않았기 때문. 어차피 내가 스스로 개발할 때는 최신버전으로 해야할 확률이 높으니, 강의에서처럼 일일이 버전명을 치지 않고 최신버전으로 모든 것을 맞추기로 했다. 결과적으로 성공했지만, 기록해놔야 할 것들이 꽤 있다. 

1. 결과적으로 직접 코드를 쳐 수정한 파일은 `package.json` 과 `.babelrc` 두 개다.
1. 가장 큰 변경사항은 기존 `babel-core` 이라는 **6** 버전대의 Babel 이, **7** 버전대의 Babel 이 되어 **@** 와 **/** 이 사용된 `@babel/core` 로 바뀌었고, 이 core 에 맞춰 다른 모든 babel 관련 라이브러리, preset 및 plugin 들이 모두 유사한 형태의 다른 라이브러리로 이름이 바뀌거나 아예 다른 이름이 되었다. > 참고: [도움되는 github 질의응답](https://github.com/babel/babel/issues/6808)

아래는 강의를 따라갔을 때의 `package.json` 상태와, 최신 버전으로 업데이트 한 `package.json` 상태다.

```json
// 변경하기 전
"babel-cli": "6.24.1",
"babel-core": "6.25.0",
"babel-loader": "7.1.1",
"babel-plugin-transform-class-properties": "6.24.1",
"babel-preset-env": "1.5.2",
"babel-preset-react": "6.24.1",
"css-loader": "0.28.4",
"live-server": "^1.2.1",
"react": "16.0.0",
"react-dom": "16.0.0",
"react-modal": "2.2.2",
"style-loader": "0.18.2",
"validator": "8.0.0",
"webpack": "3.1.0",
"webpack-dev-server": "2.5.1"
```

```json
// 변경 후
"@babel/cli": "^7.8.4",
"@babel/core": "^7.8.7",
"@babel/plugin-proposal-class-properties": "^7.8.3",
"@babel/preset-env": "^7.8.7",
"@babel/preset-react": "^7.8.3",
"babel-loader": "^8.0.6",
"css-loader": "^3.4.2",
"live-server": "^1.2.1",
"node-sass": "^4.13.1",
"react": "^16.13.0",
"react-dom": "^16.13.0",
"react-modal": "^3.11.2",
"sass-loader": "^8.0.2",
"style-loader": "^1.1.3",
"validator": "^12.2.0",
"webpack": "^4.42.0",
"webpack-cli": "^3.3.11",
"webpack-dev-server": "^3.10.3"
```

이 아래는 변경 후 `.babelrc` 파일 내용이다. 기존 `babel-plugin-transform-class-properties` 이 아예 이름이 바뀐 것을 확인할 수 있다.

```json
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
  "plugins": [
    "@babel/plugin-proposal-class-properties"
  ]
}
```

결과적으로 컴파일된 걸 보면 최신버전의 webpack과 babel 을 활용한 것이 hidden modules 개수가 많이 줄어든 것 같으니 더 성능이 좋다고 추측된다.

## SCSS
`@import` 구문으로 다른 scss 파일을 가져올 수 있다. 부분적인 코드(partial)를 담고 있는 scss 파일명은 언더스코어(_) 로 시작한다. 이 부분적인 scss 파일을 one entry point SCSS 파일(중심파일)에 `@import` 할 때, 앞에 언더스코어부분을 생략하도록 되어있다.

### rem
이용자가 브라우저 상에서 폰트 크기를 조절할 수 있도록 하거나 기기별로 다른 설정을 지원하기 위해서는 단순 픽셀단위가 아닌 상대적인 크기를 폰트 크기로 지정할 필요가 있다. 따라서 **rem** 을 사용한다. 그런데 일반적인 브라우저 폰트 기본 사이즈는 16px 이다. 16px 을 기준으로 하면, 크기 조절을 할 때 계산하기가 너무 힘들기 때문에, 보통 `html` 태그의 css 속성에 font-size 를 0.625%, 즉 10px 로 해놓고, 그것에 대한 상대 크기를 조절하자. 물론 `body` 태그에 다시 1.6rem 으로 지정해서, 브라우저 기본 값을 되찾아주자.

```css
html {
  font-size: 62.5%;
}

body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 1.6rem;
}
```

### BEM
**BEM**, Block Element Modifier Naming Convention   
클래스 이름 붙이는 네이밍 컨벤션이다. 

1. `header__title` 같이, header 같은 큰 단위를 블럭, 그 안에 있는 title 같은 것을 element 라고 생각하며 __ 를 이용해 이름 붙인다.

1. `button--link` 같이, 어떤 button 의 basic setting 에 추가적으로 **modified** 된 버전의 css 를 작성하면, -- 를 붙인다.

자세한 내용이 필요하면 찾아보자

### Reset CSS
브라우저마다 기본 스타일링이 다르기 때문에, 모든 브라우저에서 똑같은 경험을 하게 하려면 먼저 모든 css 를 reset 해줄 필요가 있다. 정말 다양한 부분에서 다르기 때문에 직접 코딩하기에는 무리가 있고, `Normalize.css` 같은 이미 만들어진 것을 가져다 쓰는 게 좋다.

`yarn add normalize.css` 로 설치한 후, `app.js` 에서 `import` 하자. 그리고 이전에 sass 이용을 위해 바꿔뒀던 sass 관련 loader 의 정규표현식을 `test: /\.s?css$/,` 로 바꿔서 scss 와 css 모두 해당되도록 해주자.

## word-break: break-all
사용자가 지나치게 긴 글자를 입력했는데, 심지어 띄어쓰기도 없이 길게 이어졌다면, 주어진 박스 크기를 뚫고 나갈 수 있다. 따라서 css 에 `word-break: break-all` 을 써서 한 단어라도 줄 바꿈이 되도록 하는 게 좋다.

# React-Router

> [ReactTraining/react-router 사이트] (https://reacttraining.com/react-router) 

## 설치

1. web 버전은 `yarn add react-router-dom`
2. Native 버전은 `yarn add react-router-native`



## 역사/작동원리

1. 자바스크립트를 이용한 라우팅은 React 가 처음 도입한 것은 아니고, 그 전에도 이미 많이 활용되던 기술이다. 특히 HTML5 의 `history` api 를 이용할 수 있게 되면서 사용이 더 용이해졌다. 
2. 전통적인 **서버 사이드 라우팅** 과 상반되는 **클라이언트 사이드 라우팅**이 된 것으로, 페이지마다 서버에 요청하지 않고, 주소창은 구분을 위한 url 일 뿐, 실질적으로 각 주소마다 사용자에게 보여주는 파일은 오직 `index.html` 하나다. 즉, 어떤 경로로 접근하든 `index.html` 이 주어지고, 자바스크립트가 그 주소에 맞게 어떤 컴포넌트를 보여줄 지 동적으로 결정한다. 



### 설정 코드

1. `app.js` 파일에 `react-router` 와 관련된 설정을 한다. `exact` 설정을 해야 앞부분이 겹친다고 모두 렌더링되지 않고, 그 주소에 꼭 맞는 페이지가 로드된다. 물론 일부러 겹치는 모든 게 다 나오게 하는 경우도 있다.

```jsx
// app.js 파일
import { BrowserRouter, Route } from 'react-router-dom';
// ...
const routes = (
  <BrowserRouter>
    <div>
      <Route path="/" component={ExpenseDashboardPage} exact={true}></Route>
      <Route path="/create" component={AddExpensePage} ></Route>
    </div>
  </BrowserRouter>
);

ReactDOM.render(routes, document.getElementById('app'));
```



1. webpack 설정파일에 `devServer` property 에 `historyApiFallback: true` 를 부여한다. 앱의 어떤 경로를 get 하는 것에 실패했을 때(기존 서버 사이드 라우팅 방식에 비교하면, 존재하지 않는 파일 경로는 실패한다.), 무조건 `index.html` 파일을 주도록 할 수 있다.

```js
// webpack.config.js
devServer: {
    contentBase: path.join(__dirname, 'public'),
    historyApiFallback: true
}
```



## 404 페이지

맨 마지막 순서로 `path` 가 지정되지 않은 `<Route>` 태그를 두면, 앞서 설정된 Route 들 모두와 일치하지 않을 경우 404 페이지가 뜨도록 할 수 있다. 그런데, 단순히 맨 마지막에 `path` 없이 두면, 없는 페이지 상황 뿐 아니라 모든 경로에 다 뜨게 된다. (빈 루트는 어떤 것에든 일치하기 때문)    

따라서 `react-router` 가 제공하는 컴포넌트 중 하나인 `<Switch>` 를 써야 한다. 스위치 컴포넌트를 써야, 매칭되는 한 가지 경우의 수를 찾았을 때, 그 페이지를 렌더링 하는 것에서 멈추고 더 탐색하지 않는다. 원래 `<BrowserRouter>` 가 하나의 요소만 허용했기 때문에 단순 div 태그로 감쌌었는데, Switch 로 바꿔주기만 하면 된다. 



```jsx
import { BrowserRouter, Route } from 'react-router-dom';
// ...
const routes = (
  <BrowserRouter>
    <Switch>
      <Route path="/" component={ExpenseDashboardPage} exact={true}></Route>
      <Route path="/create" component={AddExpensePage} ></Route>
      <Route path="/edit" component={EditExpensePage} ></Route>
      <Route path="/help" component={HelpPage} ></Route>
      <Route component={NotFoundPage} ></Route>
    </Switch>
  </BrowserRouter>
);
```



## Linking between routes

단순 html `<a>` 태그로 라우팅을 하면, 브라우저 기본 설정 상 무조건 새로고침을 해서 처음부터 다시 페이지를 로드한다. 그럼 SPA 의 장점이 사라지므로, 경로는 이동하되 a 태그는 누르지 않은 것처럼 되어야 한다. 그리고 이 기능을 react-router 가 `<Link>` 나 `<NavLink>` 를 통해 제공한다. `<NavLink>` 가 제공하는 기능이 더 많아 복잡하므로, 단순하게는 Link 를 사용해서 라우팅할 수 있다.

```jsx
<Link to="/">Go Home</Link>
```



### Layout?

`<Switch>` 와 같은 레벨에 다른 컴포넌트를 넣어서, 언제나 렌더링 되는 header 나 footer 같은 걸 구현할 수 있다.



## Query Strings and URL parameters

`<Route>` 가 무조건 `props` 로 받는 history, location, match 속성들을 이용해서 여러가지 라우팅 관련 일을 할 수 있다.



# Redux

> [공식문서](https://redux.js.org)



기본적인 생성 코드는 다음과 같다. `createStore` 함수가 받는 `state` 매개변수는, 현재 상태의 state 를 말한다. 맨 처음 생성되었을 때는 아무런 state 가 없으므로, default Object 인 `{count: 0}` 을 넣고 테스트해 보았다. `getState` 로 현재 store 의 state를 받아볼 수 있다.

```js
import { createStore } from 'redux';

const store = createStore((state = { count: 0 }) => {
  return state
});

console.log(store.getState());
```



## Dispatching Actions

- Action 은 Redux Store 에 보내지는 **Object** 이다. 이 Object 는 어떤 종류(type)의 액션을 할지를 `type` property 에 담아 `store` 에 `dispatch` 한다. 

### Naming convention

보통 action 의 type 이름은 모두 대문자(uppercase) 를 쓴다. 한 단어로 쓸 수 없는 경우, 언더스코어(_) 를 써서 구분한다. 

### Using in store object

redux 의 createStore 가 받는 함수는, `state` 뿐 아니라 `action` 도 받는다. 그리고 함수 내에서, if 문을 이용해서 `if (action.type === 'ACTION_NAME')` 과 같이 분기문을 작성해도 되겠지만, 얼마나 더 action 의 수가 많아질 지 모르는 상황이기 때문에 보통 `switch` 문을 많이 쓴다.

```js
import { createStore } from 'redux';

const store = createStore((state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return {
        count: state.count + 1
      };
    default:
      return state;
  }

  // if (action.type === 'INCREMENT') {
  //   return {
  //     count: state.count + 1
  //   };
  // } else {
  //   return state;
  // }
});

console.log(store.getState());

store.dispatch({
  type: 'INCREMENT'
});

console.log(store.getState());
```



## Subscribing and Dynamic Actions

실제 어플리케이션을 만들었을 때, Store 의 상태가 변할 때마다 일일이 `getStore` 로 찍어볼 수는 없다. 변화가 생기면 자동으로 인식하고 그 변화에 맞춰서 새로 렌더링해줄 필요가 있기 때문이다. 그래서 변화를 인지하는 `subscribe()` 를 사용한다. 이 `subscribe` 메서드가 반환하는 것이 subscribe 를 중단하는 함수이기 때문에, 변수에 저장해놨다가 그 변수를 호출하면 그 시점에서 subscribe 가 중단된다.

```js
const unsubscribe = store.subscribe(() => {
  console.log(store.getState());
});

store.dispatch({
  type: 'INCREMENT'
});

unsubscribe(); // 중단

store.dispatch({
  type: 'DECREMENT'
});
```



Action 에 `type` 외에 다른 property 를 만들고 그것을 활용할 수 있다. 

```js
// store 내 switch 문
switch (action.type) {
    case 'INCREMENT':
        const incrementBy = typeof action.incrementBy === 'number' ? action.incrementBy : 1;
        return {
            count: state.count + incrementBy
        };
}

store.dispatch({
  type: 'INCREMENT',
  incrementBy: 5
});
```

## Action Generator

ES6 의 Object destructuring 을 이용하면, 보다 깔끔하고, 오타를 방지하며, 덜 반복적인 방법으로 action 을 정의하고 이용할 수 있다.  (함수는 자동완성이 되니까)

1. dispatch 에 직접 Object 를 넘기지 않고, Object 를 반환하는 함수를 호출한다.
2. 그 Obejct 를 반환하는 함수는 매개변수로 해당 Action 을 위한 객체를 받지만, 아무것도 넘기지 않고 호출되도 작동할 수 있도록  default 값이 빈 Object 인 함수다. 그런데, Object destructuring 에서 좌변에도 default 값을 가질 수 있다는 점을 이용해, 객체가 인자로 주어지지 않았을 경우의 기본 값을 설정할 수 있다. 

```js
const incrementCount = ({incrementBy = 1} = {}) => ({
    type: 'INCREMENT',
    incrementBy
});

// ...

store.dispatch(incrementCount()); // 객체를 넘겨주지 않아도 정상적으로 실행됨.
```



## Reducer

단어의 어감은 무서워 보이지만 그냥 Action 이 들어왔을 때 정작 State 를 어떻게 변화시킬 지 결정하고 변화시키는 **Pure Function** 이 Reducer 다. 즉, `createStore` 의 인자로 들어가는 함수가 Reducer 다. 여기서 Pure Function 이란, 함수의 내용이 함수 밖의 Scope 와 전혀 연관이 없는 함수로, Output 도 오로지 Input 만을 가지고 만들어지는 함수를 뜻한다. (함수형 프로그래밍에서도 자주 쓰이는 개념이다. ) 

어플리케이션이 하는 일이 많아질수록, `createStore` 는 여러개의 Reducer 를 가질 수 있고, 따라서 `createStore` 내에서 함수를 정의하기 보다는 따로 분리해서 Reducer 들을 만든 후, 나중에 그 함수들을 `combindReducers` 로 합쳐서 쓰는 식으로 구조를 짠다.

Reducers 의 특징은, 

1. Pure Functions 이다.
2. Reducer 는 결코 state 와 action 을 직접적으로 변형시키지 않는다.



## ES6 Spread Operator in Reducers

Pure Function 이라는 Reducer 의 특징상, 관리하고 있는 배열이 있고, 그 배열에 원소를 추가하고 싶을 때, `.push` 메서드를 쓰면 안된다. 따라서 새로운 배열을 만들어 `return` 해야 한다. 주로 아래 2가지 방식이 쓰인다.

1. `.concat` 메서드를 대신해서 쓴다.
2. Spread Operator 을 써서 복사한다.



## Object destructuring and Redux

결국 redux 의 store 는, 각 reducer 가 관리하고 있는 State 를 (배열일수도, 객체일수도..) 통째로 갈아치우는 방식으로 작동한다. 즉, State 의 일부 property 만 바꾸려고 해도 나머지 모든 property 까지 합쳐서 `return` 해야한다. 그런데 모든 property 를 일일이 타이핑할 수는 없기 때문에, Array destructuring 혹은 Object destructuring 을 잘 활용해야 한다. 특히 앞쪽에 기존 state 를 모두 destructuring 해서 전부 복사한 뒤, 뒤쪽에 같은 key 를 가진 property(변화가 필요한 property) 를 재정의함으로써 덮어씌우는 방식이 많이 이용된다. 



## Timestamp

1970년 1월 1일 기준(unix epoch) 부터 milliseconds 단위로 증가해온 timestamp 로 날짜를 구분한다. **음수**도 지원하며, 그 경우에는 1970 년 이전이 된다.



### .sort() 와 compare function

쉽게 생각하자면, 2개의 인자 중 첫번째가 -1, 두번째가 1 이라고 우선 생각하자.(-1 이 1보다 작다.) 그리고 아래 조건문을 작성한 뒤, 그 조건문이 return 하는 것이 -1 이면 첫번째가 -1 이었으니 그게 앞에 서고, return 하는 것이 1 이면 두번째 것이 1 이었으니 두번째가 앞에 선다. 

# React with Redux

## High Order Component (HOC)
다른 컴포넌트를 생산하는 컴포넌트를 HOC 라고 부른다. 즉, 컴포넌트를 return 하는 함수라고 생각하면 된다. HOC 는 다른 함수로 감싸져서, 그 외부 함수가 인자로 받아오는 어떤 컴포넌트를 내부 HOC 함수가 상황에 맞게 그 컴포넌트를 렌더하는 방식으로 사용된다. 즉, 바깥 함수가 아닌 안에 있는 함수가 HOC Component 이다. Redux 가 React 에서 쓰일 수 있는 방식도, 비록 그냥 주어진 라이브러리를 쓰면 되긴 하지만, **내부적으로는 HOC 패턴**으로 구현된다. Redux Store 를 쓸 수 있는 컴포넌트로 재탄생시키는 것이다. 

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const Info = (props) => (
  <div>
    <h1>Info</h1>
    <p>The info is: {props.info}</p>
  </div>
);

const withAdminWarning = (WrappedComponent) => {
  return (props) => (
    <div>
      {props.isAdmin && <p>This is private info. Please don't share!</p>}
      <WrappedComponent {...props} />
    </div>
  );
};

const requireAuthentication = (WrappedComponent) => {
  return (props) => (
    <div>
      {props.isAuthenticated ? (
        <WrappedComponent {...props} />
      ) : (
          <p>Please Login</p>
        )}
    </div>
  );
};

const AdminInfo = withAdminWarning(Info);
const AuthInfo = requireAuthentication(Info);

// ReactDOM.render(<AdminInfo isAdmin={true} info="There are the details" />, document.getElementById('app'));
ReactDOM.render(<AuthInfo isAuthenticated={false} info="There are the details" />, document.getElementById('app'));
```



## Connecting Store and Component with React-Redux

`react-redux` 라는 라이브러리를 설치해서 이용한다. 그리고 메인 파일인 `app.js` 에서, `Provider` 를 import 해서 기존 메인 라우트 컴포넌트를 감싸준다. 이때 `Provider` 에 redux store props 를 넘겨주자. 이렇게 하고나면, 이제 `Provider` 안의 모든 컴포넌트에서 원할 때 redux store 를 연결해서 사용할 수 있게 된다.

```jsx
import { Provider } from 'react-redux';

// ...

const jsx = (
  <Provider store = {store}>
    <AppRouter />
  </Provider>
);

ReactDOM.render(jsx, document.getElementById('app'));
```



### Store 를 사용하고자 하는 Component 에서 **connect** 로 store와 연결하기

어떤 컴포넌트에서 redux store 를 활용하고자 한다면, 우선 `react-redux` 라이브러리의 `connect` 함수를 import 해야 한다. 이 `connect` 함수는 곧바로 HOC 를 반환하지는 않고, 앞서 배운 HOC 의 Outer function 과 같은 것을 반환한다. 즉, `connect` 의 반환 함수에 감싸고자 하는 **컴포넌트(wrappedComponent, 즉, redux 에 접근하고자 하는 컴포넌트)를 인자로 넣어** 또다시 호출해주어야만 HOC 가 정상적으로 작동한다.  그럼 **`connect` 의 함수호출부 괄호에는 어떤 인자가 들어갈까?** 바로, 감싸진 component 에게 props 로 넘겨질 객체다. 물론 우리가 넘겨주고자 하는 객체는 redux store 의 state 다. 그래서 이 connect 호출부의 인자는 store의 state 를 기본인자로 받는 또다른 함수이다. **왜 함수냐?** 는 조금 더 생각해보면 이해할 수 있다. 계속해서 데이터가 바뀌고 있는 상황일 때, state 가 변하면 그때그때 함수로 새로 호출해줘야만 최신 state를 가져올 수 있다는 것으로 해석하면 된다.(실제로 `store.subscribe()` 나 `getState()` 같은 함수 호출 없이도 reactive 하게 컴포넌트가 다시 렌더링된다.) 아무튼, 이 `connect` 인자 함수는 wrappedComponent 가 props 로 받을 객체를 key-value 로 설정해 반환한다. (store의 모든 state 가 필요하지 않을테니, 필요한 부분만 다시 key-value 로 만들어 props 로 넘기는 것이다.)

```jsx
import React from 'react';
import { connect } from 'react-redux';

const ExpenseList = (props) => (
  <div>
    <h1>
      Expense List
    </h1>
    {props.expenses.length}
  </div>
);

const ConnectedExpenseList = connect((state) => {
  return {
    expenses: state.expenses
  };
})(ExpenseList);

export default ConnectedExpenseList; // ExpenseList 컴포넌트가 HOC 를 통해 redux store 와 연결된 상태인 ConnectedExpenseList 라는 새로운 컴포넌트가 되고, 그것을 다른 컴포넌트에서 사용할 수 있도록 export 됨.
```



실전예제에서는, `connect` 함수를 곧바로 export default 해버리고, `connect` 의 인자로 들어가는 함수도 `mapStateToProps` 같은 이름의 함수로 따로 분리하는 경우가 많다. (함수명에서 보다시피 store 의 state 중 일부를 wrappedComponent 의 props 로 변환하는 과정이다.)

```jsx
const mapStateToProps = (state) => {
  return {
    expenses: state.expenses
  };
};

export default connect(mapStateToProps)(ExpenseList);
```

데이터를 어떤 규칙을 따라 filtering 하거나 sorting 할 필요가 있다면, 같은 파일 내에서 규칙을 작성하여 변환해도 되지만 따로 `selectors` 같은 폴더를 만들어 state 를 조건에 따라 변환하는 함수를 작성하면 좋다. 



```jsx
import selectExpense from '../selectors/expenses';

// ...
const mapStateToProps = (state) => {
  return {
    expenses: selectExpense(state.expenses, state.filters)
  };
};
```



## store 와 `connect` 된 컴포넌트에서 `dispatch` 사용하기

`connect` 된 컴포넌트의 props 에는, `mapStateToProps` 로 넘겨준 state 외에도, store 의`dispatch` 메서드도 존재한다. 즉, 컴포넌트에서 곧바로 `dispatch` 할 수 있다. 물론 `dispatch` 의 인자로 넘겨줄 action generator 는 미리 만든 것을 가져와서 쓰는 게 좋다.

## Controlled Inputs for Filters

아래처럼 input 내용이 바뀔 때마다 store 의 `setTextFilter` 를 호출해줄 수 있다. `(props)` 대신에 `({dispatch})` 하면, 앞에 `props` 붙일 필요 없이 `dispatch` 사용가능하다.

```jsx
import React from 'react';
import { connect } from 'react-redux';
import {setTextFilter} from '../actions/filters'

const ExpenseListFilters = (props) => (
  <div>
    <input type="text" value={props.filters.text} onChange={(e)=> {
      props.dispatch(setTextFilter(e.target.value));
    }} />
  </div>
);

const mapStateToProps = (state) => {
  return {
    filters: state.filters
  };
};

export default connect(mapStateToProps)(ExpenseListFilters);
```



# Testing with JEST

- jest 는 facebook 에서 개발한, react 를 테스트 할 수 있는 라이브러리다.
- Test 의 목적은 인간의 손으로 할 수 없는 것을 테스트하는 게 아니라, 앱이 복잡해졌을 때, 일일이 사람이 할 필요 없이 테스팅을 하기 위함이다. 
- 공식문서가 아주 잘 되어 있기 때문에, 공식문서를 잘 활용하자. [공식문서](https://jestjs.io/docs/en/getting-started)

## 설치 & 실행

1. `yarn add jest`
2. `package.json` 파일의 scripts 에 `"test": "jest"` 추가
3. `yarn run test` 혹은 `yarn test` 로 검사 시작. test 는 워낙에 많이 쓰여, **`run` 이 생략가능**하다.



## test 만들기

1. `src` 폴더 아래에 `tests` 폴더 만들기. 
2. `tests` 폴더 안에 `add.test.js` 처럼 가운데 `.test` 가 들어간 파일을 만들어 사용.
3. 상황에 따라 `throw new Error()` 함수를 직접 작성할수도 있지만, Jest 가 제공하는 `expect` 와, 그 메서드를 잘 활용하는 것이 훨씬 효율적이다.

```js
const add =(a,b) => a + b;

test('should add two numbers', () => {
  const result = add(3,4);
  // 직접 에러를 발생시키는 함수를 만들 경우
  // if (result !==7) {
  //   throw new Error('You added 4 and 3. The result was ${result}. Expected 7');
  // }
  expect(result).toBe(7);
})
```



# 배포를 위한 준비 (Deploying Your Apps)

지금까지의 개발환경을 그대로 `build` 하면, webpack 이 만들어 주는 `bundle.js` 의 크기가 너무 크다. 그래서 배포전 최적화 작업이 필요하다.  

웹팩 버전에 따라 최적화 방법도 달라졌기 때문에, 공식문서를 참고하는 것이 좋다. [공식문서](https://webpack.js.org/guides/production/#root)   

사실 이 강의에서 사용한 웹팩 및 dependecy libraries 를 따르지 않고 중간에 임의로 수정했기 때문에, 웹팩의 새로운 버전에 대한 공부가 필요한 상황이다.. [웹팩공식문서](https://webpack.js.org/guides/getting-started/)  

일단은 강의 내용을 정리해보도록 하겠다.

## `-p` 프로덕션 모드

`webpack -p` 와 같이 뒤에 `-p` 플래그를 붙여줌으로써 webpack 에게 production 모드를 이용하도록 할 수 있다. 

```json
// package.json
"scripts": {
  "serve": "live-server public/",
  "build:dev": "webpack",
  "build:prod": "webpack -p",
  "dev-server": "webpack-dev-server",
  "test": "jest"
},
```

## 웹팩 설정파일 수정

이렇게만 해도 1메가바이트 넘게 축약되지만, production 모드와 development 모드에 따라 webpack.config.js 파일을 수정하도록 해야 더 많은 축약이 가능하다.   

그리고 이 방법을 적용하기 위해서는 우선 `webpack.config.js` 파일의 `module.exports` 를 객체가 아닌 함수로 만들어야 한다. 그래야만 개발환경과, 옵션에 관한 설정을 매개변수로 받을 수 있게 된다. [공식문서](https://webpack.js.org/configuration/configuration-types/#exporting-a-function)  

```js
// webpack.config.js
const path = require('path');

// module.exports = {
module.exports = (env) => {
  console.log(env) // package.json 의 스크립트를 수정해서 env 넘겨줄 수 있음
  const isProduction = env === 'production';
  return {
    entry: './src/app.js',
    output: {
      path: path.join(__dirname, 'public'),
      filename: 'bundle.js'
    },
    module: {
      rules: [{
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/
      }, {
        test: /\.s?css$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader'
        ]
      }]
    },
    devtool: 'cheap-module-eval-source-map',
    devServer: {
      contentBase: path.join(__dirname, 'public'),
      historyApiFallback: true
    }
  };
}
```

```json
//package.json 의 script 변경
"build:prod": "webpack -p --env production"
```

## devtool 변경

가장 먼저 손봐야할 것은 `devtool` 영역이다. production 모드에서는 빌드는 느리더라도 더 작은 사이즈의 번들을 만들어내는 devtool 을 사용하도록 설정하자.

```js
// webpack.config.js
devtool: isProduction ? 'source-map' : 'cheap-module-eval-source-map',
```

`source-map` devtool 을 사용해서 build 하면 훨씬 작은 크기의 번들과, 처음보는 `bundle.js.map` 이라는 파일도 받을 수 있는데, `.map` 파일은 개발자도구로 뜯어보지 않으면 사용되지 않는 것이므로 안심하자. `source-map` 은 실제로 output 을 내므로, `webpack dev-server` 대신 거의 처음에 설정했었던 `yarn run serve` 스크립트로 결과물을 실행해볼 수 있다. 



## css 분리

현상태의 세팅(style-loader사용)은, 모든 css 를 html 태그의 `style` 속성으로 inline 적용하고 있다. 따라서 모든 css 가 `bundle.js` 파일에 포함되어 있다. 이렇게 되어있으면 생기는 문제는

1. 번들의 크기가 크고
2. 자바스크립트 파일이 로드될 때까지 CSS 도 적용되지 못한다.

그래서 웹팩 설정을 바꿔서 번들은 자바스크립트만을 포함하고, css 는 따로 파일로 추출해서 만들어줄 수 있도록 해야 한다. 이를 위해서 사용할 라이브러리는 `extract-text-webpack-plugin` 이다. 그런데 이 플러그인은 웹팩 버전 3 까지만 지원하고 있다. 따라서 설치할 때 뒤에 `@next` 를 붙여서 설치하거나, 아예 다른 라이브러리인 `mini-css-extract-plugin` 을 사용하도록 하자.

1. 플러그인에 만들어질 css 파일 이름을 포함한 인스턴스를 등록하고, 설정을 수정하면 다음과 같다.

```JS
// webpack.config.js
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

// module.exports = {
module.exports = (env) => {
  console.log(env);
  const isProduction = env === 'production';
  return {
    entry: './src/app.js',
    output: {
      path: path.join(__dirname, 'public'),
      filename: 'bundle.js'
    },
    module: {
      rules: [{
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/
      }, {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            "css-loader",
            "sass-loader"
          ]
        })
        // use: [
        //   'style-loader',
        //   'css-loader',
        //   'sass-loader'
        // ]
      }]
    },
    plugins: [
      new ExtractTextPlugin("styles.css"),
    ],
    devtool: isProduction ? 'source-map' : 'cheap-module-eval-source-map',
    devServer: {
      contentBase: path.join(__dirname, 'public'),
      historyApiFallback: true
    }
  };
}
```

CSS 를 위한 source-map 을 적용하기 위해서는, 다른 devtool 과 loader 들에 추가적인 옵션 부여가 필요하다.

```js
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

// module.exports = {
module.exports = (env) => {
  console.log(env);
  const isProduction = env === 'production';
  return {
    entry: './src/app.js',
    output: {
      path: path.join(__dirname, 'public'),
      filename: 'bundle.js'
    },
    module: {
      rules: [{
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/
      }, {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'css-loader',
              options: {
                sourceMap: true
              }
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: true
              }
            }
          ]
        })
      }]
    },
    plugins: [
      new ExtractTextPlugin("styles.css"),
    ],
    devtool: isProduction ? 'source-map' : 'inline-source-map',
    devServer: {
      contentBase: path.join(__dirname, 'public'),
      historyApiFallback: true
    }
  };
}
```



## Express 로 간단한 웹서버 만들기

```js
// server/server.js
const path = require('path');
const express = require('express');
const app = express();
const publicPath = path.join(__dirname, '..', 'public');

app.use(express.static(publicPath));

app.get('*', (req, res) => {
  res.sendFile(path.join(publicPath, 'index.html'));
});

app.listen(3000, () => {
  console.log('Server is running')
});
```



## Heroku 로 배포

1. `heroku create *app-name` 으로 heroku remote repository 를 만들어준 후에, heroku 에 파일을 올리면 heroku 가 알아서 배포할 수 있도록 설정해주어야 한다. 
2. 우선 package.json 파일에 `start` 스크립트를 등록해 간단히 만든 express 서버가 돌아가도록 한다. 
3. 그리고 express 코드도, 포트 3000이 아닌  heroku 가 주는 포트번호를 쓰도록 수정한다. (`process.env.PORT`) 
4. 마지막으로 `.gitignore` 파일에 `index.html` 파일을 제외한 다른 파일을 추가하고,
5. `package.json` 에, heroku 가 `yarn install` 로 dependency 를 설치한 후에 실행하는 스크립트인 `  "heroku-postbuild": "yarn run build:prod"` 를 추가해준다.

