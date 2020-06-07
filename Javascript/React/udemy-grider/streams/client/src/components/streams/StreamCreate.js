import React, { Component } from 'react';
import { Field, reduxForm } from 'redux-form';

export class StreamCreate extends Component {
  renderError({ error, touched }) {
    if (touched && error) {
      console.log(touched, error);
      return (
        <div className='ui error message'>
          <div className='header'>{error}</div>
        </div>
      );
    }
  }

  // formProps 를 destructuring 해서 많이 쓴다.
  renderInput = (formProps) => {
    // console.log(formProps);
    const className = `field ${formProps.meta.error && formProps.meta.touched ? 'error' : ''}`
    return (
      <div className={className}>
        <label htmlFor=''>{formProps.label}</label>
        <input {...formProps.input} autoComplete='off' />
        {this.renderError(formProps.meta)}
      </div>
    );
  };

  onSubmit(formValues) {
    console.log(formValues);
  }

  render() {
    // console.log(this.props);
    return (
      <form
        onSubmit={this.props.handleSubmit(this.onSubmit)}
        className='ui form error'
      >
        <Field name='title' component={this.renderInput} label='Enter Title' />
        <Field
          name='description'
          component={this.renderInput}
          label='Enter Description'
        />
        <button className='ui button primary'>Submit</button>
      </form>
    );
  }
}

const validate = (formValues) => {
  const errors = {};

  if (!formValues.title) {
    errors.title = '제목은 반드시 입력해야 해요';
  }

  if (!formValues.description) {
    errors.description = '내용은 반드시 입력해야 해요!';
  }

  return errors;
};

export default reduxForm({
  // 이 form 이름 붙이기
  form: 'streamCreate',
  validate,
})(StreamCreate);
