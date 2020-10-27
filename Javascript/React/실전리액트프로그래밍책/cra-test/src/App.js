import React, { useState } from 'react'
import { BrowserRouter, Link, Route } from 'react-router-dom'
import useWindowWidth from './customHooks/useWindowWidth';
import Rooms from './Rooms';
import Title from './Title';

export default function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: 20, border: '5px solid gray' }}>
        <Link to='/'>홈</Link>
        <br />
        <Link to='/photo'>사진</Link>
        <br />
        <Link to='/rooms'>방 소개</Link>
        <br />
        <Link to='/rmemo'>React.memo</Link>
        <br />
        <Link to='/resize'>Resize Event</Link>
        <br />
        Route
      </div>
      <Route exact path='/' component={Home} />
      <Route path='/photo' component={Photo} />
      <Route path='/rooms' component={Rooms} />
      <Route path='/rmemo' component={Rmemo} />
      <Route path='/resize' component={Resize} />
    </BrowserRouter>
  );
}

function Home({match}) {
  return <h2>홈페이지</h2>
}

function Photo({match}) {
  return <h2>사진 감상페이지</h2>
}

function Rmemo({match}) {
  const [count, setCount] = useState(0)
  function onClick() {
    setCount(count+1);
  }
  return (
    <div>
      <Title title={`현재 카운트: ${count}`} />
      <button onClick={onClick}>Increase</button>
    </div>
  )
}

function Resize() {
  const width = useWindowWidth();

  return (
    <div>
      {`width is ${width}`}
    </div>
  )
}
