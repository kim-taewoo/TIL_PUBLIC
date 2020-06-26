import React, { Component } from 'react';

class ClassCounter extends Component {
  constructor(props) {
    super(props);

    this.state = {
      count: 0,
      name: '',
    };
  }

  componentDidMount() {
    document.title = `Clicked ${this.state.count} times`;
  }

  componentDidUpdate(prevProps, prevState) {
    if(prevState.count !== this.state.count) {
      console.log('updating document title');      
    }
    document.title = `Clicked ${this.state.count} times`;
  }

  increment = () => {
    this.setState({
      count: this.state.count + 1,
    });
  };

  render() {
    return (
      <div>
        <input
          type='text'
          name=''
          id=''
          value={this.state.name}
          onChange={(e) => {
            this.setState({ name: e.target.value });
          }}
        />
        <button onClick={this.increment}>Count {this.state.count}</button>
      </div>
    );
  }
}

export default ClassCounter;
