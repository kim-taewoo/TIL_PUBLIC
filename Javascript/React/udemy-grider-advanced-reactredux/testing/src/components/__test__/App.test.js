import React from 'react'
import {shallow} from 'enzyme'
import App from 'components/App'
import CommentBox from 'components/CommentBox'
import CommentList from 'components/CommentList';

let wrapped;

beforeEach(() => {
  wrapped = shallow(<App />);
})

it('shows a comment box', () => {
  // 사실 네이밍이 wrapped 보다 component 가 어울리다는 사람도 많다.
  expect(wrapped.find(CommentBox).length).toEqual(1);
})

it('shows a comment list', () => {
  expect(wrapped.find(CommentList).length).toEqual(1);
});