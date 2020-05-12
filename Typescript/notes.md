## 명령어 단축

`ts-node index.ts` : `tsc index.ts` + `node index.js`

## types

**Type** : Easy way to refer to the different properties + functions that a value has.
**이름을 붙이는** 것이라 생각하자. 어떤 json data 를 받았을 때, 그 json data 가 어떤 property 를 가진 data 인지를 계속 말하기 보다, 그냥 `User` 라고 이름 붙이는 거다. 그래서 이 json data 는 `User` 다. 라고 말할 수 있게 된다. 물론 그 `User` 가 그래서 뭘 가지고 있는지는 `interface` 로 정의했던 `User` 를 더 들여다보면 되겠지.

## Type annotations and Type inference

annotations 은 개발자가 타입스크립트가 곧바로 알 수 있게 직접 작성하는 것이고, Inference 는 타입스크립트가 알아서 예측하는 것이다.

Inference 의 경우, 변수의 선언과 함께 곧바로 초기화를 하면 쉽게 예측한다. 따라서, 대부분의 단순 변수 선언에서 굳이 Type annotation 을 해줄 필요는 없이 Type inference 에 의존할 수 있다.

함수의 inference 는 매개변수는 추측하지 않고 return value 만 추측한다.
그래서 매개변수에 대한 타입을 적어놨다면 return 타입은 보통 알아서 추측해준다. **하지만** 무조건 리턴 값 타입도 쓰는걸 추천한다. 그래야만 혹시나 return 구문을 빼먹거나 헀을 때 경고를 받을 수 있다.

## parameter destructuring

타입은 무조건 : 로 구분해서 오른쪽에다 쓴다. destructuring 이 일어났을 때도!
그리고 destructuring 을 했다면, 오른쪽 타입들도 그 destructuring 문법을 따라해주어야 한다. (obj 분해했으면 타입도 중괄호 안에 넣어야 함)

```js
const logWeather = (forecast: { date: Date, weather: string }): void => {
  console.log(forecast.date);
  console.log(forecast.weather);
};

// ES2015 destructuring
const logWeather2015 = ({ date, weather }: { date: Date, weather: string }) => {
  console.log(date);
  console.log(weather);
};
```

### Where to use typed arrays?

Any time we need to represent a collection of records with some arbitrary sort order

### interface + Classes

interface 와 Class 를 잘 조합해서 쓰는게 타입스크립트의 진수다.

`interface`: Creates a new type, describing the property names and value types of an object

interface 는 타입을 정의하지만, 어떤 obj 가 interface 에서 정의된 타입 개수 이상의 property 를 가지고 있다고 해서 문제삼지 않는다. 이렇게 최소한의 공통점만 있으면 같은 interface Type 로 분류될 수 있다는 점을 이용해 Reusable 한 코드를 작성하는 데 도움받을 수 있다. 

## Classes
`private` 는 오직 자기 자신 안에서만 호출 가능하고 상속받은 자식 클래스에서도 호출이 불가능하지만, 
`protected` 로 선언된 멤버함수는 해당 클래스 내에서, 혹은 그 클래스를 상속 받은 클래스 내에서만 호출될 수 있다. (인스턴스에서 . 접근자로 호출 불가능.)

### 멤버변수 훨씬 짧게 정의하기 

매개변수 자리에 아예 `public`, `private` 혹은 `protected` 이라고 써주면 알아서 멤버 변수로 사용가능하게 된다.

```js
  // color: string;

  constructor(public color: string) {
    // this.color = color;
  }
```