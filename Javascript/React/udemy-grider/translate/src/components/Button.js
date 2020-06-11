import React, { Component } from 'react';
import LanguageContext from '../contexts/LanguageContext';
import ColorContext from '../contexts/ColorContext'

export class Button extends Component {
  renderSubmit(language) {
    return language === 'english' ? 'Submit' : '제출'
  }

  render() {
    return (
      <ColorContext.Consumer>
        {(color) => (
          <button className={`ui button ${color}`}>
            <LanguageContext.Consumer>
              {({language}) =>  this.renderSubmit(language)}
            </LanguageContext.Consumer>
          </button>
        )}
      </ColorContext.Consumer>
    )
  }
}

export default Button;
