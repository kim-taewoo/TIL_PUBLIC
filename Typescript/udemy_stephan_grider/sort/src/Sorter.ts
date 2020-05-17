// Abstract Class 를 쓰게 되면 interface 가 필요없어짐.
// 서로에게 종속된 클래스라면 상속과 Abstract Class 를 사용하고, 서로 별개의 클래스라면 interface 를 쓰는 게 맞다.
// interface Sortable {
//   length: number;
//   compare(leftIndex: number, rightIndex: number): boolean;
//   swap(leftIndex: number, rightIndex: number): void;
// }

export abstract class Sorter {
  // constructor(public collection: Sortable) {}

  // sort(): void {
  //   const { length } = this.collection;

  //   for (let i = 0; i < length; i++) {
  //     for (let j = 0; j < length - i - 1; j++) {
  //       if (this.collection.compare(j, j + 1)) {
  //         this.collection.swap(j, j + 1);
  //       }
  //     }
  //   }
  // }

  // 무조건 상속해서 쓰이게 될 Sorter 라서 그냥 `this` 만 남기면
  // 일단 이 Sorter 클래스에 `length`, `compare`, `swap` 같은
  // 메서드가 존재하지 않기 때문에 에러가 발생한다.
  // 그래서 타입스크립트한테 제대로 알려주기 위해, 이 클래스를 `Abstract Class` 로 변환시켜 줘야 한다.
  // `Abstract Class` 는 직접적으로 instance 를 만들 수 없는 클래스로(new 사용 불가), 오직 상속만 하는 parent class 로만 존재할 수 있다.

  abstract compare(leftIndex: number, rightIndex: number): boolean;
  abstract swap(leftIndex: number, rightIndex: number): void;
  abstract length: number;

  sort(): void {
    const { length } = this;

    for (let i = 0; i < length; i++) {
      for (let j = 0; j < length - i - 1; j++) {
        if (this.compare(j, j + 1)) {
          this.swap(j, j + 1);
        }
      }
    }
  }
}
