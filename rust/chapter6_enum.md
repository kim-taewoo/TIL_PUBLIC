# Enums

- _Rust’s enums are most similar to algebraic data types in functional languages, such as F#, OCaml, and Haskell._
- enum 의 필드는 'variants` 라고 부르는 듯하다. 이 변종? 중 하나를 택해야 한다는 느낌.
- 네임스페이스처럼 `::` 를 이용해서 enum 안의 variants 에 접근할 수 있다.

```rust
enum IpAddrKind {
  V4,
  V6,
}

let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

- 좀 더 많은 정보를 표현하기 위해 Struct 와 조합해서 쓸 수도 있지만, enum 의 각 variant 에 데이터를 직접적으로 넣어둘 수도 있다.

```rust
enum IpAddr {
  V4(String),
  V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));
let home = IpAddr::V6(String::from("::1"));
```

- 같은 타입이라면 같은 필드 타입을 가져야 하는 struct 와 달리, enum 은 같은 enum 타입 내에서 variant 마다 타입을 달리 할 수 있다는 장점이 있다.

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```

- enum 의 각 variant 가 가질 수 있는 타입은 아주 다양해서 struct 든 다른 enum 이든 다 넣을 수 있다. 즉, **enum은 사실상 struct 들을 한 번 더 그룹화해서 관리하기 편하게 한 것이라고 볼 수 있다.**

```rust
enum Message {
    Quit, // 관계된 데이터없음. unit struct 와 유사
    Move { x: i32, y: i32 }, // 익명 struct
    Write(String), // tuple struct 와 유사
    ChangeColor(i32, i32, i32), // tuple struct 와 유사
}
```

- 심지어 enum 메서드도 정의할 수 있다!

```rust
impl Message {
    fn call(&self) {
        // method body would be defined here
    }
}

let m = Message::Write(String::from("hello"));
m.call();
```

# `match` control flow operator

- 어떤 값을 패턴들에 대입해보고 매칭되면 그에 맞는 코드를 실행시킨다.
- 패턴은 literal values, variable names, wildcards, 등 다양하다.
- `if` 와 유사해보이지만, boolean 으로 판별하기 보다 그냥 타입 비교만으로도 가능하다는 점에서 차이가 있다.
- `=>` 으로 match arms 가 표현된다. 화살표 앞은 패턴이고, 뒤에는 실행할 코드다. 다음 arm 과는 쉼표로 구분되며, 여러 줄의 코드인 경우 중괄호를 쓴다.
- 첫번째 매칭이 되면 그 뒤 패턴으로 검사하지 않는다.

```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

- match 패턴으로 매칭되는 타입의 값까지 가져올 수 있다.
- 위 내용을 바탕으로 `Option<T>` 에서 `T` 의 값도 꺼낼 수 있다.

```rust
fn main() {
    fn plus_one(x: Option<i32>) -> Option<i32> {
        match x {
            None => None, // x 가 None 인 경우
            Some(i) => Some(i + 1), // x 가 값을 가지고 있을 경우 연산. i 가 Some 타입이 가지고 있는 값의 변수로 바인딩됨.
        }
    }

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
}

```

- 이렇게 match 로 enum 내 값을 변수로 할당해 코드를 호출할 수 있다는 건 상당히 어색하게 느껴지지만, 익숙해지면 아주 평가가 좋다고 한다.
- 기본적으로 러스트 match 는 가능한 모든 패턴을 커버해야 하지만, `_` 를 이용해서 default 커버 코드를 작성할 수 있다. 예를 들어 아무것도 하지 않을 것이라면 `_ => ()` 를 작성해둔다.

# if let

- if let 으로 '한 개의 케이스와 매칭될 때' 의 상황만 다루고 나머지는 무시하는 코드를 간략하게 작성할 수 있다.

```rust
let some_u8_value = Some(0u8);
match some_u8_value {
    Some(3) => println!("three"),
    _ => (), // 이렇게 default 커버를 해줘야 하는 귀찮음.
}
```

```rust
let some_u8_value = Some(0u8);
if let Some(3) = some_u8_value {
    println!("three");
}
```

- 위처럼 `패턴 = expression` 형태로 줄여서 쓸 수 있다.
- else 키워드로 `_` 의 default 커버를 구현할 수 있다.
