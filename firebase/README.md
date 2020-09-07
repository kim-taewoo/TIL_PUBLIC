## firestore 구조 크기 단위

collection -> document -> data



## firestore reference

```js
// collection ref
export const carsCollection = db.collection('cars');
// document ref. collection ref 뒤에 `.doc(원하는 id)` 를 넣어 접근 가능하다.
export const siteRef = db.doc('site/business')
```



## Looping firestore collection

```js
export const firebaseLooper = (snapshot) => {
  // 아래 코드는 파이어베이스가 자체 제공하는 forEach 를 사용해서 `docs` 부분을 생략할 수도 있다.
  // 즉, snapshot.forEach((doc) => ({id: doc.id, ...doc.data()}))
  // 여기서 forEach 는 자바스크립트에서 제공하는 기본 forEach 가 아님을 알아야 한다!
  const data = snapshot.docs.map((doc)=> ({id: doc.id, ...doc.data()}))
  return data;
};
```



### where

```js
  getAlltheCars() {
    carsCollection
      .where('color', '==', 'red')
      .get()
      .then((snapshot) => {
        const cars = firebaseLooper(snapshot);
        this.setState({ cars });
      })
      .catch((e) => console.error(e));
  }
```



### orderBy

```js
.orderBy('price', 'asc')
.orderBy('price', 'desc')
```



## add 대신 set

`collection.add({})` 대신 `collection.doc().set({})` 을 사용할 수 있다. set 이 add 와 다른 점은, 

1. 반드시 `doc()` 이 앞에 있어야 한다는 점
2. `doc(아이디 지정)` doc 괄호 안에 본인이 원하는 id 를 넣을 수 있고, 또 아무것도 __넣지 않을 때__에만 `add` 처럼 자동으로 아이디가 생성된다는 점이다. 



## 객체와 배열의 업데이트

파이어베이스에서 객체의 추가, 삭제 등은 어렵지 않다. 그냥 원하는 필드에 접근해 (문자열로 접근이 가능하다. 예를 들어 `.update({ "dealers.california": false }))` 처럼 property 접근을 그냥 문자열로 한다.) 원하는 속성의 값을 변경한 뒤 update 하면 된다.

그러나 배열의 경우에는 좀 어렵다. 인덱스로 접근해서 변경하는 것이 불가능하기 때문에 전체 내용을 받아 한꺼번에 변경한 후 한꺼번에 업데이트 해야 한다. 이게 싫다면 `firebase.firestore.FieldValue.arrayUnion()` 같은 파이어베이스가 제공하는 배열 추가 메서드를 사용하는 식의 방법을 써야 한다. 게다가 파이어베이스의 배열에서 중복된 값은 같은 것으로 취급되어 버린다.. 즉 배열 안에 똑같은 것이 있을 수 없다. 수동으로 같은 값을 넣었다고 해도, 둘 중 하나를 지우면 둘다 사라져 버린다. 



## limit, limit to last, start and end at

`.limitToLast(2)` 는 뒤에서부터 개수 제한으로 가져온다.

`.startAt(200)` 은 `.orderBy`() 된 속성이 200 이상인 값을 가진 것을,

`.endAt(300)` 은 `.orderBy()` 된 속성이 300 이하인 값을 가져온다. 

'이상', '이하' 대신 '초과', '미만' 을 하고 싶다면 `startAfter` 나 `endBefore` 같은 메서드를 사용할 수도 있다.



## 존재 확인

`snapshot.exists` 속성 값을 통해서 값의 존재 여부를 알수도 있지만, `OnSnapshot` 을 쓰는 게 더 많은 걸 할 수 있다. 이건 실시간으로 값을 체크할 수 있다. 

즉, 값이 변경될 때마다 변경된 값을 알려준다. 업데이트 함수가 실행되었더라도, 현재 값과 다르지 않다면 알려주지 않는, 아주 효율적인 메서드다.

`.onSnapshot` 은 collection 을 대상으로 할 수도 있고 하나의 doc을 대상으로 할 수도 있다. 만약 collection 을 대상으로 사용했다면 해당 collection 이 가진 모든 doc 에 대한 정보를 받는데, 각각의 doc 의 상태를 `type` 속성값을 통해 감지할 수 있다. 기본 값은 `added` 이며, `modified` 와 `removed` 같은 것으로 상태 변경을 파악할 수 있다. 

`.onSnapshot` 으로 구독하고 있는 것을 구독 취소하기 위해서는, 구독할 때의 메서드를 변수에 저장했다가, 구독취소를 하고 싶을 때 그 변수를 실행시키면 된다. 즉 subscribe 메서드의 반환값은 unsubscribe 메서드다.