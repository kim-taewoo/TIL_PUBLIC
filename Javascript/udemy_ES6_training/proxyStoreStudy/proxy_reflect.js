// https://javascript.info/proxy

// let proxy = new Proxy(target, handler);
// target is an object to wrap. can be anything, including function
// handler : proxy configuration. `an object` with traps. methods that intercept operations. ex) get trap for reading a property of target, set trap for writing a property into target, and so on.

// proxy operation 중에 handler 에 있는 corresponding trap 이 있다면, 작동한다.

// let target = {};
// let proxy = new Proxy(target, {}); //empty handler

// proxy.test = 5;
// console.log(target.test);

// console.log(proxy.test)

// for (let key in proxy) console.log(key);

// 즉, 아무런 trap 이 없으면 그냥 투명한 wrapper 다.

// Proxy 는 special "exotic object" 로, 자기 자신의 property 를 가지지 않는다.

// # Default value with "get" trap
// To intercept reading, the `handler` should have a method `get(target, property, receiver)`

// target 은 타겟 객체로, new Proxy 의 첫번째 인자다.
// property 는 그냥 property 이름이다.
// receiver 은 target property 가 getter 인 경우, receiver 는 호출할 때 `this` 로 사용될 객체다. 보통은 그게 `proxy` 그 자체 객체인 경우가 많다. (아니면 proxy 를 상속받은 객체거나. ) 당장은 필요없는 인자니 아직 신경쓰지 말자

// 원래 배열은 존재하지 않는 인덱스의 값을 get 하려고 하면 `undefined` 를 반환하는데, proxy 로 감싸서 없는 경우에는 0 을 반환하게 해보자

// let numbers = [0,1,2]

// numbers = new Proxy(numbers, {
//   get(target, prop) {
//     if (prop in target) {
//       return target[prop];
//     } else {
//       return 0; // default value 로 0
//     }
//   }
// })

// console.log(numbers[1]);
// console.log(numbers[123]);

// let dictionary = {
//   'hello': 'hola',
//   'bye' : 'Adios'
// }

// dictionary = new Proxy(dictionary, {
//   get(target, phrase) {
//     if (phrase in target) {
//       // 사전에 있으면 번역한 것을 돌려줌.
//       return target[phrase]
//     } else {
//       // 아니면 그냥 원래 걸로 돌려줘
//       return phrase
//     }
//   }
// })

// console.log(dictionary['hello']);
// console.log(dictionary['welcome to proxy']);

// # validation with 'set' trap
// set(target, property, value, receiver)

// set trap 은 언제나 `true` 를 반환해야 한다. false 를 반환하면 `TypeError` 가 발생한다. false 가 발생하는 경우는 set 이 실패했고, 에러를 일으켜야 하는 상황이다.

// let numbers = [];
// numbers = new Proxy(numbers, {
//   set(target, prop, val) {
//     if (typeof val === 'number') {
//       target[prop] = val;
//       return true;
//     } else {
//       return false;
//     }
//   }
// })

// numbers.push(1);
// numbers.push(2);

// console.log("length is " + numbers.length); // 2

// // numbers.push('test') // TypeError

// console.log('this line is never reached (error above)');

// array 의 push 나 unshift 를 override 할 필요는 없다. 왜냐하면 그것들도 내부적으로는 [[Set]] 을 사용하고 있고, 그것을 proxy 가 intercept 하고 있기 때문이다.

// # Iteration with "ownKeys" and "getOwnPropertyDescriptor"

// `Object.keys`, `for...in` loop and most other methods that iterate over object properties use [[OwnPropertyKeys]] internal method (intercepted by `ownKeys` trap) to get a list of properties

// 그니까 객체의 iterable 속성들에 접근하는 것도 intercept 가능하다.

// 세부적으로는 좀 차이가 있다.
// `Object.getOwnPropertyNames(obj)` returns non-symbol keys.
// `Object.getOwnPropertySymbols(obj)` returns symbol keys.
// `Object.keys/values()` returns non-symbol keys/values with `enumerable` flag
// `for...in` loops over non-symbol keys with `enumerable` flag. and also prototype keys

// const user = {
//   name: 'John',
//   age: 30,
//   _password: '**',
// };

// const proxy = new Proxy(user, {
//   ownKeys(target) {
//     return Object.keys(target).filter((key) => {
//       return !key.startsWith('_');
//     });
//   },
// }); 

// for (const key in proxy) console.log(key);
// console.log(Object.getOwnPropertyNames(proxy));
// // console.log(Object.getOwnPropertySymbols(proxy));
// console.log(Object.keys(proxy));
// console.log(Object.values(proxy));

// 그런데 아예 뜬금없는 새로운 값을 반환하고 싶다고 해보자. 

// const user = {};
// userProxy = new Proxy(user, {
//   ownKeys(target) {
//     return ['a', 'b', 'c'];
//   }
// })

// console.log(Object.keys(userProxy));

