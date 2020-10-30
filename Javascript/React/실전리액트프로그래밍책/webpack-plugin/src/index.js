// import React from 'react'
import ReactDOM from 'react-dom'

function App() {
  return (
    <div>
      <h3>안녕하세요 웹팩 플러그인 예제입니다. </h3>
      <p>html-webpack-plugin 플러그인을 사용합니다.</p>
      <p>플러그인은 로더보다 강력한 기능을 갖습니다. 로더는 특정 모듈에 대한 처리만 담당하지만 플러그인은 웹팩이 실행되는 전체 과정에 개입할 수 있습니다. </p>
      <p>{`앱 버전은 ${APP_VERSION}입니다.`}</p>
      <p>{`10 * 10 = ${TEN * TEN}`}</p>
    </div>
  )
}

ReactDOM.render(<App />, $('#root')[0]);