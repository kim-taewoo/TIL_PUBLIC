import jsonPlaceholder from '../apis/jsonPlaceholder';
// import _ from 'lodash';

// export const fetchPosts = () => {
//   // Bad approach. ERROR: Actions must be plain objects!
//   // const response = await jsonPlaceholder.get('/posts');

//   // return {
//   //   type: 'FETCH_POSTS',
//   //   payload: response,
//   // };

//   // Redux Thunk 로 함수를 반환하면 비동기 처리가 이용가능하다.
//   return async function (dispatch, getState) {
//     const response = await jsonPlaceholder.get('/posts');

//     dispatch({type: 'FETCH_POSTS', paylaod: response})
//   }
// };

// 위 코드 통째로 간략화
export const fetchPosts = () => async (dispatch) => {
  const response = await jsonPlaceholder.get('/posts');
  dispatch({ type: 'FETCH_POSTS', payload: response.data });
};

// API call 최적화 전. 같은 id 인자를 받아도 무조건 새로 호출하고 있다.
export const fetchUser = (id) => async (dispatch) => {
  const response = await jsonPlaceholder.get(`/users/${id}`);
  dispatch({ type: 'FETCH_USER', payload: response.data });
};

// lodash 를 이용한 최적화
// 그러나 이 방법을 사용하면, 한 번 사용된 인자면 무조건 같은 값만을 반환하기 때문에, 업데이트 되었거나 이런 걸 받아볼 수 없고, 코드도 얼핏보면 이해하기 어렵다.
// export const fetchUser = (id) => (dispatch) => {
//   _fetchUser(id, dispatch);
// };

// const _fetchUser = _.memoize(async (id, dispatch) => {
//   const response = await jsonPlaceholder.get(`/users/${id}`);
//   dispatch({ type: 'FETCH_USER', payload: response.data });
// });

// 두 개 이상의 Action Creator 를 합성해서 API 호출을 최적화하는 방법
export const fetchPostsAndUsers = () => async (dispatch, getState) => {
  console.log('About to fetch posts');
  await dispatch(fetchPosts());
  // const userIds = _.uniq(_.map(getState().posts, 'userId'))
  // 위 코드를 lodash 체인을 사용한 경우
  // _.chain(getState().posts)
  //   .map('userId')
  //   .uniq()
  //   .forEach(id => dispatch(fetchUser(id)))
  //   .value()
  // ES6 버전
  const uniqueUsers = [...new Set(getState().posts.map((post) => post.userId))];
  uniqueUsers.forEach(id => {
    dispatch(fetchUser(id))
  });
}