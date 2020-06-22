import React, { Component } from 'react'
import { connect } from 'react-redux'
import comments from 'reducers/comments'

export class CommentList extends Component {
  renderComments() {
    return this.props.comments.map((comment) => {
      return <li key={comment}>{comment}</li>
    })
  }

  render() {
    return (
      <div>
        <ul>
          {this.renderComments()}
        </ul>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  comments: state.comments
})

const mapDispatchToProps = {
  
}

export default connect(mapStateToProps, mapDispatchToProps)(CommentList)
