console.log('app.js is running');

const app = {
  title: '결정, 해드립니다',
  subtitle: '고민중인 선택지를 입력하세요.',
  options: []
};

const onFormSubmit = (e) => {
  e.preventDefault();
  const option = e.target.elements.option.value;

  if (option) {
    app.options.push(option);
    e.target.elements.option.value = '';
    render();
  }
};

const onMakeDecision = () => {
  const randomNum = Math.floor(Math.random() * app.options.length);
  const option = app.options[randomNum];
  alert(option);
};

const resetOption = () => {
  app.options = [];
  render();
};

const appRoot = document.getElementById('app');

const render = () => {
  const template = (
    <div>
      <h1>{app.title}</h1>
      {app.subtitle && <p>{app.subtitle}</p>}
      <p>{app.options.length > 0 ? '입력된 선택지 리스트' : '선택지가 없습니다.'}</p>
      <button disabled={!app.options.length} onClick={onMakeDecision}>결정해주세요!</button>
      <button onClick={resetOption}>모두 지우기</button>
      <ol>
        {
          app.options.map((option) => <li key={option}>{option}</li>)
        }
      </ol>
      <form onSubmit={onFormSubmit}>
        <input type="text" name="option" />
        <button>선택지 추가</button>
      </form>
    </div>
  );
  ReactDOM.render(template, appRoot);
};

render();
