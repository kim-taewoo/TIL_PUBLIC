# Plugin, Preset
필요한 Plugin 들을 모아 놓은 것이 Preset.

# Babel Cli 사용 예시 코드
`npx babel src/code.js --presets=@babel/preset-react --plugins=@babel/plugin-transform-template-literals,@babel/plugin-
transform-arrow-functions`

보다시피 사용하는 플러그인 및 프리셋이 많아질수록 상당히 귀찮다. 따라서 따로 설정 파일을 만드는 것이 좋다. 

Babel 6 까지는 `.babelrc` 파일로 설정값을 관리했지만, Babel 7 부터는 `babel.config.js` 파일로 관리하는 것을 추천한다. 