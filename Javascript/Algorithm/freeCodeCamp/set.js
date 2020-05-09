function mySet() {
  const collection = [];
  this.has = function (element) {
    return collection.indexOf(element) !== -1;
  };

  this.values = function () {
    return collection;
  };

  this.add = function (element) {
    if (!this.has(element)) {
      collection.push(element);
      return true;
    }
    return false;
  };

  this.remove = function (element) {
    if (this.has(element)) {
      index = collection.indexOf(element);
      collection.splice(index, 1);
      return true;
    }
    return false;
  };

  // 여기 위에는 전부 ES6 의 기본 자료형인 Set 에 포함된 내용이다. (remove 대신 delete 라는 이름으로 쓰는 것 외에는.)
  // 아래 size 도 있긴 한데, 함수가 아니라 property 다.
  this.size = function () {
    return collection.length;
  };

  // 여기서부터는 ES6 Set 자료형에 기본으로 탑재되지 않은 메서드들이다. 그래서 직접 구현할 필요가 있다...

  this.union = function (otherSet) {
    var unionSet = new mySet();
    var firstSet = this.values();
    var secondSet = otherSet.values();
    firstSet.forEach((element) => {
      unionSet.add(element);
    });
    secondSet.forEach((element) => {
      unionSet.add(element);
    });
    return unionSet;
  };

  this.intersection = function (otherSet) {
    var intersectionSet = new mySet();
    var firstSet = this.values();
    firstSet.forEach((element) => {
      if (otherSet.has(element)) {
        intersectionSet.add(element);
      }
    });
    return intersectionSet;
  };

  this.difference = function (otherSet) {
    var differenceSet = new mySet();
    var firstSet = this.values();
    firstSet.forEach((element) => {
      if (!otherSet.has(element)) {
        differenceSet.add(element);
      }
    });
    return differenceSet;
  };

  this.subset = function (otherSet) {
    var firstSet = this.values();
    return firstSet.every(function (value) {
      return otherSet.has(value);
    });
  };
}

var setA = new mySet();
var setB = new mySet();
setA.add('a');
setB.add('b');
setB.add('c');
setB.add('a');
setB.add('d');
console.log(setA.subset(setB));
console.log(setA.intersection(setB).values());

// ES6 기본 자료형을 써도 거의 유사하다. 대신 안되는 것들이 있다.
var setC = new Set();
var setD = new Set();
setC.add('a');
setD.add('b');
setD.add('c');
setD.add('a');
setD.add('d');

// .values 는 iterator 을 반환한다.
console.log(setD.values());
for (const value of setD.values()) {
  console.log(value);
}


// 얘들 안 됨
// console.log(setA.subset(setB));
// console.log(setA.intersection(setB).values());