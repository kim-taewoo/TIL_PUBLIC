## bind, call, apply

"Use .bind() when you want that function to later be called with a certain context, useful in events. Use .call() or .apply() when you want to invoke the function immediately, with modification of the context." \_Chad

### call()

call function takes two arguments:

1. Context
2. Function arguments

A context is an object that replaces **this** keyword inside the function. Later arguments are passed as function arguments.

For Ex:

```javascript
var cylinder = {
  pi: 3.14,
  volume: function (r, h) {
    return this.pi * r * r * h;
  },
};
// Call invocation is like this
cylinder.volume.call({ pi: 3.14159 }, 2, 6);
// 75.39815999999999
```

### apply()

Apply is exactly same as `call()` except Function arguments are passed as a list for god’s sake.

```javascript
cylinder.volume.apply({ pi: 3.14159 }, [2, 6]);
// 75.39815999999999;
```

### bind()

Bind attaches a brand new this to a given function. In bind’s case, the function is not executed instantly like Call or Apply.

```javascript
var newVolume = cylinder.volume.bind({pi: 3.14159}); // This is not instant call
// After some long time, somewhere in the wild 
newVolume(2,6); // Now pi is 3.14159
```

What is the use of Bind? It allows us to inject a context into a function which returns a new function with updated context. It means this variable will be user supplied variable. This is very useful while working with JavaScript events.


## Scope

There are three kinds of scopes:  
1. Global scope
1. Local Scope/Function scope
1. Block scope(Introduced in ES6)

### Block Scope 예시

```javascript
var a = 10;

function Foo() {
  if (true) {
    let a = 4;
  }

  alert(a); // alerts '10' because the 'let' keyword
}
Foo();
```