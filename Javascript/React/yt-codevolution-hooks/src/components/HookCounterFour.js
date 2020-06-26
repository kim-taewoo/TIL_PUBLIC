import React, { useState } from 'react'

function HookCounterFour() {
  const [items, setItems] = useState([])

  const addItem = (params) => {
    setItems([...items, {
      id: items.length,
      value: Math.floor(Math.random() * 10) + 1
    }])
  }
  return (
    <div>
      <button onClick={addItem}>Add a number</button>
      <ul>
        {items.map(item => {
          return <li key={item.id}>{item.value}</li>
        })}
      </ul>
    </div>
  )
}

export default HookCounterFour
