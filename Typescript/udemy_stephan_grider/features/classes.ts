class Vehicle {
  // drive(): void {
  //   console.log('부릉부릉');
  // }

  // color: string;

  constructor(public color: string) {
    // this.color = color;
  }

  protected honk(): void {
    console.log('빵빵');
  }
}

const vehicle = new Vehicle('orange');
console.log(vehicle.color);

class Car extends Vehicle {
  // color 은 부모 클래스에서 이미 public 을 부여받았으므로 덮어쓰지 않기 위해 새로 public 같은 키워드를 붙여주지 않는다.
  constructor(public wheels: number, color: string) {
    super(color);
  }

  private drive(): void {
    console.log('붕붕붕');
  }

  startDrivingProcess(): void {
    this.drive();
    this.honk();
  }
}

const car = new Car(4, 'red');
car.startDrivingProcess();
