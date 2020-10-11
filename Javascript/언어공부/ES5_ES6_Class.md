- [간결한 설명 블로그](https://medium.com/@apalshah/javascript-class-difference-between-es5-and-es6-classes-a37b6c90c7f8)

# Classes in ES6
```js

'use strict';

/**
 * Person class.
 *
 * @constructor
 * @param {String} name - name of a person.
 * @param {Number} age  - age of a person.
 * @param {String} gender  - gender of a person.
 */

class Person {
  constructor(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
  }

  getName() {
    return this.name;
  }

  getAge() {
    return this.age;
  }

  getGender() {
    return this.gender;
  }
}

/**
 * Teacher class.
 *
 * @constructor
 * @param {String} name - name of a teacher.
 * @param {Number} age  - age of a teacher.
 * @param {String} gender  - gender of a teacher.
 * @param {String} subject - subject of a teacher.
 */

class Teacher extends Person {
  constructor(name, age, gender, subject) {
    super(name, age, gender);

    this.subject = subject;
  }

  getSubject() {
    return this.subject;
  }
}

/**
 * Student class.
 *
 * @constructor
 * @param {String} name - name of a student.
 * @param {Number} age  - age of a student.
 * @param {String} gender  - gender of a student.
 * @param {Number} marks - marks of a student.
 */

class Student extends Person {
  constructor(name, age, gender, marks) {
    super(name, age, gender);
    this.marks = marks;
  }

  getMarks() {
    return this.marks;
  }
}

const teacher = new Teacher('John Doe', 30, 'male', 'Maths');
const student = new Student('Jane Miles', 12, 'female', 88);

console.log(
  'Teacher:',
  teacher.getName(),
  teacher.getAge(),
  teacher.getGender(),
  teacher.getSubject(),
);
console.log(
  'Student:',
  student.getName(),
  student.getAge(),
  student.getGender(),
  student.getMarks(),
);
```

> Note: I don’t know if you noticed this — we are not using any `let`, `var`, `const` or `function` keywords to create a property, which may lead to some confusion. And *after ES6, we don’t need the constructor to initialize the properties.* I’ll publish that blog after this, which will clear one doubt that all the beginners have — what is the difference between a variable and a property inside a class?

# Classes in ES5

```js
'use strict';

/**
 * Person class.
 *
 * @constructor
 * @param {String} name - name of a person.
 * @param {Number} age  - age of a person.
 * @param {String} gender  - gender of a person.
 */

// 함수 자체가 Constructor 처럼 작동함
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

Person.prototype.getName = function() {
  return this.name;
};

Person.prototype.getAge = function() {
  return this.age;
};

Person.prototype.getGender = function() {
  return this.gender;
};

/**
 * Teacher class.
 *
 * @constructor
 * @param {String} name - name of a teacher.
 * @param {Number} age  - age of a teacher.
 * @param {String} gender  - gender of a teacher.
 * @param {String} subject - subject of a teacher.
 */

function Teacher(name, age, gender, subject) {
  Person.call(this, name, age, gender);
  this.subject = subject;
}

Teacher.prototype = Object.create(Person.prototype);

Teacher.prototype.getSubject = function() {
  return this.subject;
};

/**
 * Student class.
 *
 * @constructor
 * @param {String} name - name of a student.
 * @param {Number} age  - age of a student.
 * @param {String} gender  - gender of a student.
 * @param {Number} marks - marks of a student.
 */

function Student(name, age, gender, marks) {
  Person.call(this, name, age, gender);
  this.marks = marks;
}

Student.prototype = Object.create(Person.prototype);

Student.prototype.getMarks = function() {
  return this.marks;
};

// `new` operator 로 생성된 객체는 생성된 자신을 `this` 로 가진다. 
// 이 이유에 따라, 위에서 정의한 함수 내의 `this` 들이 글로벌 객체가 아닌 인스턴스를 가리키게 된다.
const teacher = new Teacher('John Doe', 30, 'male', 'Maths');
const student = new Student('Jane Miles', 12, 'female', 88);

console.log(
  'Teacher:',
  teacher.getName(),
  teacher.getAge(),
  teacher.getGender(),
  teacher.getSubject(),
);
console.log(
  'Student:',
  student.getName(),
  student.getAge(),
  student.getGender(),
  student.getMarks(),
);
```

# Constructor

### MDN

If you don't provide your own constructor, then a default constructor will be supplied for you. If your class is a base class, the default constructor is empty:

```js
constructor() {}
```

If your class is a derived class, the default constructor calls the parent constructor, passing along any arguments that were provided:

```js
constructor(...args) {
  super(...args);
}
```

즉, 커스텀하게 initialize 할 게 있으면 `constructor` 을 작성하고 안에 `super` 도 꼭 작성해주어야 하지만, 커스텀이 필요 없다면 알아서 해준다.