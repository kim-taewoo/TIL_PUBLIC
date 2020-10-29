# Babel 을 실행하는 여러 가지 방법
1. @babel/cli 로 실행
1. 웹팩에서 babel-loader 로 실행
1. @babel/core 를 직접 실행
1. @babel/register 로 실행. 

이 중에서 마지막 @babel/register 을 이용하는 것은 리액트와 사용하는 경우가 많지 않음으로 생략한다.

# Plugin, Preset
필요한 Plugin 들을 모아 놓은 것이 Preset.

# Babel Cli 사용 예시 코드
`npx babel src/code.js --presets=@babel/preset-react --plugins=@babel/plugin-transform-template-literals,@babel/plugin-
transform-arrow-functions`

보다시피 사용하는 플러그인 및 프리셋이 많아질수록 상당히 귀찮다. 따라서 따로 설정 파일을 만드는 것이 좋다. 

Babel 6 까지는 `.babelrc` 파일로 설정값을 관리했지만, Babel 7 부터는 `babel.config.js` 파일로 관리하는 것을 추천한다. 

# extends, env, overrides
바벨 설정 파일에서 사용할 수 있는 속성들 중 하나
- extends 속성을 이용하면 다른 설정 파일을 가져와서 확장할 수 있다.
- env 또는 overrides 속성을 이용하면 환경별 또는 파일별로 다른 설정을 적용할 수 있다. 