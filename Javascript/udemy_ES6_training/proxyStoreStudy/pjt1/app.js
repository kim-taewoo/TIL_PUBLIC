const getNodeType = function(node) {
  if (node.nodeType === 3) return 'text';
  if (node.nodeType === 8) return 'comment';
  return node.tagName.toLowerCase();
}

const getNodeContent = function (node) {
  if (node.childNodes && node.childNodes.length > 0) return null;
  return node.textContent;
}

const stringToHTML = function (str) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(str, 'text/html');
  return doc.body;
}

const diff = function(template, elem) {
  const domNodes = [...elem.childNodes];
  const templateNodes = [...template.childNodes]

  let count = domNodes.length - templateNodes.length;
  while (count > 0) {
    domNodes[domNodes.length - count].remove();
  }

  templateNodes.forEach((node, index) => {
    if (!domNodes[index]) {
      elem.appendChild(node.cloneNode(true))
      return;
    }

    if (getNodeType(node) !== getNodeType(domNodes[index])) {
      domNodes[index].parentNode.replaceChild(node.cloneNode(true), domNodes[index])
      return;
    }

    const templateContent = getNodeContent(node);
    if (templateContent && templateContent !== getNodeContent(domNodes[index])) {
      domNodes[index].textContent = tempalteContent;
    }

    if (domNodes[index].childNodes.length > 0 && node.childNodes.length < 1) {
      domNodes[index].innerHTML = '';
      return;
    }

    if (domNodes[index].childNodes.length < 1 && node.childNodes.length > 0) {
      const fragment = document.createDocumentFragment();
      diff(node, fragment);
      domNodes[index].appendChild(fragment);
      return;
    }

    if (node.childNodes.length > 0) {
      diff(node, domNodes[index]);
    }
  })
}

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
    // this.elem.innerHTML = this.template(this.data);
    const templateHTML = stringToHTML(this.template(this.data))

    diff(templateHTML, this.elem)
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