// 빈 값이 나오는 이유는, `Object.keys` 란 놈이 언제나 `enumerable` flag 를 가진 property 들만을 반환하기 때문이다. 

// let user = {};

// user = new Proxy(user, {
//   ownKeys(target) { // called once to get a list of properties
//     return ['a','b','c'];
//   },

//   // 객체에 존재하지 않는 property 에 관한 것은 getOwnPropertyDescriptor trap 만 쓰면 된다.
//   getOwnPropertyDescriptor(target, prop) { // called for every property
//     return {
//       enumerable: true,
//       configurable: true,
//       // other flags, probable "value: ..."
//     }
//   }
// })

// console.log(Object.keys(user));

// # Protected properties with 'deleteProperty' and other traps
// _ 가 붙은 속성을 진짜 secret 하게 만들어보자. 즉, 바깥에서 접근이 불가능한 속성으로 만들어 보자.
// let user = {
//   name: 'John',
//   _password: 'secret'
// }
// 위처럼만 하면 그냥 접근 가능하다.
// console.log(user._password);

// 필요한 proxy 트랩은 다음과 같다. 

// 1. get  -> 접근 때 에러 발생하도록
// 2. set  -> write 시도할 때 에러 발생하도록
// 3. deleteProperty  -> 지우려 시도하면 에러발생하도록
// 4. ownKeys  -> _ 로 시작하는 애들은 `for...in` 같은 메서드에서 순회되지 않도록

// let user = {
//   name: "John",
//   _password: "***"
// };

// user = new Proxy(user, {
//   get(target, prop) {
//     if (prop.startsWith('_')) {
//       throw new Error("Access denied");
//     }
//     let value = target[prop];
//     // 아래 설명 참고
//     return (typeof value === 'function') ? value.bind(target) : value; // (*)
//   },
//   set(target, prop, val) { // to intercept property writing
//     if (prop.startsWith('_')) {
//       throw new Error("Access denied");
//     } else {
//       target[prop] = val;
//       return true;
//     }
//   },
//   deleteProperty(target, prop) { // to intercept property deletion
//     if (prop.startsWith('_')) {
//       throw new Error("Access denied");
//     } else {
//       delete target[prop];
//       return true;
//     }
//   },
//   ownKeys(target) { // to intercept property list
//     return Object.keys(target).filter(key => !key.startsWith('_'));
//   }
// });

// // "get" doesn't allow to read _password
// try {
//   console.log(user._password); // Error: Access denied
// } catch(e) { console.log(e.message); }

// // "set" doesn't allow to write _password
// try {
//   user._password = "test"; // Error: Access denied
// } catch(e) { console.log(e.message); }

// // "deleteProperty" doesn't allow to delete _password
// try {
//   delete user._password; // Error: Access denied
// } catch(e) { console.log(e.message); }

// // "ownKeys" filters out _password
// for(let key in user) console.log(key); // name

// `this` 키워드에 접근이 필요한 메서드들이 있다. (this 란 . 전에 오는 것이라고 생각하면 편하다.) 이 메서드들은 호출될 때 결국은 `get` trap 을 활성화하기 때문에 `this` 키워드를 쓰는 걸 제대로 하려면 `bind` 해주어야 한다. 


// "In range" with 'has' trap

// let range = {
//   start: 1,
//   end: 10
// }

// range = new Proxy(range, {
//   has(target, prop) {
//     return prop >= target.start && prop <= target.end;
//   }
// });

// console.log(5 in range) // true
// console.log(50 in range) // false


// # Wrapping functions: 'apply'

// apply(target, thisArg, args)
// thisArg is the value of this
// args is a list of arguments

// function delay(f, ms) {
//   // return a wrapper that passes the call to f after the timeout
//   return function() { // (*)
//     setTimeout(() => f.apply(this, arguments), ms);
//   };
// }

// function sayHi(user) {
//   console.log(`Hello, ${user}!`);
// }
// console.log(sayHi.length)
// // after this wrapping, calls to sayHi will be delayed for 3 seconds
// sayHi = delay(sayHi, 3000);

// sayHi("John"); // Hello, John! (after 3 seconds)

// console.log(sayHi.length); // 1 (function length is the arguments count in its declaration)

// sayHi = delay(sayHi, 3000);

// console.log(sayHi.length); // 0 (in the wrapper declaration, there are zero arguments)

// function delay(f, ms) {
//   return new Proxy(f, {
//     apply(target, thisArg, args) {
//       console.log(thisArg);
//       console.log(args); 
//       setTimeout(() => target.apply(thisArg, args), ms);
//     }
//   })
// }

// function sayHi (user) {
//   console.log(arguments);
//   console.log(`Hello, ${user}!`);
// }

// sayHi = delay(sayHi, 3000)

// console.log(sayHi.length);

// sayHi('john')


// # Reflect
// Reflect is a built-in object that simplifies creation of Proxy.

// It was said previously that internal methods, such as [[Get]], [[Set]] and others are specification-only, they can’t be called directly.

// The Reflect object makes that somewhat possible. Its methods are minimal wrappers around the internal methods.

