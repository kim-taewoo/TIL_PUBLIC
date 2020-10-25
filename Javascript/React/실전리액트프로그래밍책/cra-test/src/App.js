import Box from "./Box4";
import TodoList from "./TodoList";

function App() {
  console.log(`REACT_APP_DATA_API = ${process.env.REACT_APP_DATA_API}`);
  console.log(`REACT_APP_LOGIN_API = ${process.env.REACT_APP_LOGIN_API}`);
  return (
    <div className="App">
      <TodoList />
      <Box /*size="big"*/ />
    </div>
  );
}

export default App;

