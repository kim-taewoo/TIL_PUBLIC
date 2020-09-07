import React, { Component } from 'react';
import { firebaseLooper } from '../../utils/tools';
import { carsCollection, employeesRef } from '../../utils/firebase';
import Form from './forms';

export class Cars extends Component {
  state = {
    cars: [],
    start: 0,
    end: 100
  };

  getAlltheCars() {
    carsCollection
      // .where('color', '==', 'red')
      .orderBy('price')
      .startAt(this.state.start)
      .endAt(this.state.end)
      .get()
      .then((snapshot) => {
        const cars = firebaseLooper(snapshot);
        this.setState({cars});
      })
      .catch((e) => console.error(e));
  }

  componentDidMount() {
    this.getAlltheCars();
  }

  handleCarData = (cars) =>
    cars.length
      ? cars.map((data) => {
          return (
            <tr key={data.id}>
              <td>{data.id}</td>
              <td>{data.brand}</td>
              <td>{data.color}</td>
              <td>{data.price}</td>
              <td>{new Date(data.createdAt.seconds).toLocaleString()}</td>
            </tr>
          );
        })
      : null;

  render() {
    const cars = this.state.cars;
    return (
      <>
        <Form />
        <hr />
        <table className='table table-dark'>
          <thead>
            <tr>
              <th>ID</th>
              <th>Brand</th>
              <th>Color</th>
              <th>Price</th>
              <th>CreatedAt</th>
            </tr>
          </thead>
          <tbody>{this.handleCarData(cars)}</tbody>
        </table>
      </>
    );
  }
}

export default Cars;
