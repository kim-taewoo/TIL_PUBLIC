import {
  CREATE_STREAM,
  FETCH_STREAMS,
  FETCH_STREAM,
  DELETE_STREAM,
  EDIT_STREAM,
} from '../actions/types';

export default (state = {}, action) => {
  switch (action.type) {
    case FETCH_STREAMS:
      return {
        ...state,
        ...action.payload.reduce((obj, payload) => {
          obj[payload.id] = payload;
          return obj;
        }, {}),
      };
    case FETCH_STREAM:
    case CREATE_STREAM:
    case EDIT_STREAM:
      return { ...state, [action.payload.id]: action.payload };
    case DELETE_STREAM:
      const omit = (key, { [key]: _, ...object }) => object;
      return omit(action.payload, state);
    default:
      return state;
  }
};
