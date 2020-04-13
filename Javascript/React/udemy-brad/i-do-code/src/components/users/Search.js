import React, { useState } from 'react';
import PropTypes from 'prop-types';

const Search = ({ setAlert, searchUsers, showClear, clearUsers }) => {
  const [text, setText] = useState('');

  const onChange = (e) => {
    // setState({
    //   [e.target.name]: e.target.value,
    // });
    setText(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    if (text === '') {
      setAlert('Please enter something', 'light');
    } else {
      searchUsers(text);
      setText('');
    }
  };

  return (
    <div>
      <form onSubmit={onSubmit} className='form' autoComplete='on'>
        <input
          value={text}
          type='text'
          name='text'
          placeholder='Search Users...'
          autoComplete='on'
          onChange={onChange}
        />
        <input
          type='submit'
          value='Search'
          className='btn btn-block btn-dark'
        />
      </form>
      {showClear && (
        <button className='btn btn-light btn-block' onClick={clearUsers}>
          Clear
        </button>
      )}
    </div>
  );
};

Search.propTypes = {
  searchUsers: PropTypes.func.isRequired,
  clearUsers: PropTypes.func.isRequired,
  showClear: PropTypes.bool.isRequired,
  setAlert: PropTypes.func.isRequired,
};

export default Search;
