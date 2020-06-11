import React, { Component } from 'react'
import LanguageContext from '../contexts/LanguageContext'

export class Field extends Component {
  static contextType = LanguageContext

  render() {
    const text = this.context.language === 'english' ? 'Name': '이름'

    return (
      <div className="ui field">
        <label htmlFor="name">{text}</label>
        <input type="text"/>
      </div>
    )
  }
}

export default Field
