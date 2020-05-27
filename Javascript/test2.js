var person = {
  name: 'victolee',
  email: 'asdf@example.com',
  birth: '0225',
  foo: function (val1, val2, val3) {
    console.log(val1 + val2 + val3);
    console.log(this);
  },
};

person.foo.call(this, 3, 6, 9);

console.log(this === process);
