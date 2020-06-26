import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DataFetching() {
  const [post, setPost] = useState({});
  const [id, setId] = useState(1)
  const [idFromButtonClick, setIdFromButtonClick] = useState(1)
  useEffect(() => {
    (async function getData() {
      const res = await axios
        .get(`https://jsonplaceholder.typicode.com/posts/${id}`)
        .catch((e) => console.error('요청부터 실패'));
      console.log(res);
      setPost(res.data)
    })();
  }, [idFromButtonClick]);
  const handleClick = () => {
    setIdFromButtonClick(id)
  }
  return (
    <div>
      <input type="text" name="" value={id} onChange={e => setId(e.target.value)} id=""/>
      <button type="button" onClick={handleClick}>Fetch Post</button>
      <div>{post.title}</div>
      {/* <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul> */}
    </div>
  );
}

export default DataFetching;
