# TYPESCRIPT



## 명령어 단축

`ts-node index.ts` : `tsc index.ts` + `node index.js`



## 컴파일 옵션

`tsc index.ts` 처럼 `tsc` 명령어로 타입스크립트 파일을 컴파일하면 되지만, 컴파일 옵션을 다양하게 바꿀 수 있다는 걸 알아야 한다. 명령어 조합으로 옵션을 바꿀 수도 있지만 보통 `touch tsconfig.json`과 같은 명령어로 `tsconfig.json` 파일을 만들어서 따로 컴파일 옵션을 지정한다. 



### target

어떤 자바스크립트로 컴파일할 지 결정한다. 예를 들어 "ESNext"  로 설정하면 `async`, `await` 도 natively 지원하는 최신 문법으로 컴파일한다. (즉, 컴파일 결과물이 달라지는 거의 게 없다.)  Default value 는 `"ES3"` 로, `async`, `await` 을 쓰고 있었다면 비슷한 결과를 내기 위해 미친듯이 복잡한 자바스크립트 코드로 컴파일되는 걸 볼 수 있다.

```json
{
    "compilerOptions": {
        "target": "ESNext"
    }
}
```

### watch

`"watch" : true` 는 파일을 저장할 때마다 recompile 을 자동으로 해주는 옵션이다.





## types

**Type** : Easy way to refer to the different properties + functions that a value has.
**이름을 붙이는** 것이라 생각하자. 어떤 json data 를 받았을 때, 그 json data 가 어떤 property 를 가진 data 인지를 하나하나씩 설명하기 보다, 그냥 `User` 라고 이름 붙이는 거다. 그래서 이 json data 는 `User` 다. 라고 말할 수 있게 된다. 물론 그 `User` 가 그래서 뭘 가지고 있는지는 `interface` 로 정의했던 `User` 를 더 들여다보면 되겠지.

## Type annotations and Type inference

annotations 은 개발자가 타입스크립트가 곧바로 알 수 있게 직접 작성하는 것이고, Inference 는 타입스크립트가 알아서 예측하는 것이다.

Inference 의 경우, 변수의 **선언과 함께 곧바로 초기화**를 하면 쉽게 예측한다. 따라서, 대부분의 단순 변수 선언에서 굳이 Type annotation 을 해줄 필요는 없이 Type inference 에 의존할 수 있다.

함수의 inference 는 매개변수는 추측하지 않고 return value 만 추측한다.
그래서 매개변수에 대한 타입을 적어놨다면 return 타입은 보통 알아서 추측해준다. **하지만** 무조건 리턴 값 타입도 쓰는걸 추천한다. 그래야만 혹시나 return 구문을 빼먹거나 헀을 때 경고를 받을 수 있다. (return 값의 타입은 매개변수를 넣는 괄호 오른쪽에 쓴다.)

## parameter destructuring

타입은 무조건 **:** 로 구분해서 오른쪽에다 쓴다. destructuring 이 일어났을 때도!
그리고 destructuring 을 했다면, 오른쪽 타입들도 그 destructuring 문법을 따라해주어야 한다. (obj 분해했으면 타입도 중괄호(객체처럼) 안에 넣어야 함)

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

즉, 이렇게 `interface` 를 잘 사용하면 어떤 함수의 argument 가 되기 위한 **조건** 을 문지기로 두는 것과 같고, 문지기를 설정해놓았기 때문에, 굳이 타입들을 `import` 해서 직접 `|` 조건연산자로 묶어둘 필요가 없어진다. ~ 이러한 조건에 맞으면 무엇이든 가능하다는 의미를 가지게 되는 것이다.

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
`const id = attrs.get('id') as number` 같은 식으로도 씀. 

## tuple 사용

어떤 배열의 각 요소마다 데이터타입이 다른 경우에, tuple 을 사용함으로써 모든 데이터 타입을 | 로 union 하는 짓을 막을 수 있다. tuple 은 일단 기본적으로 `Array` 로 여겨진다.

## Generics

- **Like function arguments**, but for types in class/function definitions
- Allows us to define the type of a property/argument/return value at a future point
- Used heavily when writing reusable code

흔히 `<T>` 로 많이 표시하는 것으로, 같은 클래스에 다양한 타입의 데이터를 멤버변수로 받아 사용하고 싶을 때, 데이터 타입마다 새로 클래스를 정의하지 않고 Generic 을 사용한다.

