const debounceRender = function (instance) {

  // if there's a pending render, cancel it
  if (instance.debounce) {
    window.cancelAnimationFrame(instance.debounce);
  }

  // setup the new render to run at the next animation frame
  instance.debounce = window.requestAnimationFrame(() => {
    instance.render();
  })
}


const handler = function (instance) {
  return {
    get(target, prop, receiver) {
      console.log('got it!');
      const value = Reflect.get(target, prop, receiver)
      // const value = Reflect.get(...arguments)
      if (typeof value === 'object') {
        return new Proxy(value, handler(instance))
      }
      return typeof value === 'function' ? value.bind(target) : value;
    },
    set(target, prop, value) {
      console.log('set it');
      Reflect.set(target, prop, value);
      debounceRender(instance)
      // instance.render();
      return true;
    },
    deleteProperty(target, prop) {
      console.log('delete it');
      Reflect.deleteProperty(target, prop)
      instance.render();
      return true;
    }
  }
}


class Component {
  constructor(options) {
    const _this = this;
    const _data = new Proxy(options.data, handler(this))
    this.elem =document.querySelector(options.selector)
    this.template = options.template;
    this.debounce = null;

    Object.defineProperty(this, 'data', {
      get() {
        return _data;
      },
      set(data) {
        _data = new Proxy(data, handler(_this));
        debounce(_this);
        return true;
      }
    })
  }

  render () {
    this.elem.innerHTML = this.template(this.data);
  }
}


const app = new Component({
  selector: '#app',
  data: {
    heading: 'TEST',
    slides: ['swim','climb','jumb','play']
  },
  template (props) {
    return `
      <h1>${props.heading}</h1>
      <ul>
        ${props.slides.map(slide => {
          return `<li>${slide}</li>`;
        }).join('')}
      </ul>
    `;
  }
})

app.render();
app.data.slides.push('nap zzz');

// setTimeout(() => {
//   app.data.slides.push('nap zzz');

//   app.render();
// }, 3000)