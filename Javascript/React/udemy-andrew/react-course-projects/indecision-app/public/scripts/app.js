'use strict';

console.log('app.js is running');

var app = {
  title: '결정, 해드립니다',
  subtitle: '고민중인 선택지를 입력하세요.',
  options: []
};

var onFormSubmit = function onFormSubmit(e) {
  e.preventDefault();
  var option = e.target.elements.option.value;

  if (option) {
    app.options.push(option);
    e.target.elements.option.value = '';
    render();
  }
};

var onMakeDecision = function onMakeDecision() {
  var randomNum = Math.floor(Math.random() * app.options.length);
  var option = app.options[randomNum];
  alert(option);
};

var resetOption = function resetOption() {
  app.options = [];
  render();
};

var appRoot = document.getElementById('app');

var render = function render() {
  var template = React.createElement(
    'div',
    null,
    React.createElement(
      'h1',
      null,
      app.title
    ),
    app.subtitle && React.createElement(
      'p',
      null,
      app.subtitle
    ),
    React.createElement(
      'p',
      null,
      app.options.length > 0 ? '입력된 선택지 리스트' : '선택지가 없습니다.'
    ),
    React.createElement(
      'button',
      { disabled: !app.options.length, onClick: onMakeDecision },
      '\uACB0\uC815\uD574\uC8FC\uC138\uC694!'
    ),
    React.createElement(
      'button',
      { onClick: resetOption },
      '\uBAA8\uB450 \uC9C0\uC6B0\uAE30'
    ),
    React.createElement(
      'ol',
      null,
      app.options.map(function (option) {
        return React.createElement(
          'li',
          { key: option },
          option
        );
      })
    ),
    React.createElement(
      'form',
      { onSubmit: onFormSubmit },
      React.createElement('input', { type: 'text', name: 'option' }),
      React.createElement(
        'button',
        null,
        '\uC120\uD0DD\uC9C0 \uCD94\uAC00'
      )
    )
  );
  ReactDOM.render(template, appRoot);
};

render();
