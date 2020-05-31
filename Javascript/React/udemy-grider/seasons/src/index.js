import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import SeasonDisplay from './SeasonDisplay';
import Spinner from './Spinner';

class App extends Component {
  state = {
    lat: null,
    lng: null,
    errorMessage: '',
    time: new Date().toLocaleTimeString(),
  };

  componentDidMount() {
    window.navigator.geolocation.getCurrentPosition(
      (position) => this.setState({ lat: position.coords.latitude }),
      (err) => this.setState({ errorMessage: err.message })
    );

    setInterval(() => {
      this.setState({ time: new Date().toLocaleTimeString() });
    }, 1000);
  }

  // Helper method
  renderContent() {
    if (this.state.errorMessage && !this.state.lat) {
      return <div>Error!: {this.state.errorMessage}</div>;
    }

    if (!this.state.errorMessage && this.state.lat) {
      return (
        <div>
          <div
            style={{
              textAlign: 'center',
              backgroundColor: 'orange',
              color: 'white',
            }}
          >
            {this.state.time}
          </div>
          <SeasonDisplay lat={this.state.lat} />
        </div>
      );
    }

    return <Spinner message='Please accept loaction request' />;
  }

  render() {
    return <div className='border red'>{this.renderContent()}</div>;
  }
}

ReactDOM.render(<App />, document.getElementById('root'));
