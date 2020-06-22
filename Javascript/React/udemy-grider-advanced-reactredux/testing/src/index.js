import React from 'react';
import { render } from 'react-dom';
import App from 'components/App';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import reducers from 'reducers';

render(
  <Provider store={createStore(reducers, {})}>
    <App />
  </Provider>,
  document.getElementById('root')
);
