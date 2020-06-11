import React, { Component } from 'react';
import UserCreate from './UserCreate'
import LanguageContext from '../contexts/LanguageContext'
import ColorContext from '../contexts/ColorContext';

export class App extends Component {
  state = { language: 'english' };

  onLanguageChange = (language) => {
    this.setState({language});
  };

  render() {
    return (
      <div className='ui container'>
        <div>
          Select a language:
          <i
            onClick={() => this.onLanguageChange('english')}
            className='flag us'
          ></i>
          <i
            onClick={() => this.onLanguageChange('korean')}
            className='flag kr'
          ></i>
        </div>
        <LanguageContext.Provider value={this.state.language}>
          <ColorContext.Provider value="red">
            <UserCreate />
          </ColorContext.Provider>
        </LanguageContext.Provider>
      </div>
    );
  }
}

export default App;