### Generic constraint

`<T extends SomeInterface>` 와 같은 문법으로, generic 이 받을 수 있는 **다양한** 타입의 범위를 줄여줄 수 있다. 마치 "아무나는 아니고, 이건 만족시켜야 돼" 같은 제약 조건을 걸어주는 것이다. (남녀 조건 따지는 것 같네)

## A Huge Misconception around Composition

> "Favor object composition over class inheritance" \_\_ Design Patterns, page 20

디자인 패턴 책에 나와 유명해진 말인데, 대부분의 사람이 이것을 자바스크립트에 적용할 때 이상하게 오해해서 사용하고 있다. 많은 사람들이 Composition 이 단순히 여러 Object 를 합쳐서 사용함으로써 필드를 사용하는 방법을 늘리는 것으로 생각한다. 그러나 단순히 `Object.assign(obj1, obj2, obj3...)` 을 이용해서 Object 를 합쳐서 사용하는 것은, 겹치는 이름의 필드 혹은 메서드가 있기만 해도 그 합치는 순서에 따라 결과가 달라지는 아주 취약한 구조의 사용법이다.

위 사용법은 `Multiple Inheritance`, 즉 그냥 여러 곳에서 단순 복사 붙여넣기해서 사용하는 수준에 불과하다. **Design patterns** 의 저자가 권장하는 composition 은 그런 것이 아니라, 주로 **Delegation** 개념을 이용해, 어떤 요청이 들어왔을 때, 두 개의 클래스가 그 요청을 처리하게 되고, 한 클래스가 다른 클래스에 특정 데이터 처리(data operation) 을 위임(delegation)해서 요청을 처리하게 된다.

## Optional Interface props

interface props 뒤에 ? 를 붙여 선택적으로 넣을 수 있게 할 수 있다.

```typescript
interface UserProps {
  name?: string;
  age?: number;
}
```

## 함수 타입 정의

함수도 물론 타입으로 정의할 수 있다. 아래는 아무런 인자도 받지 않고, 리턴하는 것도 없는 함수타입의 정의다.

`type Callback = () => void;`

`() => {}` 라고 해버리면 object 를 반환하는 게 되어버림에 주의해야 한다.


## 재사용 가능한 코드를 만들기 위한 Two important rules

단순히 클래스를 generic 이라고 만들어 놓아도, 정작 클래스 안의 메서드들은, 어떤 Type 를 인자로 받고, 그에 따라 어떤 타입을 반환하게 될 지 모르게 된다. 그런데 그렇다고 **Union** 을 이용해서 죄다 **|** 로 이 중에 암거나.. 라고 써 놓으면 그 타입들끼리 중복되는 attribute 혹은 method 만 사용 가능하기 때문에 개발에 상당한 지장이 생긴다. 그렇다고 또 일일이 **type guard** 를 if 문으로 만들어 쓰려면 손에 쥐가 난다. 이 상황을 해결하기 위해 쓰이는 것이 메서드 함수에 또다른 generic 을 붙이는 것이다. 그리고 이 메서드 제네릭을 이해하기 위한 2가지 규칙이 아래와 같다.

1. In typescript, strings can be types
1. In JS(and therefore TS), all objects keys are strings

1 번 룰 예:

```typescript
type BestName = 'Taewoo';

const printName = (name: BestName): void => {

};

// 위처럼 해놓은 경우, 오직 `Taewoo` 만이 인자로 들어갈 수 있다. 

printName('Taewoo'); // 이것 외엔 모두 에러 발생
```

2번 룰 예:

```javascript
const colors = {}
colors[5] = 'red'
colors[5] // 'red'
// 위처럼 했을 때, 비록 숫자가 key 가 된 것 같아 보이지만,
// 실제로는 colors['5'] 처럼 저장되어 있다.
// 즉 자바스크립트 객체의 키는 모두 string 이다.
```

위 2개의 룰이 무슨 상관인가 할 수 있다. 하지만 위 두 개를 조합하면,

> Keys of an object can be types

라는 뜻이 된다. 

그래서 이제 어떤 generic class 를 만들었을 때 **T** 라는 객체를 넘겨준다면, 오직 그 **T** 가 가지고 있는 **Keys**, 즉 **K** 만이 사용될 수 있음을 typescript 에게 알려줄 수 있다. 마치 클래스 메서드의 generic constranit 를 `extends` 키워드로 먹였듯이, 메서드에도 generic constranit 를 먹이면 된다.