// Here are examples of operations and Reflect calls that do the same:

// Operation	Reflect call	Internal method
// obj[prop]	Reflect.get(obj, prop)	[[Get]]
// obj[prop] = value	Reflect.set(obj, prop, value)	[[Set]]
// delete obj[prop]	Reflect.deleteProperty(obj, prop)	[[Delete]]
// new F(value)	Reflect.construct(F, value)	[[Construct]]
// …	…	…
// For example:

// let user = {};

// Reflect.set(user, 'name', 'John');

// console.log(user.name); // John
// In particular, Reflect allows us to call operators (new, delete…) as functions (Reflect.construct, Reflect.deleteProperty, …). That’s an interesting capability, but here another thing is important.

// For every internal method, trappable by Proxy, there’s a corresponding method in Reflect, with the same name and arguments as the Proxy trap.

// let user = {
//   _name: "Guest",
//   get name() {
//     return this._name;
//   }
// }

// let userProxy = new Proxy(user, {
//   get(target, prop, receiver) {
//     // return target[prop] // 얘는 상황에 맞게 `this` 를 변형시켜주지 못함
//     return Reflect.get(target, prop, receiver) // receiver 를 써야 getter에 올바른 `this` reference 를 전달해줌
//     // return Reflect.get(...arguments) // shortest version
//   }
// })

// console.log(userProxy.name);

// let admin = {
//   __proto__: userProxy,
//   _name: "Admin"
// };

// console.log(admin.name);


// Proxy limitations

// Built-in objects: `Internal` slots
// Many built-in objects, for example Map, Set, Date, Promise and others make use of so-called “internal slots”.

// These are like properties, but reserved for internal, specification-only purposes. For instance, Map stores items in the internal slot [[MapData]]. Built-in methods access them directly, not via [[Get]]/[[Set]] internal methods. So Proxy can’t intercept that.

// Why care? They’re internal anyway!

// Well, here’s the issue. After a built-in object like that gets proxied, the proxy doesn’t have these internal slots, so built-in methods will fail.

// let map = new Map();

// let proxy = new Proxy(map, {});

// proxy.set('test', 1); // Error

// Internally, a Map stores all data in its [[MapData]] internal slot. The proxy doesn’t have such a slot. The built-in method Map.prototype.set method tries to access the internal property this.[[MapData]], but because this=proxy, can’t find it in proxy and just fails.

// Fortunately, there’s a way to fix it:

// let map = new Map();

// let proxy = new Proxy(map, {
//   get(target, prop, receiver) {
//     let value = Reflect.get(...arguments);
//     return typeof value == 'function' ? value.bind(target) : value;
//   }
// });

// proxy.set('test', 1);
// console.log(proxy.get('test')); // 1 (works!)

// Now it works fine, because get trap binds function properties, such as map.set, to the target object (map) itself.

// Unlike the previous example, the value of this inside proxy.set(...) will be not proxy, but the original map. So when the internal implementation of set tries to access this.[[MapData]] internal slot, it succeeds.

// 존재하지 않는 property 에 접근하려하면 undefined 대신 에러를 발생시키는 proxy

// let user = {
//   name: "John"
// };



// function wrap(target) {
//   return new Proxy(target, {
//     get(target, prop, receiver) {
//       if (prop in target) {
//         return Reflect.get(target, prop, receiver);
//       } else {
//         throw new ReferenceError(`Property doesn't exist: "${prop}"`)
//       }
//     }
//   });
// }

// user = wrap(user);

// console.log(user.name); // John
// console.log(user.age); // ReferenceError: Property doesn't exist "age"


// negative index like python

// let array = [1, 2, 3];

// array = new Proxy(array, {
//   get(target, prop, receiver) {
//     if (prop < 0) {
//       // even if we access it like arr[1]
//       // prop is a string, so need to convert it to number
//       prop = +prop + target.length;
//     }
//     return Reflect.get(target, prop, receiver);
//   }
// });


// console.log(array[-1]); // 3
// console.log(array[-2]); // 2


// # Observable

// create a function `makeObservable(target)` that makes the object observable by returning a proxy

// The solution consists of two parts:

// 1. Whenever .observe(handler) is called, we need to remember the handler somewhere, to be able to call it later. We can store handlers right in the object, using our symbol as the property key.
// 2. We need a proxy with set trap to call handlers in case of any change.

let handlers = Symbol('handlers')

function makeObservable(target) {
  // initialize handlers store
  target[handlers] = [];

  // store the handler function in array for future calls
  target.observe = function(handler) {
    this[handlers].push(handler);
  }

  // create a proxy to handle changes
  return new Proxy(target, {
    set(target, property, value, receiver) {
      let success = Reflect.set(...arguments)
      if (success) {
        target[handlers].forEach(handler => handler(property, value));
      }
      return success;
    }
  });
}

let user = {};
user = makeObservable(user);

user.observe((key, value) => {
  console.log(`SET ${key} = ${value}`);
})

user.name = 'Joshua'