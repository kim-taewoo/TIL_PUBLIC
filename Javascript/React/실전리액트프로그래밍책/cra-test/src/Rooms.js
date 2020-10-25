import React from 'react'
import { Link, Route } from 'react-router-dom'

export default function Rooms({match}) {
  return (
    <div>
      <h2>Rooms Page</h2>
      <Link to={`${match.url}/blueRoom`}>Blue room</Link>
      <br />
      <Link to={`${match.url}/greenRoom`}>Green room</Link>
      <br />
      <Route path={`${match.url}/:roomId`} component={Room} />
      <Route exact path={match.url} render={() => <h3>방을 선택해주세요</h3>} />
    </div>
  )
}

function Room({match}) {
  return <h2>{`${match.params.roomId} 방을 선택하셨습니다.`}</h2>
}
