[Generator 부터 Iterator 까지 잘 설명한 블로그](https://valuefactory.tistory.com/209)

# Iterator
Iterator는 next메서드를 가지고있는 객체이다. 이 메서드는 순차적으로 원소들을 탐색하며, next메서드의 호출시마다 새로운 객체를 반환한다. 반환되는 객체는 value 와(또는 = and/or) done 프로퍼티를 가지고 있으며, 탐색이 완료될 때 done프로퍼티의 값이 true가 된다. 대부분의 Iterator들은 탐색이 완료될때, value를 생략한다. —> return {done: true};

Iterable은 `Symbol.iterator라는 **메서드**`를 가지고있는 객체이다. 이 메서드가 Iterator를 반환한다.

Iterable/Iterator Example
피보나치 수열을 생성하는 코드를 작성하였다. fibonacci변수가 참조하고 있는 객체는 Iterable이다.

```js
const fibonacci = {
    [Symbol.iterator]() {
        let n1 = 0, n2 = 1, value;
        return {
            next() {
                value = n1;
                n1 = n2;
                n2 = value + n2;
                // [value, n1, n2] = [n1, n2, n1 + n2]

                if (value > 100) {
                    return {done: true};
                } else {
                    return {value};
                }
            }
        };
    }
};

for (const n of fibonacci) {
    console.log(n);
}
```

# Generators
Generator는 Iterable이면서 Iterator인 객체의 특별한 종류이다. 이 객체는 일시정지와 재시작 기능을 여러 반환 포인트들을 통해 사용할 수 있다. 이러한 반환 포인트들은 yield 키워드를 통해 구현할 수 있으며, 오직 generator 함수에서만 사용할 수 있다. next호출시마다 다음 yield의 expression이 반환된다.
yield value를 사용하면 한가지 값을 반환할 수 있고, yield* iterable을 사용하면 해당되는 Iterable의 값들을 순차적으로 반환시킬 수 있다.

Generator의 반복이 끝나는 시점은 3가지 경우인데, generator 함수에서 return 사용, 에러 발생 그리고 마지막으로 함수의 끝부분까지 모두 수행된 이후, 이렇게 3가지 경우이다. 그리고 이때 done 프로퍼티가 true가 될 것이다.