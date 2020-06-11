// hooks 를 배운 뒤 돌아와서 작성한 Refactored version
// 다른 데 사용할 때 재사용하기 쉽다.

import {useState, useEffect} from 'react'

export default () => {
  const [lat, setLat] = useState(null)
  const [errorMessage, setErrorMessage] = useState('')

  useEffect(() => {
    window.navigator.geolocation.getCurrentPosition(
      position => setLat(position.coords.latitude),
      err => setErrorMessage(err.message)
    )
  }, [])

  return [lat, errorMessage]
}