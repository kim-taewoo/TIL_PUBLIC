import React, { Component } from 'react';
import { connect } from 'react-redux';
import * as actions from 'actions';

export class CommentBox extends Component {
  state = { comment: '' };

  handleChange = (event) => {
    this.setState({ comment: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    this.props.saveComment(this.state.comment)
    this.setState({ comment: '' });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <h4>댓글 추가</h4>
          <textarea onChange={this.handleChange} value={this.state.comment} />
          <div>
            <button>확인</button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, actions)(CommentBox);