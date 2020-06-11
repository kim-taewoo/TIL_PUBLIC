import React, { Component } from 'react'
import LanguageContext from '../contexts/LanguageContext'

export class LanguageSelector extends Component {
  static contextType = LanguageContext
  render() {
    return (
      <div>
        Select a language:
        <i
          onClick={() => this.context.onLanguageChange('english')}
          className='flag us'
        ></i>
        <i
          onClick={() => this.context.onLanguageChange('korean')}
          className='flag kr'
        ></i>
      </div>
    );
  }
}

export default LanguageSelector
