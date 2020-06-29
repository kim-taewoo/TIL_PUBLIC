import React, { useEffect, useReducer } from 'react';
import axios from 'axios';

const initialState = {
  loading: true,
  error: '',
  post: {},
};

const reducer = (state, action) => {
  switch (action.type) {
    case 'FETCH_SUCCESS':
      return {
        loading: false,
        post: action.payload,
        error: '',
      };
    case 'FETCH_ERROR':
      return {
        loading: false,
        post: {},
        error: 'Something went wrong!',
      };
    default:
      return state;
  }
};

function DataFetchingTwo() {
  const [{loading, error, post}, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    (async function () {
      try {
        const response = await axios.get(
          'https://jsonplaceholder.typicode.com/posts/1'
        );
        dispatch({ type: 'FETCH_SUCCESS', payload: response.data });
      } catch (error) {
        dispatch({ type: 'FETCH_ERROR' });
      }
    })();
  }, []);

  return (
    <div>
      {loading ? 'Loading...' : post.title}
      {error ? error : null}
    </div>
  );
}

export default DataFetchingTwo;
