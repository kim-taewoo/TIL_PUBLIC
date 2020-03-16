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

1. *&&* logical operator 의 특성을 이용해 모든 조건을 만족하는 경우에만 마지막 부분의 html 태그를 그릴 수 있다. 

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