import React, { useEffect, useState } from 'react';

export default function App() {
  const [pageName, setPageName] = useState('');
  useEffect(() => {
    window.onpopstate = (e) => {
      setPageName(e.state);
      console.log(`location: ${document.location}, state: ${e.state}`); // 객체도 가능.
    };
  }, []);

  function onClick1() {
    const pageName = 'page1';
    window.history.pushState(pageName, '', '/page1');
    setPageName(pageName);
  }

  function onClick2() {
    const pageName = 'page2';
    window.history.pushState(pageName, '', '/page2');
    setPageName(pageName);
  }

  return (
    <>
      <button onClick={onClick1}>page1</button>
      <button onClick={onClick2}>page2</button>
      {!pageName && <Home />}
      {pageName === 'page1' && <Page1 />}
      {pageName === 'page2' && <Page2 />}
    </>
  );
}

function Home() {
  return <h2>홈페이지</h2>;
}

function Page1() {
  return (
    <div>
      <h2>page1</h2>
      <p>{document.location.href}</p>
    </div>
  );
}

function Page2() {
  return (
    <div>
      <h2>page2</h2>
      <p>{document.location.href}</p>
    </div>
  );
}
