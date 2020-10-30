import React, { useEffect, useState } from 'react';
import Home from './Home';
import About from './About';
import styled from 'styled-components';

const Container = styled.div`
  background-color: #aaaaaa;
  border: 1px solid blue;
  color: red;
`;

export default function App({ page:currentPage }) {
  const [page, setPage] = useState(currentPage);
  useEffect(() => {
    window.onpopstate = (event) => {
      setPage(event.state);
    };
  }, []);

  function onChangePage(e) {
    const newPage = e.target.dataset.page;
    window.history.pushState(newPage, '', `/${newPage}`);
    setPage(newPage);
  }
  const PageComponent = page === 'home' ? Home : About;

  return (
    <Container>
      <button onClick={onChangePage} data-page='home'>
        Home
      </button>
      <button onClick={onChangePage} data-page='about'>
        About
      </button>
      <PageComponent />
    </Container>
  );
}
