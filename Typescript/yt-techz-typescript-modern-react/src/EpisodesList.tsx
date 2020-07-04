import React from 'react';
import { IEpisode } from './Interfaces';

export default function EpisodesList(props: any): Array<JSX.Element> {
  const { episodes, toggleFavAction, favourites } = props;
  return episodes.map((episode: IEpisode) => {
    return (
      <section key={episode.id} className='episode-box'>
        <img src={episode.image.medium} alt={`Rick & Morty ${episode.name}`} />
        <div>{episode.name}</div>
        <section style={{ display: 'flex', justifyContent: 'space-between' }}>
          Season: {episode.season} Number: {episode.number}
          <div>
            <button type='button' onClick={() => toggleFavAction(episode)}>
              {favourites.find((fav: IEpisode) => fav.id === episode.id)
                ? 'UnFav'
                : 'Fav'}
            </button>
          </div>
        </section>
      </section>
    );
  });
}
