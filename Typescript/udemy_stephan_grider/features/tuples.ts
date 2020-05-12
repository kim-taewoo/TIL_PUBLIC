const drink = {
  color: 'brown',
  carbonated: true,
  sugar: 40,
};

// 각 인덱스에 들어가는 타입순서를 강제하고 싶을 때
// tuple 을 쓴다.

// 아래처럼 일반 배열을 쓰면 인덱스마다의 타입이 강제되지 않아서 차후 수정될 우려가 있다.
const pepsi = ['brown', true, 40];

const pepsiTuple: [string, boolean, number] = ['brown', true, 40];

// 위처럼 튜플을 쓸 때마다 대괄호 안에 일일이 타입을 적어주기 힘들다면, 따로 type 을 정의해놓고 불러다 쓰는 게 좋다.

type Drink = [string, boolean, number];

const coke: Drink = ['brown', true, 40];
const sprite: Drink = ['clear', true, 40];
const tea: Drink = ['brown', false, 0];

// 근데 튜플이 사실 썩 실용도가 있지는 않다는 의견도 많다. 데이터에 대해 명확히 표현하고 싶었다면 차라리 object 형태로 쓰는 게 낫지.. 나중에 뭐 csv 데이터 읽을 때는 쓸모가 있다고는 한다.
