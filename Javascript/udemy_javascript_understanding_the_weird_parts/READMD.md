# Conceptual aside

## Syntax parsers

A program that readsd your code and determines what it does and if its grammar is valid.

## Lexical environments

Where something sits physically in the code you write. (프로그램을 어디에 쓰냐가 중요하다.)

## Execution context

A wrapper to help manage the code that is running.

  ### Execution Context(Global)

  자바스크립트 코드가 실행되면 **자바스크립트 엔진이 다음 3개를 만들어준다.** Global Object 와 `this` 그리고 Outer Environment. 웹브라우저 환경이라면 `window` 가 글로벌 object 이고 nodejs 환경이라면 `process` 겠지. 그리고 글로벌 환경에서는 global object === `this` 다.

  자바스크립트에서 Global 이란, "Not inside a Function" 라는 뜻이다. 즉, 어떤 함수에 들어가지있지 않은 변수나 함수는 Global object 에 직접적으로 정의된다.

  ### Hoisting 
  작성한 코드가 실제로 위쪽으로 움직이는 게 아니다. Execution context 가 만들어질 때(Creation Phase), 작성되어 있는 코드를 한 번 점검하며 변수와 함수들을 위한 메모리 공간을 setup 하는 게 Hoisting 이다. 그런데 함수는 통째로 메모리 공간을 할당받지만, 변수는 자바스크립트 엔진이 한줄한줄 읽어 내려가면서 이 값이 **변하지 않을 것이라는 확신이 없다.** 그래서 함수처럼 완벽히 fix 된 값을 메모리에 setup 하지 못하고 placeholder 로 `undefined` 를 배정해둔다.  
  > 참고로 아예 선언을 안 한 경우 에러가 발생하므로 undefined 조차 되지 않음에 주의하자. hoisting 은 선언은 되어야 메모리 배정을 한다. 

  Execution context 의 creation phase 다음 **code execution phase** 가 있다.  
  
  - Synchronous: One at a time in order
  - 

  코드가 실행되면, 우선 Global Execution Context 가 생기고, 코드가 진행된다. 그리고 함수 호출을 만날 때마다 새로운 Execution conetext 가 execution stack 에 추가된다. 

## Obejct

A collection of name-value pairs


## Scope
Where a variable is available in your code, and if it's truly the same variable, or a new copy.