```typescript
export class Attributes<T> {
  constructor(private data: T) {}

  get<K extends keyof T>(key: K): T[K] {
    return this.data[key];
  }
}
```

## `get` accessor 의 delegation 위주 composition 패턴에서의 활용법.

클래스 메서드 앞에 `get` 키워드를 붙이면, getter 가 되어 메서드임에도 호출할 때 괄호를 붙이지 않아도 된다. 즉, "오직 클래스 attribute 에 접근할 뿐이지, 어떤 걸 변경하는 행동을 수행할 의도가 없다." 라는 것을 확실히 할 수 있다.

그런데 이게 클래스가 자신이 가진 메서드 내에서 처리를 하는 게 아닌 composition 디자인 패턴에서 매우 유용하다. 자신이 위임한 클래스까지 타고 들어가 그 클래스의 메서드를 실행해야 한다면 최상단에서 유저가 어떤 메서드를 호출하고 싶을 때 호출 코드가 `.` 을 타고타고 들어가는 못생긴 코드가 될 것이다. 그런데 `getter` 를 잘 활용하면, 오직 reference 만을 반환함으로써, 최상단에서 유저가 괄호(`()`) 로 호출 하는 메서드가 처리를 위임받은 깊숙한 곳의 메서드가 되도록 할 수 있다. 물론 `this` 가 엉키는 사태가 일어나는데, 그래서 위임받는 클래스들의 메서드들은 거의 100% 화살표 함수로 정의하는 것이 좋다.

이걸 **Passthrough Methods** 라고 부른다. 특정상황에서 좀 더 짧게 쓰는 팁이 있다면, 애초에 reference 를 반환할 뿐이기 때문에, 굳이 `get` 키워드 쓰지 않고 클래스 attribute 처럼 곧바로 써도 똑같이 동작한다. 다만 이렇게 쓰고 싶다면 이 reference 가 되는 다른 class 들이 `constructor` 에서 인자로 받아들여져서, 가장 빠른 타이밍에 이미 초기화 되어있어야 한다. 즉, constructor 밖에서 초기화가 이루어지면 타이밍이 늦어 `undefined` 가 되어버린다. 


```typescript
  // 오직 reference 만을 반환한다.
  // 근데 그렇기 땜에 `get` 이란 키워드 없이
  // 그냥 attribute 처럼 써놔도 똑같이 동작한다.
  // get on() {
  //   return this.events.on;
  // }
  on = this.events.on; // 아래 것들도 이렇게 가능.

  get trigger() {
    return this.events.trigger;
  }

  get get() {
    return this.attributes.get;
  }
```



## Decorators



데코레이터는 그냥 Function 인데, 

1. 내 source code 에 hook in 해서, 그 코드의 기능을 확장하거나 수정할 수 있다.
2. meta data 로 주석을 남길 수 있다. 이 주석 다는 기능은 사실 angular compiler 같이 dependency injection 같은 기능이 필요할 때 쓴다.. 1번에 집중하자.

### 추가 설명(udemy)

1. **class** 내의 property/method 를 수정하고, 바꾸는 등의 역할을 할 수 있는 함수들
2. vanilla javascript 의 decorator와 **다르다.**
3. 오직 `class` 내부에서만 사용된다. 
4. 데코레이터가 실행되는 순서를 이해하는 것이 중요하다. (decorator 는 composable 하기에, 여러 개가 한 번에 한 대상에 적용될 수 있다. 보통은 위에서 아래로 실행된다.)
5. 아직 실험중인 기능이다.

### 추가 설명(Toast UI Article)

