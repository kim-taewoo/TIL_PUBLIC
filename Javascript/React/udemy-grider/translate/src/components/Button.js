import React, { Component } from 'react';
import LanguageContext from '../contexts/LanguageContext';
import ColorContext from '../contexts/ColorContext'

export class Button extends Component {
  renderSubmit(value) {
    return value === 'english' ? 'Submit' : '제출'
  }

  render() {
    return (
      <ColorContext.Consumer>
        {(color) => (
          <button className={`ui button ${color}`}>
            <LanguageContext.Consumer>
              {(value) =>  this.renderSubmit(value)}
            </LanguageContext.Consumer>
          </button>
        )}
      </ColorContext.Consumer>
    )
  }
}

export default Button;
