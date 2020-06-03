import React, { Component } from 'react';

export class SearchBar extends Component {
  state = { term: '' };

  onInputChange = (event) => {
    this.setState({ term: event.target.value });
  };

  onFormSubmit = event => {
    event.preventDefault();

    this.props.onTermSubmit(this.state.term)
  }

  render() {
    return (
      <div className='search-bar ui segment'>
        <form action='#' className='ui form' onSubmit={this.onFormSubmit}>
          <div className='field'>
            <label htmlFor='search'>Video Search</label>
            <input
              type='text'
              name='search'
              value={this.state.term}
              onChange={this.onInputChange}
            />
          </div>
        </form>
      </div>
    );
  }
}

export default SearchBar;
