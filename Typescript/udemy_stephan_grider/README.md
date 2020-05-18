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

## 외부 라이브러리

외부 라이브러리를 쓸 때, 그 라이브러리에 존재하는 다양한 함수 등의 타입을 정의해줄 필요가 있다. 물론 모든 라이브러리가 타입스크립트에 최적화되어있지는 않지만, `DefinitelyTyped` 라는 명칭을 붙여, typesecipt 와 쓰기 좋도록 `Type definition file` 을 제공하는 라이브러리도 많다. `axios` 같이 아예 내장되어서 다운 받아지는 것도 있고, 그게 아니라면 npm 에서 `@types/faker` 처럼 앞에 `@types` 를 붙여 라이브러리 검색을 해보자.

### google map api

구글 맵 api 처럼 아예 HTML 파일에 script 태그로 때려 넣어 전역 변수로 자바스크립트를 불러와 사용하는 경우에도 동일하게 `@types/googlemaps` 같은 걸 찾아서 `npm install` 해주어야 한다. **그런데** 특이하게도 바로 적용이 안되는 경우가 발생한다. 나같은 경우 프로젝트의 root 폴더가 현재 작업중인 `node_modules` 가 설치된 폴더가 아니라 다른 게 있을 경우에 그랬다. 그래서 이왕이면 항상 현재 프로젝트가 root 폴더인 상태에서 작업하는 게 건강에 이롭다.. 문제 해결법을 찾는 게 쉽지 않았다.

### 타입스크립트를 제대로 쓰는 법.

외부라이브러리를 쓸 때, `@types` 로 포팅된 코드를 제공한다면, `ctrl+click` 으로 파고 들어가 문서를 읽어보는 습관을 들이자. 공식 설명 문서 없이도 사용 방법을 알게 될 수 있다.

### 외부라이브러리 제한하기

외부 라이브러리를 쓰는 건 좋지만, 내가 직접 작성하지 않은 수많은 메서드들, 혹은 클래스들이 예정에 없게 호출되어 앱 전체가 점점 이해하기 어려운 스파게티 코드가 되는 것을 막을 필요가 있다. 즉 외부 라이브러리를 불러오는 곳을 따로 두고, 그 라이브러리에서 내가 내 앱에서 쓸 클래스나 메서드들을 따로 추출해서 내 앱으로 가져오는 것이 추후 생길 수 있는 혼란을 막을 수 있다. **커스텀** 해서 써야된다는 것이다. 물리적으로 완벽히 막을 수 없다고 해도, 적어도 쉽게 겉으로 티나지 않게라도 막아야만 쉽사리 앱이 망가지는 것을 막을 수 있다.

## | (or 조건연산자)

두 개의 타입을 | 로 엮어두면, 그 두 개의 타입을 서로 비교해 겹치는 property 영역만을 남긴다. 즉, 해당 조건이 들어간 곳의 함수 선언 내부에서 쓸 수 있는 property 가 제한된다. 그런데, 어차피 겹치는 것만 남기도록 연산된다면, 차라리 `interface` 로 사용할 property 를 따로 정의해서 사용하는 게, 대상 타입이 추가될 때마다 일일이 | 로 추가하는 짓을 안해도 되고 좋다. 

즉, 이렇게 `interface` 를 잘 사용하면 어떤 함수의 argument 가 되기 위한 **조건** 을 문지기로 두는 것과 같고, 문지기를 설정해놓았기 때문에, 굳이 타입들을 `import` 해서 직접 `| ` 조건연산자로 묶어둘 필요가 없어진다. ~ 이러한 조건에 맞으면 무엇이든 가능하다는 의미를 가지게 되는 것이다. 

> `interface` 는 두 개의 클래스가 서로 어떻게 연결될 것인지 **계약(Contract)** 을 맺어두는 것과 같다. 어떤 형식을 만족하면 어떤 것이든 받아들이겠다는 약속인 것이다.


## Better typescript Environment

1. `tsc --init` 으로 `tsconfig.json` 생성. 
1. `rootDir` 에 `./src` 를 작성해서 원본 소스 코드 폴더 지정
1. `outDir` 에 `./build` 작성해서 컴파일된 소스 코드 폴더 지정
1. 이제 `tsc` 라고만 치면 알아서 `tsconfig.json` 을 참고해서 컴파일 해준다.
1. 게다가 `tsc -w` 라고 하면, `rootDir` 폴더 내의 변경사항이 있으면 자동으로 컴파일해준다...  
1. 이제 전체 프로젝트 실행환경 세팅을 추가해보자.
1. `concurrently` 로, `nodemon` 과 `tsc -w` 를 동시에 실행해서 변경사항이 있을 때마다 타입스크립트 컴파일과 `nodejs` 로 파일 실행을 동시에 할 수 있다.
1. `npm install concurrently nodemon` 을 해주고,
1. `package.json` 에 다음 실행스크립트를 추가하자.
    ```json
      "start:build": "tsc -w",
      "start:run": "nodemon build/index.js",
      "start": "concurrently npm:start:*"
    ```
