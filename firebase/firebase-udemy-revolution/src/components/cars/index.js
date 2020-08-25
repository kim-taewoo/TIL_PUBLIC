import React, { Component } from 'react';
import { db } from '../../utils/firebase';

import { firebaseLooper } from '../../utils/tools';

export class Cars extends Component {
  state = {
    cars: null,
  };

  componentDidMount() {
    db.collection('cars')
      .get()
      .then((snapshot) => {
        const cars = firebaseLooper(snapshot);
        this.setState({ cars });
      })
      .catch((e) => console.error(e));
  }

  handleCarData = (cars) =>
    cars
      ? cars.map((data, i) => (
          <tr key={i}>
            <td>{data.id}</td>
            <td>{data.brand}</td>
            <td>{data.color}</td>
          </tr>
        ))
      : null;

  render() {
    const cars = this.state.cars;
    return (
      <>
        <table className='table table-dark'>
          <thead>
            <tr>
              <th>ID</th>
              <th>Brand</th>
              <th>Color</th>
            </tr>
          </thead>
          <tbody>{this.handleCarData(cars)}</tbody>
        </table>
      </>
    );
  }
}

export default Cars;
