import React from 'react'
import { BrowserRouter, Link, Route } from 'react-router-dom'
import Rooms from './Rooms';

export default function App() {
  return (
    <BrowserRouter>
      <div style={{padding: 20, border: '5px solid gray'}}>
        <Link to='/'>홈</Link>
        <br />
        <Link to='/photo'>사진</Link>
        <br />
        <Link to='/rooms'>방 소개</Link>
        <br />
        Route
      </div>
      <Route exact path='/' component={Home} />
      <Route path='/photo' component={Photo} />
      <Route path='/rooms' component={Rooms} />
    </BrowserRouter>
  );
}

function Home({match}) {
  return <h2>홈페이지</h2>
}

function Photo({match}) {
  return <h2>사진 감상페이지</h2>
}

