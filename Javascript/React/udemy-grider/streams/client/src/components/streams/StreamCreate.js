import React, { Component } from 'react';
import {connect} from 'react-redux'
import {createStream} from '../../actions'
import StreamForm from './StreamForm'

export class StreamCreate extends Component {

  onSubmit = (formValues) => {
    this.props.createStream(formValues);
  }

  render() {
    // console.log(this.props);
    return (
      <div>
        <h3>Create a Stream</h3>
        <StreamForm onSubmit={this.onSubmit} />
      </div>
    );
  }
}


const mapStateToProps = (state) => ({
  
})

const mapDispatchToProps = {
  createStream
}


export default connect(mapStateToProps, mapDispatchToProps )(StreamCreate)