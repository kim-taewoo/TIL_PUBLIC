import React, { Component } from 'react';
import SearchBar from './SearchBar';
import youtube from '../apis/youtube';

const KEY = process.env.REACT_APP_YOUTUBE_API_KEY;

export class App extends Component {
  onTermSubmit = (term) => {
    youtube.get('/search', {
      params: {
        part: 'snippet',
        type: 'video',
        maxResult: 5,
        key: `${KEY}`,
        q: term,
      }
    });
  };

  render() {
    return (
      <div className='ui container'>
        <SearchBar onTermSubmit={this.onTermSubmit} />
      </div>
    );
  }
}

export default App;
