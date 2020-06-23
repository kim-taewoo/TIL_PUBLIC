import React from 'react';
import { mount } from 'enzyme';
import moxios from 'moxios';
import Root from 'Root';
import App from 'components/App';

beforeEach(() => {
  moxios.install();
});

afterEach(() => {
  moxios.uninstall();
});

it('can fetch a list of comments and display them', (done) => {
  // Attempt to render the *entire* App
  const wrapped = mount(
    <Root>
      <App />
    </Root>
  );
  // find the 'fetchComments' button and click it
  wrapped.find('.fetch-comments').simulate('click');
  // Introduce a TINY little pause
  moxios.wait(() => {
    // Expect to find a list of comments!
    let request = moxios.requests.mostRecent();
    request.respondWith({
      status: 200,
      response: [
        {
          name: 'Fetched #1'
        },
        {
          name: 'Fetched #2'
        }
      ]
    }).then(() => {
      wrapped.update();
      expect(request.config.url).toEqual('http://jsonplaceholder.typicode.com/comments')
      expect(wrapped.find('li').length).toEqual(2);
      done()
      wrapped.unmount();
    })
  }); 
});
