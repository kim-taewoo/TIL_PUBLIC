// https://javascript.info/call-apply-decorators#decorators-and-function-properties

// function slow(x) {
//   // cpu-intensive job
//   console.log(`Called with ${x}`)
//   return x;
// }

// function cachingDecorator(func) {
//   let cache = new Map();

//   return function(x) {
//     if (cache.has(x)) {
//       return cache.get(x);
//     }

//     let result = func(x) // 캐슁없으면 진행

//     cache.set(x, result);
//     return result;
//   }
// }

// slow = cachingDecorator(slow);

// console.log(slow(1));

// console.log(`again: ${slow(1)}`);

// console.log(slow(2));
// console.log(`again: ${slow(2)}`);

// object methods 와 함께 쓰려면 .apply 를 써야 한다. `this` 를 유지시키기 위함

// let worker = {
//   someMethod() {
//     return 1;
//   },

//   slow(x) {
//     console.log(`called with ${x}`);
//     return x * this.someMethod();
//   }
// }

// function cachingDecorator(func) {
//   let cache = new Map();
//   return function(x) {
//     if (cache.has(x)) {
//       return cache.get(x)
//     }
//     let result = func.call(this, x)
//     cache.set(x, result)
//     return result
//   }
// }

// console.log(worker.slow(1));
// worker.slow = cachingDecorator(worker.slow)
// console.log(worker.slow(2));

// let worker = {
//   slow(min, max) {
//     console.log(`Called with ${min}, ${max}`);
//     return min+max;
//   }
// }

// function cachingDecorator(func, hash) {
//   let cache = new Map();
//   return function() {
//     let key = hash(arguments);
//     if (cache.has(key)) {
//       return cache.get(key)
//     }

//     let result = func.call(this, ...arguments);

//     cache.set(key, result);
//     return result;
//   };
// }

// function hash() {
//   return [].join.call(arguments)
// }

// worker.slow = cachingDecorator(worker.slow, hash)

// console.log(worker.slow(3,5));
// console.log('again' + worker.slow(3,5));


function spy(func) {

  function wrapper(...args) {
    // using ...args instead of arguments to store "real" array in wrapper.calls
    wrapper.calls.push(args);
    return func.apply(this, args);
  }

  wrapper.calls = [];

  return wrapper;
}

function work(a, b) {
  console.log(a + b); // work is an arbitrary function or method
}

work = spy(work);

work(1, 2); // 3
work(4, 5); // 9

for (let args of work.calls) {
  console.log('call:' + args.join()); // "call:1,2", "call:4,5"
}

function debounce(func, ms) {
  let timeout;
  return function () {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, arguments), ms);
  };
}


function throttle(func, ms) {
  let isThrottled = false,
    savedArgs,
    savedThis;

  function wrapper() {
    if (isThrottled) {
      // (2)
      savedArgs = arguments;
      savedThis = this;
      return;
    }

    func.apply(this, arguments); // (1)

    isThrottled = true;

    setTimeout(function () {
      isThrottled = false; // (3)
      if (savedArgs) {
        wrapper.apply(savedThis, savedArgs);
        savedArgs = savedThis = null;
      }
    }, ms);
  }

  return wrapper;
}