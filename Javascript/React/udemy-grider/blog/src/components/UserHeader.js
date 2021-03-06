import React, { Component } from 'react';
import { connect } from 'react-redux';

export class UserHeader extends Component {

  render() {
    const {user} = this.props
    if (!user) {
      return null;
    }

    return <div className='header'>{user.name}</div>;
  }
}
// Component 클래스 내에서 필터링하는 것보다, 
// mapStateToProps 에서 필터링 하는 게 재사용성 측면에서 좋다.
const mapStateToProps = (state, ownProps) => ({
  user: state.users.find(user => user.id === ownProps.userId),
});

const mapDispatchToProps = {
};

export default connect(mapStateToProps, mapDispatchToProps)(UserHeader);
