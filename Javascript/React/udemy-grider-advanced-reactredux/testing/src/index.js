import React from 'react';
import { render } from 'react-dom';
import { Route, BrowserRouter as Router } from 'react-router-dom'

import App from 'components/App';
import Root from 'Root'

render(
  <Root>
    <Router>
      <Route path="/" component={App} />
    </Router>
  </Root>,
  document.getElementById('root')
);
