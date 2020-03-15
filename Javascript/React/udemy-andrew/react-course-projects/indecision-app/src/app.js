console.log('app.js is learning');

// JSX - Javascript XML
var template = <h1>This is JSX from app.js</h1>;
var appRoot = document.getElementById('app');
ReactDOM.render(template, appRoot);