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
1. 그런데 코드를 수정할 때마다 매번 위 길고 긴 babel 명령어를 칠 순 없기 때문에, 마지막에 `--watch` 만 추가해주면, 파일을 수정할 때마다 자동으로 인식해서 babel 을 실행시켜 변환시켜준다.

> `yarn` 도 `npm` 과 마찬가지로 `yarn install` 로 `package.json` 내 라이브러리를 재설치해준다.