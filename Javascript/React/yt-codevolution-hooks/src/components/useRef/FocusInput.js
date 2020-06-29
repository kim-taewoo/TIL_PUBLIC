import React, { useEffect, useRef } from 'react'

function FocusInput() {
  const inputRef = useRef(null)
  useEffect(() => {
    // focus the input element
    inputRef.current.focus()
    return () => {
    }
  }, [])
  return (
    <div>
      <input ref={inputRef} type="text" name="" id=""/>
    </div>
  )
}

export default FocusInput
