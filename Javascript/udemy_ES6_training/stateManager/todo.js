import { createState } from './app.js';

const TODO_NEW_ITEMS = (item, deletionAction) => {
  console.log(`In todo items : ${item}`);
  return `
    <div id="todo-item" class= "todo-item" data-id=${item.id}>
        <p id='todo-text'>${item.value}</p>
        <button id="delTodo" onclick=${deletionAction}(this)>DEL</button>
    </div>
  `;
};

const TODO_COMPLETED_ITEMS = (item) => {
  return `
      <div id="todo-completed-item" class= "todo-completed-item" data-id=${item.id}>
          <p id='todo-completed-text'>${item.value}</p>
      </div>
    `;
};

const TODO_PAGE = (state) => {
  return ` <div class="todo-container">
    <div class="todo-items">
    ${state.items
      .map((item) => {
        if (!item.completed) {
          return TODO_NEW_ITEMS(item, state.events.deleteTodo);
        }
      })
      .join('\n')}
    </div>
    <form class="todo-input-container" action='javascript:' ">
      <div class="todo-input">
        <input id="newTodo" type="text" name="newTodo" value="${
          state.currentItem
        }"  placeholder="Add to do item" onkeyup="${
    state.events.recordTodo
  }(this)" />
      </div>
      <div class="todo-add">
        <button type='button' id="addTodo" name="addTodo" onclick="${
          state.events.insertTodoItem
        }(this)" >ADD</button>
      </div>
    </form>
    <div class='todo-completed'>
    ${state.items
      .map((item) => {
        if (item.completed) {
          return TODO_COMPLETED_ITEMS(item);
        }
      })
      .join('\n')}
    </div>
  </div>`;
};

let todoInitialstate = {
  items: [],
  currentItem: '',
  events: {
    recordTodo: 'recordTodo',
    insertTodoItem: 'insertTodoItem',
    deleteTodo: 'deleteTodo',
  },
  target: {},
};

var todoState = createState(todoInitialstate);

function recordTodo(target) {
  //todoItemsSpace.appendChild(todoItem(event.target.value));
  // state.currentItem = event.target.value;
  console.log(
    `event fired with state value ${JSON.stringify(todoState.state)}`
  );
  console.log(target);
  // updateState(state);
  // rough.innerHTML = event.target.value
  todoState.setState({
    ...todoState.state,
    currentItem: target.value,
    target: target,
  });
}

function insertTodoItem(target) {
  console.log('insertTodoItem');
  console.log('Adding todo npow.');

  let id = Date.now();
  let tempState = todoState.state;
  tempState.items.push({
    id: id,
    value: tempState.currentItem,
    completed: false,
  });

  tempState.currentItem = '';
  tempState.target = target;
  todoState.setState(tempState);
}

window.addEventListener('stateUpdate', generateView);

function generateView() {
  let main_Page = TODO_PAGE(todoState.state);

  document.getElementById('root').innerHTML = main_Page;

  let element = todoState.state.target;
  if (element.type == 'text') {
    document
      .getElementById(element.id)
      .setSelectionRange(element.selectionStart, element.selectionEnd);

    document.getElementById(element.id).focus();
  }
}

generateView();