[아주 정성들여 설명해주고 있는 글이다.](https://ui.toast.com/weekly-pick/ko_20200102/) 이 글을 읽으면 자바스크립트 객체의 숨겨진 작동방식 중 하나인 **속성 설명자**, 즉 `PropertyDescriptor` 가 데코레이터를 이해하는 데 큰 도움이 된다는 것을 알 수 있다.



### 5 things that can be decorated

#### 01. class definitions (덜 중요)

- class decorator는 constructor 를 인자로 받는다.

```typescript
function Frozen(constructor: Function) {
    Object.freeze(constructor);
    Object.freeze(constructor.prototype);
}

// 컴포넌트 class 에 Decorator 적용사례
@Frozen
export class IceCreamComponent {
    
}

// 제대로 적용되었는지 확인
console.log(Object.isFrozen(IceCreamComponent))

class Froyo extends IceCreamComponent {} // 에러 발생! readonly 상태기 때문에 부모 컴포넌트가 될 수 없다.
```



#### 02.properties (중요!)

- 상당히 실용적으로 많이 쓰이는 사례. 예를 들어 `스텐실` 이라는 웹 컴포넌트 프레임워크에서는, 그냥 클래스 property 에 `@state` 를 붙이기만 하면 그 속성이 변경될 때 리렌더링이 발생하게 할 수 있다. 마법같이!
- property decorator 가 인자로 받는 2가지는 target(parent class) 와 key (property we are decorating)이다
- property decorator 는 factory Function 으로 쓰이는 게 권장된다. 왜냐하면 필요에 따라 자신의 custom 데이터를 **클로저**의 특성을 이용해 사용할 수 있기 때문이다.

```typescript
// Property decorator
/// Factory Function 임을 알 수 있다. 
function Emoji() {
    // 여기에 어떤 변수를 작성하면 클로저를 이용해 privately 하게 쓸 수 있겠지
    return function(target: Object, key: string | symbol) {
        let val = target[key];
        const getter = () => {
            return val;
        };
        const setter = (next) => {
            console.log('updating flavor...');
            val = `:-) ${next} :-)`;
        };
        
        // override initial property
        Object.defineProperty(target, key, {
            get: getter,
            set: setter, 
            enumerable: true,
            configurable: true
        });
    }
}

export class IceCreamComponent {
    @Emoji() // Emoji 데코레이터는 Factory Function 이다.
    flavor = 'vanilla'; // 앞 뒤로 ':-)' 붙음
}
```



#### 03. method decorator (중요!)

- 얘도 주로 factory function 쓴다.
- 3개를 인자로 받는데, 앞 2개는 property decorator 와 동일하고, 3번째는 대상 method 자기 자신이다. 자료형이 `propertyDescriptor` 인 이유는, **메서드도 결국 어떤 object 의 property** 며, 단지 그 값이 함수일 뿐이기 때문이다. 

```typescript
function Confirmable(message: string) {
    return function(target: Object, key: string|Symbol, descriptor: PropertyDescriptor){
        // 원본 값은 original 에 저장
   		const original = descriptor.value;
        // 원하는대로 메서드 수정(다만 화살표 함수여선 안 된다. this 를 쓸 일이 있어)
        descriptor.value = function(...args: any[]) {
            // 여기서는 단순히 confirm 메시지 참/거짓에 따라 실행 or 취소
            const allow = confirm(message);
            if(allow) {
                const result = original.apply(this, args);
                return result;
            } else {
                return null;
            }
        }
    }
}

export class IceCreamComponent {
    @Emoji()
    flavor = 'vanilla';
	
	toppings = [];
	
	@Confirmable('Are you sure?')
	@Confirmable('checked again?') // 데코레이터는 composable 하기에 여러 개 적용가능
	addToping(topping = 'sprinkles') {
        this.topings.push(topping);
    }
}
```



#### 04. accessors

- getter 이나 setter 을 말함
- 대체로 method decorator 와 비슷하지만, 기존 descriptor 의 `value` 가 아닌 `get`  을 override 한다. 

```typescript
function WithTax(rate: number) {
    return function(target: any, key: string, descriptor: PropertyDescriptor) {
        const original = descriptor.get;
        
        descriptor.get = function() {
            const result = original.apply(this);
            return (result * (1+rate)).toFixed(2);
        };
        return descriptor;
    }
}

export class IceCreamComponent {
    @Emoji()
    flavor = 'vanilla';
	
	toppings = [];
	
	@Confirmable('Are you sure?')
	addToping(topping = 'sprinkles') {
        this.toppings.push(topping);
    }
	
	@WithTax(0.15)
	get price() {
        return 5.00 + 0.25 * this.toppings.length;
    }
	
}
```



#### 05. Parameters

- 음.. 이건 다음에



### Decorator 로 Angular 에 React Hook 같은 걸 만들어보기



