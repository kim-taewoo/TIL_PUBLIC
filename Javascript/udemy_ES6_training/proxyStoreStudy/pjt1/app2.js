var debounceRender = function (instance) {
  // If there's a pending render, cancel it
  if (instance.debounce) {
    window.cancelAnimationFrame(instance.debounce);
  }
  
  // Setup the new render to run at the next animation frame
  instance.debounce = window.requestAnimationFrame(function () {
    instance.render();
  });
};

var handler = function (instance) {
  return {
    get: function (obj, prop) {
      if (
        ['[object Object]', '[object Array]'].indexOf(
          Object.prototype.toString.call(obj[prop])
        ) > -1
      ) {
        return new Proxy(obj[prop], handler(instance));
      }
      return obj[prop];
    },
    set: function (obj, prop, value) {
      obj[prop] = value;
      debounceRender(instance);
      return true;
    },
    deleteProperty: function (obj, prop) {
      delete obj[prop];
      debounceRender(instance);
      return true;
    },
  };
};

var Rue = function (options) {
  // Variables
  var _this = this;
  _this.elem = document.querySelector(options.selector);
  var _data = new Proxy(options.data, handler(this));
  _this.template = options.template;
  _this.debounce = null;

  // Define setter and getter for data
  Object.defineProperty(this, 'data', {
    get: function () {
      return _data;
    },
    set: function (data) {
      _data = new Proxy(data, handler(_this));
      debounce(_this);
      return true;
    },
  });
};

Rue.prototype.render = function () {
  this.elem.innerHTML = this.template(this.data);
};

var app = new Rue({
  selector: '#app',
  data: {
    heading: 'My Todos',
    todos: ['Swim', 'Climb', 'Jump', 'Play'],
  },
  template: function (props) {
    return `
			<h1>${props.heading}</h1>
			<ul>
				${props.todos
          .map(function (todo) {
            return `<li>${todo}</li>`;
          })
          .join('')}
			</ul>`;
  },
});

// Render the initial UI
app.render();

// After 3 seconds, update the data and render a new UI
setTimeout(function () {
  app.data.todos.push('Take a nap... zzzzz');
}, 3000);
