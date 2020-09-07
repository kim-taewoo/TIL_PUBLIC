import React, { Component } from 'react';
import { carsCollection, firebaseTimestamp } from '../../utils/firebase';

export default class Form extends Component {
  state = {
    brand: '',
    price: '',
    color: '',
    available: 'true',
  };

  handleForm = (e) => {
    e.preventDefault();
    carsCollection
      .doc()
      .set({
        ...this.state,
        price: +this.state.price,
        available: this.state.available === 'true' ? true : false,
        createdAt: firebaseTimestamp(),
        dealers: {
          virginia: true,
          washington: false,
          california: true
        },
        tags: ['good','comfortable','expensive']
      })
      .then((data) => console.log(data))
      .catch((e) => console.error(e));
  };

  changeHandler = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState({ [name]: value });
  };

  render() {
    return (
      <>
        <form onSubmit={(e) => this.handleForm(e)}>
          <div className='form-group'>
            <label htmlFor=''>Brand</label>
            <input
              name='brand'
              onChange={(e) => this.changeHandler(e)}
              type='text'
              className='form-control'
            />
          </div>

          <div className='form-group'>
            <label htmlFor=''>Color</label>
            <input
              name='color'
              onChange={(e) => this.changeHandler(e)}
              type='text'
              className='form-control'
            />
          </div>

          <div className='form-group'>
            <label htmlFor=''>Price</label>
            <input
              name='price'
              onChange={(e) => this.changeHandler(e)}
              type='number'
              className='form-control'
            />
          </div>

          <div className='form-group'>
            <label htmlFor=''>Available</label>
            <select
              defaultValue='true'
              className='form-control'
              name='available'
              id=''
              onChange={(e) => this.changeHandler(e)}
            >
              <option value='true'>YES</option>
              <option value='false'>NO</option>
            </select>
          </div>

          <button type='submit' className='btn btn-primary'>
            Submit
          </button>
        </form>
      </>
    );
  }
}