```typescript
import {Component} from '@angular/core';

@component({
    selector: 'app-hooks',
    template: `
		<p>You clicked {{count}} times </p>
		<button (click)="setCount(count+1)">Click me! </button>
	`,
})
export class HooksComponent {
    @useState(0) count; setCount; // property decorator. 0 초기값, getter, setter 순
    
    @useEffect() // method decorator. initial value 나 변화시마다 동작
    onEffect() {
        document.title = `You clicked ${this.count} times`;
    }
}

function UseState(seed: any) {
    return function(target, key) {
        target[key] = seed;
        // 메서드 정의
        target[`set${key.replace(/^\w/, c => c.toUpperCase())}`] = (val) => target[key]
    }
}

function UseEffect() {
    // 앵귤러에 이미 내재된 life cycle hook 이용
    return function (target, key, descriptor) {
        target.ngOnInit = descriptor.value;
        target.ngAfterViewChecked = descriptor.value;
    }
}
```





## Typescript with React

- `npx create-react-app --template typescript` 를 이용하면 간편하게 타입스크립트가 적용된 프로젝트를 생성할 수 있다.

- 컴포넌트를 반환해야 하는 경우, 확장자가 `.tsx` 라는, jsx 를 사용하는 타입스크립트 파일을 사용한다. 그럴 필요가 없으면 그냥 `.ts` 파일을 쓴다.

### props with Typescript

`React.Component` 에 마우스를 올려보면, Generic 으로 `P = {}`, 즉 props 를 받는다는 걸 알 수 있다. 그래서 interface 안에 props 로 들어갈 것들을 정의하고, 그것을 `React.Component<AppProps>` 같은 형식으로 넣어주면 된다. 



### state with Typescript

React 컴포넌트 내에서 `constructor` 내에서 `this.state = {~~}` 와 같이 state 를 정의하려고 하면, 제대로 그 state 를 쓰지 못하는 사태가 발생한다. 그 이유는, 기본적으로 React.Component 의 `S`, 즉 state 는 `ReadOnly` 이기 때문이다. 즉 React.Component 내부에서 State 를 쓰고 싶다면 아래 두 가지 중 하나를 써야 한다.

1. 클래스 내부에서 property 로 직접적으로 State 를 선언해서 Overriding 해버리거나,
2. Props 를 Generic 으로 넣어줬듯이 두번째 Generic 으로 State 에 대한 `interface` 를 넣어줘야 한다.

혹시나 두 가지 방법을 동시에 써버리면, 오버라이딩 해버린 게 더 뒤에 작동하므로, 오버라이딩된 state 가 사용됨에 유의하자!



```typescript
interface AppProps {
  color: string;
}

interface AppState {
  counter: number;
}

class App extends React.Component<AppProps, AppState> {
  // state = {counter: 0}; // STATE 를 사용하는 한가지 방법. 이건 extend 한 Component의 state 를 오버라이딩 해버리고 사용한다.
	
  // constructor 를 사용.
  constructor(props: AppProps) {
    super(props);
    this.state = {counter: 0}
  }

  onIncrement = ():void => {
    this.setState({counter:this.state.counter+1})
  };

  onDecrement = ():void => {
    this.setState({counter: this.state.counter - 1})
  }
  
  render() {
    return (
      <div>
        <button onClick={this.onIncrement}>Increment</button>
        <button onClick={this.onDecrement}>Decrement</button>
        {this.state.counter}
      </div>
    )
  }
}
```





### Functional Component with Typescript

`JSX.Element` 타입을 반환하는 함수형 컴포넌트를 사용할 수 있다.

```typescript
const App = (props: AppProps): JSX.Element => {
    return <div>{props.color}</div>
}
```



## Async Action Creator with Typescript

`redux-thunk` 미들웨어를 사용한 Async 액션을 생성하려고 해도, 인자로 받는 `dispatch` 등이 어떤 type 이어야하는지 알기 어렵다. 이럴 때 라이브러리를 파고들어 분석할 필요가 있다. `import 'redux'` 와 같이 임의로 라이브러리를 불러들이는 코드를 만든 후, `ctrl` + `click` 을 통해 `dispatch` 가 어떤 type 이어야 하는지 찾을 수 있다. 검색 등을 통해 찾아보면, Axios 내에 `Dispatch` 라는 interface 가 정의되어 있음을 알 수 있고, 그럼 그 `interface` 를 `import` 해서 사용할 수 있다. 완성된 코드는 아래와 비슷할 것이다.



