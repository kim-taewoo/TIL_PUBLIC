import React, { Component } from 'react'
import { db } from '../../utils/firebase';

import { firebaseLooper } from '../../utils/tools'

export class Cars extends Component {
  componentDidMount() {
    db.collection('cars').get().then(snapshot => {
      const cars = firebaseLooper(snapshot);
      console.log(cars);
    }).catch(e => console.error(e))
  }
  render() {
    return (
      <div>
        
      </div>
    )
  }
}

export default Cars
