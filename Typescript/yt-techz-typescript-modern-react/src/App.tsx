import React, { useContext, useEffect } from 'react';
import { Store } from './Store';
import { IAction, IEpisode } from './Interfaces';

const EpisodeList = React.lazy<any>(() => import('./EpisodesList'))

function App(): JSX.Element {
  const { state, dispatch } = useContext(Store);

  
  const fetchDataAction = async () => {
    const URL =
    'https://api.tvmaze.com/singlesearch/shows?q=rick-&-morty&embed=episodes';
    const data = await fetch(URL);
    const dataJSON = await data.json();
    return dispatch({
      type: 'FETCH_DATA',
      payload: dataJSON._embedded.episodes,
    });
  };
  
  useEffect(() => {
    state.episodes.length === 0 && fetchDataAction();
  });
  
  const toggleFavAction = (episode: IEpisode): IAction => {
    const episodeInFav = state.favourites.includes(episode);
    if (episodeInFav) {
      return dispatch({
        type: 'REMOVE_FAV',
        payload: episode,
      });
    }
    return dispatch({
      type: 'ADD_FAV',
      payload: episode,
    });
  };
  
  interface IEpisodeListProps {
    episodes: IEpisode[]
    toggleFavAction: (episode: IEpisode) => IAction
    favourites: IEpisode[]
  }

  const props = {
    episodes: state.episodes,
    toggleFavAction,
    favourites: state.favourites,
  }

  return (
    <>
      <header className='header'>
        <div>
          <h1>Rick & Morty</h1>
          <p>Pick your favorite episode!</p>
        </div>
        <div>
          Favourites(s): {state.favourites.length}
        </div>
      </header>
      <section className='episode-layout'>
        <React.Suspense fallback={<div>Loading...</div>}>
          <EpisodeList {...props} />
        </React.Suspense>  
      </section>
    </>
  );
}

export default App;
