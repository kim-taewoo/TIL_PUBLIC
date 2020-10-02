function generator(input) {
  var index = 0;
  return {
    next: function () {
      if (index < input.length) {
        index += 1;
        return input[index - 1];
      }
      return '';
    },
  };
}

const mygenerator = generator('안녕하세요');
console.log(mygenerator.next());
console.log(mygenerator.next());
console.log(mygenerator.next());
console.log(mygenerator.next());

// instanceof 예시
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
}
var newCar = new Car('Honda', 'City', 2007);
console.log(newCar instanceof Car); // returns true

var person = {
  name: 'Stranger',
  age: 24,
  identity: function() {
    return { who: this.name, howOld: this.age };
  },
};
console.log(person.identity());

console.log(global);
console.log(process);