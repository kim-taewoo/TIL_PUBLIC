import React, {useContext} from 'react'
import {UserContext} from 'App'

function ComponentA() {
  const user = useContext(UserContext)
  return (
    <div>
      {JSON.stringify(user)}
    </div>
  )
}

export default ComponentA
