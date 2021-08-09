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

# 4. Understanding Ownership

러스트의 유니크한 기능으로, 가비지 컬렉터 없이도 메모리 safety 를 보장할 수 있게 해준다.
연관된 개념으로는 borrowing, slices, and how Rust lays data out in memory 가 있다.

보통 어떤 프로그램이 컴퓨터의 메모리를 관리하는 방법은 크게 2가지가 있다.

1. 가비지 컬렉터를 이용해서 계속해서 사용되지 않는 메모리를 찾아낸다.
2. 프로그래머가 코드로 직접 메모리를 할당하고 해제한다.

러스트는 3번째 방법을 사용한다. 메모리는 컴파일러가 컴파일타임에 특정 법칙(rules) 을 체크하면서 system of ownership 에 의해 관리된다. 그리고 이 ownership 기능은 프로그램이 실행되는 동안 속도를 저하시키지 않는다.

ownership 은 새로운 개념이기 때문에, 받아들이는 데 시간이 걸린다. 하지만 이 개념을 익힐수록 자연스럽게 안전하고 효율적인 코드를 짤 수 있게 된다. 힘내라!

ownership 을 이해하면, Rust 를 특별하게 만드는 특성들을 탄탄하게 이해할 수 있다.

아주 흔한 데이터 자료형인 strings 로 ownership 을 배워보자.

## The Stack and the Heap

Rust 와 같은 시스템 프로그래밍 언어에서는 다른 언어에서보다 어떤 값이 Stack 에 들어가느냐 Heap 에 들어가느냐가 중요하다. ownership 도 이와 관련있다.

스택과 힙 모두 런타임에 사용할 수 있는 메모리의 일부인데, 스택은 LIFO, 힙은 FIFO 의 특성을 가진다.

또한 스택은 반드시 fixed size 를 가진 데이터를 저장하므로, 어떤 데이터의 사이즈를 알 수 없거나 사이즈가 변경될 수 있다면 heap에 저장되어야 한다. 힙은 좀 덜 정돈된 구조로, 데이터를 힙에 넣을 때는 그 데이터를 넣을 수 있는 충분한 크기의 공간을 할당하고 그 공간을 가리키는 포인터를 반환한다. 이 과정을 `allocating on the heap` 라고 한다. 스택에 데이터를 넣는 것은 allocating 한다고 하지 않는다. 포인터의 크기는 fixed size 이기 때문에 스택에 저장할 수 있지만, 실제 데이터를 가지고 싶다면 포인터를 따라가야 한다.

allocator 가 공간을 찾아서 배정, 정돈할 필요가 없기 때문에 stack 에 저장하는 것이 훨씬 빠르다. 마찬가지로 데이터에 접근할 때도, pointer 를 사용하는 힙보다 스택이 빠르다.

함수를 호출할 때, 함수에 넘겨준 값들(값의 위치를 가리키는 포인터 포함)과 함수의 로컬 변수들이 스택에 push 된다. 그리고 그 함수 실행이 끝나면, 그 값들은 스택에서 popped off 된다.

작성한 코드의 어떤 부분이 어떤 힙의 데이터를 사용하고 있는지 추적하고, 힙에서의 중복된 데이터를 최소화하고, 사용되지 않는 힙의 데이터를 청소하는 것이 **ownership** 이 해결하고 싶은 문제다. ownership 을 이해한다면, 그때부턴 스택과 힙에 대해서 덜 생각하며 코드를 짤 수 있지만, 이 '힙의 데이터를 관리하는 것' 이 ownership 의 존재이유라는 것을 기억하고 있으면, ownership 이 왜 그렇게 동작하는가도 이해할 수 있다.

## Ownership Rules

- Rust 의 각각의 값은 `owner` 라 불리는 변수를 가지고 있다.
- 한 번에 하나의 owner 만 존재할 수 있다.
- owner 가 스코프에서 벗어나면, 그 값은 폐기(dropped)된다.
