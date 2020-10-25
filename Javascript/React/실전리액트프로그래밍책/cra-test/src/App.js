import React, { useEffect } from 'react'

export default function App() {
  useEffect(() => {
    window.onpopstate = function(e) {
      console.log(`location: ${document.location}, state: ${e.state.name}`);
    }
  }, []);

  return (
    <>
      <button onClick={() => window.history.pushState({name:'v1'}, '', '/page1')}>
        page1
      </button>
      <button onClick={() => window.history.pushState('v2', '', '/page2')}>
        page2
      </button>
    </>
  );
}

