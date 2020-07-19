const debounceRender = function (instance) {
  // if there's a pending render, cancel it
  if (instance.debounce) {
    window.cancelAnimationFrame(instance.debounce);
  }

  // setup the new render to run at the next animation frame
  instance.debounce = window.requestAnimationFrame(() => {
    instance.render();
  });
};

const handler = function (instance) {
  return {
    get(target, prop, receiver) {
      console.log('got it!');
      const value = Reflect.get(target, prop, receiver);
      // const value = Reflect.get(...arguments)
      if (typeof value === 'object') {
        return new Proxy(value, handler(instance));
      } 
      return value;
    },
    set(target, prop, value) {
      console.log('set it');
      Reflect.set(target, prop, value);
      debounceRender(instance);
      // instance.render();
      return true;
    },
    deleteProperty(target, prop) {
      console.log('delete it');
      Reflect.deleteProperty(target, prop);
      debounceRender(instance);
      // instance.render();
      return true;
    },
  };
};

class Component {
  constructor(options) {
    const _this = this;
    this.elem = document.querySelector(options.selector);
    let _data = new Proxy(options.data, handler(this));
    this.template = options.template;
    this.debounce = null;

    Object.defineProperty(this, 'data', {
      get() {
        return _data;
      },

      set(data) {
        _data = new Proxy(data, handler(_this));
        debounceRender(_this);
        return true;
      },
    });
  }

  render() {
    this.elem.innerHTML = this.template(this.data);
  }
}

const app = new Component({
  selector: '#app',
  data: {
    heading: 'TEST',
    slides: ['swim', 'climb', 'jumb', 'play'],
  },
  template(props) {
    return `
      <h1>${props.heading}</h1>
      <ul>
        ${props.slides
          .map((slide) => {
            return `<li>${slide}</li>`;
          })
          .join('')}
      </ul>
    `;
  },
});

app.render();

setTimeout(() => {
  app.data.slides.push('nap zzz');
  // app.data = {
  //   heading: 'TEST@',
  //   slides: ['tset1','123']
  // }
}, 3000);

