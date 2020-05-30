// Import React and ReactDOM
import React from 'react';
import ReactDOM from 'react-dom';
// Create a react component
const App = () => {
  return <div>Hi there!</div>
}
// Take the react comoponent and show it on the screen

ReactDOM.render(
  <App />,
  document.querySelector('#root')
)
