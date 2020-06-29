import React, { useEffect, useState } from 'react';
import axios from 'axios';
function DataFetchingOne() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [post, setPost] = useState({});

  useEffect(() => {
    (async function () {
      try {
        const response = await axios.get(
          'https://jsonplaceholder.typicode.com/posts/1'
        );
        setLoading(false);
        setPost(response.data);
        setError('');
      } catch (error) {
        setLoading(false);
        setPost({});
        setError('Something went wrong!');
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

export default DataFetchingOne;
