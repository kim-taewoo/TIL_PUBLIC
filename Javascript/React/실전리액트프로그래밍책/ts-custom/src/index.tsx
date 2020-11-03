import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import Icon from './icon.png'
window.myValue = 123;

console.log('123'.padStart(5, '0')); // tsconfig 의 'lib' 배열 기본값에 es2017 을 추가했기 때문. 하지만 폴리필을 추가해주는 것은 아니다. 

ReactDOM.render(<App name="taewoo" age={13} />, document.getElementById('root'));