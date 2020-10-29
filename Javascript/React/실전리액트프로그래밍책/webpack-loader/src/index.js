import React from 'react';
import ReactDOM from 'react-dom';
import Style from './App.css';
import Icon from './icon.png';
import SIcon from './small-icon.png';
import Json from './data.json';
import Text from './data.txt';

console.log({ Style });

function App() {
  return (
    <div className='container'>
      <h3 className='title'>webpack example</h3>
      <div>{`name: ${Json.name}, age: ${Json.age}`}</div>
      <div>{`text: ${Text}`}</div>
      <img src={SIcon} alt='' />
      <img src={Icon} alt='' />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
