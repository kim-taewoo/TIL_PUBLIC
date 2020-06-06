import React, { Component } from 'react';
import { connect } from 'react-redux';
import { selectSong } from '../actions';

export class SongList extends Component {
  renderList() {
    return this.props.songs.map((song) => {
      return (
        <div className='item' key={song.title}>
          <div className='right floated content'>
            <button
              onClick={() => this.props.selectSong(song)}
              className='ui button primary'
            >
              Select
            </button>
          </div>
          <div className='content'>{song.title}</div>
        </div>
      );
    });
  }
  render() {
    return <div className='ui divided list'>{this.renderList()}</div>;
  }
}

const mapStateToProps = (state) => ({
  songs: state.songs,
});

const mapDispatchToProps = {
  selectSong,
};

export default connect(mapStateToProps, mapDispatchToProps)(SongList);