1. 참고로 `npm:start:*` 는, `start:` 뒤에 뭐든 붙은 모든 걸 한꺼번에 지칭하는 것이다.
1. 이제 `npm start` 를 하면, 처음에는 `nodemon` 이 타입스크립트 컴파일 되기 전에 `build/index.js` 파일을 실행시키려하기 때문에 에러가 발생한다.
1. 그러므로 일단 `ctrl + c` 로 종료한 후, 다시 실행하면 세팅이 완료된다.

## Type Guards

`|` 로 인자로 가능한 여러 데이터 타입을 union 해서 정의해놓으면, 그 두 데이터 타입의 교집합 속성 및 멤버함수만을 함수 내에서 사용할 수 있다. 즉, 둘 중 어떤 타입의 데이터가 오더라도 온전하게 사용할 수 없고 조각난 상태로 사용하게 된다.. 이 부분을 해결하기 위해 `|` 로 여러 타입을 union 해서 받아온 뒤, `if` 문으로 따로 type 검사를 하면 똑똑한 타입스크립트가 다시 온전한 상태의 데이터로 복원시켜 준다. 데이터 타입에 따라 Type guard 를 달리 쓴다. 

1. Number, String, Boolean, Symbol 인 경우: `typeof() == ''` 같이 일반적인 타입 검사 문법을 사용해 검사한다.
1. Object, Array, Class 등인 경우: `instanceof` 로 검사한다.

## interface & Abstract Class

- Abstract Class 를 쓰게 되면 interface 가 필요없어진다.
- 서로에게 종속된 클래스라면 상속과 Abstract Class 를 사용하고, 서로 별개의 클래스라면 interface 를 쓰는 게 맞다.

## Node js 기본 라이브러리의 Type Definition File

`fs`, `os`, `http` 같은 node 기본 라이브러리도 외부 라이브러리처럼 `@types/*` 같은 Type Definition File 을 다운 받아서 써야한다. 다만 그냥 `@types/node` 안에 전부 포함되어 있다.

## Type assertion

`row[5] as MatchResult,` 처럼 `row[5]` 가 `MatchResult` 의 타입(여기선 MatchResult 는 enum 타입) 일부임이 확실하다는 걸 타입스크립트에게 알려주기 위해 사용한다. 

## tuple 사용
어떤 배열의 각 요소마다 데이터타입이 다른 경우에, tuple 을 사용함으로써 모든 데이터 타입을 | 로 union 하는 짓을 막을 수 있다. tuple 은 일단 기본적으로 `Array` 로 여겨진다.

## Generics

- **Like function arguments**, but for types in class/function definitions
- Allows us to define the type of a property/argument/return value at a future point
- Used heavily when writing reusable code

흔히 `<T>` 로 많이 표시하는 것으로, 같은 클래스에 다양한 타입의 데이터를 멤버변수로 받아 사용하고 싶을 때, 데이터 타입마다 새로 클래스를 정의하지 않고 Generic 을 사용한다.

## A Huge Misconception around Composition

> "Favor object composition over class inheritance"  __ Design Patterns, page 20

디자인 패턴 책에 나와 유명해진 말인데, 대부분의 사람이 이것을 자바스크립트에 적용할 때 이상하게 오해해서 사용하고 있다. 많은 사람들이 Composition 이 단순히 여러 Object 를 합쳐서 사용함으로써 필드를 사용하는 방법을 늘리는 것으로 생각한다. 그러나 단순히 `Object.assign(obj1, obj2, obj3...)` 을 이용해서 Object 를 합쳐서 사용하는 것은, 겹치는 이름의 필드 혹은 메서드가 있기만 해도 그 합치는 순서에 따라 결과가 달라지는 아주 취약한 구조의 사용법이다. 

위 사용법은 `Multiple Inheritance`, 즉 그냥 여러 곳에서 단순 복사 붙여넣기해서 사용하는 수준에 불과하다. **Design patterns** 의 저자가 권장하는 composition 은 그런 것이 아니라, 주로 **Delegation** 개념을 이용해, 어떤 요청이 들어왔을 때, 두 개의 클래스가 그 요청을 처리하게 되고, 한 클래스가 다른 클래스에 특정 데이터 처리(data operation) 을 위임(delegation)해서 요청을 처리하게 된다.