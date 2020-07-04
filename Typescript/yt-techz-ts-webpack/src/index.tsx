import React, { useState, Fragment } from 'react';
import ReactDOM from 'react-dom';

type FormElem = React.FormEvent<HTMLFormElement>;

interface ITodo {
  text: string;
  complete: boolean;
}

// interface 장점인 상속
// interface ITodo2 extends ITodo {
//   tags: string[]
// }

export default function App(): JSX.Element {
  const [value, setValue] = useState<string>('');
  const [todos, setTodos] = useState<ITodo[]>([]);

  const handleSubmit = (e: FormElem): void => {
    e.preventDefault();
    addTodo(value);
    setValue('');
  };

  const addTodo = (text: string): void => {
    const newTodos: ITodo[] = [...todos, { text, complete: false }];
    setTodos(newTodos);
  };

  const completeTodo = (index: number): void => {
    const newTodos: ITodo[] = [...todos];
    newTodos[index].complete = !newTodos[index].complete;
    setTodos(newTodos);
  };

  const removeTodos = (index: number): void => {
    const newTodos: ITodo[] = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <>
      <h1>Todo List</h1>
      <form onSubmit={handleSubmit}>
        <input
          value={value}
          onChange={(e) => setValue(e.target.value)}
          required
          type='text'
          name=''
          id=''
        />
        <button type='submit'>확인</button>
      </form>

      <section>
        {todos.map(
          (todo: ITodo, index: number): JSX.Element => (
            <Fragment key={index}>
              <div
                style={{ textDecoration: todo.complete ? 'line-through' : '' }}
              >
                {todo.text}
              </div>
              ;
              <button onClick={(): void => completeTodo(index)}>
                {todo.complete ? 'Completed' : 'Incomplete'}
              </button>
              <button onClick={(): void => removeTodos(index)}>&times;</button>
            </Fragment>
          )
        )}
      </section>
    </>
  );
}

ReactDOM.render(<App />, document.getElementById('app'));
