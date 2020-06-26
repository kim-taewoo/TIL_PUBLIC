import React, { useState, useEffect } from 'react';

function HookCounterOne() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('')
  useEffect(() => {
    console.log('updating titile');
    document.title = `Clicked ${count} times`;
    return () => {};
  }, [count]);
  return (
    <div>
      <input type="text" name="" id="" value={name} onChange={e => setName(e.target.value)} />
      <button onClick={() => setCount((prev) => prev + 1)}>
        Click {count} times
      </button>
    </div>
  );
}

export default HookCounterOne;
