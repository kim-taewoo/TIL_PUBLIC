class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.addOne = this.addOne.bind(this);
    this.subtractOne = this.subtractOne.bind(this);
    this.resetCount = this.resetCount.bind(this);
    this.state = {
      count: 0,
    };
  }

  addOne() {
    this.setState((prevState) => {
      return {
        count: prevState.count + 1
      }
    })
  };

  subtractOne() {
    this.setState((prevState) => {
      return {
        count: prevState.count - 1
      }
    })
  };

  resetCount() {
    this.setState(() => {
      return {
        count: 0
      }
    })
  };

  render() {
    return (
      <div>
        <h1>Count: {this.state.count} </h1>
        <button onClick={this.addOne}>+1</button>
        <button onClick={this.subtractOne}>-1</button>
        <button onClick={this.resetCount}>reset</button>
      </div>
    );
  }
}

ReactDOM.render(<Counter />, document.getElementById('app'));

// let count = 0;
// const addOne = () => {
//   count++;
//   renderCounterApp();
// };

// const subtractOne = () => {
//   count--;
//   renderCounterApp();
// };

// const reset = () => {
//   count = 0;
//   renderCounterApp();
// };

// const appRoot = document.getElementById('app');

// const renderCounterApp = () => {
//   const templateTwo = (
//     <div>
//       <h1>Count: {count}</h1>
//       <button onClick={addOne}>+1</button>
//       <button onClick={subtractOne}>-1</button>
//       <button onClick={reset}>reset</button>
//     </div>
//   );
//   ReactDOM.render(templateTwo, appRoot);
// }

// renderCounterApp(); // initial render