```typescript
import axios from 'axios'
import {Dispatch} from 'redux';

const url = 'https://jsonplaceholder.typicode.com/todos'

export const fetchTodos = () => {
  return async (dispatch: Dispatch) => {
    const response = await axios.get(url);

    dispatch({
      type: 'FETCH_TODOS',
      payload: response.data
    });
  };
};
```



하지만 이렇게 만든 코드도 여전히 

1. `response` 변수가 받아오는 값이 어떤 타입인지 정보가 없으며,
2. 현재 action creator 가 반환하는 action Object 내의`payload` 도 오류가 발생하기 쉬운 단순 문자열로 전달되고 있음을 볼 수 있다.  (enum 을 이용해 해결)

1번 문제의 경우, 우리가 API 를 통해 받아올 JSON 데이터에서 사용할 property 들을 일일이 interface 로 정의해서, 그 객체의 리스트를 받아올 것임을(상황에 따라 그냥 객체일수도 있고) 명시하면 된다. 

2번 문제의 경우, `enum` 을 사용하면 굳이 문자열로 정의할 필요도 없이, 순서대로 0부터 고유값이 배정되는 `enum` 의 특성을 살려 action 을 구분하는 type 을 정의할 수 있다.

```typescript
import axios from 'axios'
import {Dispatch} from 'redux';
import {ActionTypes} from './types'
// ActionType 의 형태
//export enum ActionTypes {
//  fetchTodos
//}

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

const url = 'https://jsonplaceholder.typicode.com/todos'

export const fetchTodos = () => {
  return async (dispatch: Dispatch) => {
    const response = await axios.get<Todo[]>(url);

    dispatch({
      type: ActionTypes.fetchTodos,
      payload: response.data
    });
  };
};
```



### Action interface

위와 같이 ActionCreator 내부에서 반환하는 Action 이 결국 어떤 형태여야 하는지 `Optional Generic` 으로 추가하고 `interface` 를 집어넣음으로써, 의도치 않게 이상한 Action 을 dispatch 하게 되는 상황을 막을 수 있다.

```typescript
interface FetchTodosAction {
  type: ActionTypes.fetchTodos;
  payload: Todo[];
}

const url = 'https://jsonplaceholder.typicode.com/todos'

export const fetchTodos = () => {
  return async (dispatch: Dispatch) => {
    const response = await axios.get<Todo[]>(url);

    // 실수 방지
    dispatch<FetchTodosAction>({
      type: ActionTypes.fetchTodos,
      payload: response.data
    });
  };
};
```



## reducers and Typescript

개별 Reducer 뿐만 아니라 전체 Reducers 를 합치는 `reducers/index.ts` 파일의 `combineReducers` 에도 typescript 를 이용해 데이터 결함을 방지할 수 있다. 



`combineReducers` 함수의 Generic 으로 사용될 `interface` 를 정의해놓으면, 전체 store 가 어떤 데이터를 가져야만 하는지 한 눈에 볼 수 있게 된다.

```typescript
import { combineReducers } from 'redux';
import { todosReducer } from './todos';
import { Todo } from '../actions';

export interface StoreState {
  todos: Todo[];
}

export const reducers = combineReducers<StoreState>({
  todos: todosReducer,
});
```



### Connecting a component to Redux Store with Typescript



`connect` 를 이용해 컴포넌트를 redux 에 연결할 때도, 추가적으로 작업할 게 있다. 우선 컴포넌트가 받을 `AppProps` 의 types 를 interface 로 정의해서 component 의 generic 으로 넣어야 하며, typescript 에서는 `export default` 를 사용하지 않는 것을 권장하기 때문에, 기본 컴포넌트를 `_ComponentName` 같이 언더바를 붙인 형태의 이름 붙였다가, `connect` 를 통해 연결된 것을 언더바를 제거한 형태의 이름으로 export 한다.

```typescript
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Todo, fetchTodos } from '../actions';
import { StoreState } from '../reducers';

interface AppProps {
  todos: Todo[];
  fetchTodos(): any;
}

class _App extends Component<AppProps> {
  render() {
    return <div>Hi there!</div>;
  }
}

const mapStateToProps = ({todos}: StoreState): { todos: Todo[] } => ({
  todos: todos,
});

const mapDispatchToProps = {
  fetchTodos
};

export const App = connect(mapStateToProps, mapDispatchToProps)(_App);
```

