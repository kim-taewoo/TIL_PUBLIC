# 3.3 Functions

## 세미콜론이 끝에 붙느냐의 여부가 아주 중요하다.

세미콜론으로 끝나면 expression 이 아니라 statement 가 되면서 리턴값을 반환하지 않게 된다. 즉 값을 반환하는 것은 expression 이다.
Note the x + 1 line without a semicolon at the end, which is unlike most of the lines you’ve seen so far. Expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement, which will then not return a value.

## 함수는 바디의 마지막 expression 값을 반환한다. early return 을 위해 `return` 키워드를 사용할 수 있기는 하다. 함수의 리턴 타입은 -> 로 표시한다.

In Rust, the return value of the function is synonymous with the value of the final expression in the block of the body of a function. You can return early from a function by using the return keyword and specifying a value, but most functions return the last expression implicitly. Here’s an example of a function that returns a value:

```rust
fn five() -> i32 {
    5 // 숫자는 그 자체로 expression 으로, 값을 반환한다. (자기 자신)
}

fn main() {
    let x = five();

    println!("The value of x is: {}", x);
}

```

## if 도 expression 이다. 즉, 값을 반환한다.

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {}", number);
}
```

## Rust 의 반복. loop, while, for

loop 은 시작 조건문이 없는 while 문이며, ctrl+c 로 강제로 종료하거나 break 코드로 중단될 수 있다. 자바스크립트라면 while(true){} 로 쓰는 스타일

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result);
}

// while
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}

// for in
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the value is: {}", element);
    }
}
```

for 보다 while 으로 조건 체크하며 순회하는 게 더 느리다고 한다. 그래서 거의 모든 경우에 for 을 쓰는 것이 권장된다. 아래 코드는 Range 를 사용해서 출력하는 경우.
But this approach is error prone; we could cause the program to panic if the index length is incorrect. It’s also slow, because the compiler adds runtime code to perform the conditional check on every element on every iteration through the loop.

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
```
