import jsonPlaceholder from '../apis/jsonPlaceholder';

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

export const fetchUser = (id) => async (dispatch) => {
  const response = await jsonPlaceholder.get(`/users/${id}`);
  dispatch({ type: 'FETCH_USER', payload: response.data });
};
