import React from 'react';
import { connect } from 'react-redux';

export const SongDetail = ({ song }) => {
  if (!song) {
    return <div>Select a Song</div>;
  }
  return (
    <div>
      <h3>Details for:</h3>
      <p>
        Title: {song.title}
        <br />
        Duration: {song.duration}
      </p>
    </div>
  );
};

const mapStateToProps = (state) => ({
  song: state.selectedSong,
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(SongDetail);
