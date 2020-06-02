import axios from 'axios';

// axios instance 생성
export default axios.create({
  baseURL: 'https://api.unsplash.com',
  headers: {
    Authorization: 'Client-ID TOEIRjaMERH3eDQPK7RpO0dd2luG0M9AU6pkBZk9fwQ',
  },
});