export default ({dispatch}) => next => action => {
  //Check to see if the action has a promise on its 'payload' property
  // if it does, then wait for it to resolve
  //if it doesn't, then send the action on to the next middleware

  // debugger;

  if (!action.payload || !action.payload.then) {
    return(next(action))
  }

  // promise 를 가지고 있다면 resolve 까지 기다렸다가
  // 새로운 action 을 만들어서 dispatch
  action.payload.then((res) => {
    const newAction = {...action, payload:res}
    dispatch(newAction)
  })
}
