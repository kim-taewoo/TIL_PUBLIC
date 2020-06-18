function WithTax(rate: number) {
  return function (target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.get;

    descriptor.get = function () {
      const result = original.apply(this);
      return (result * (1 + rate)).toFixed(2);
    };
    return descriptor;
  };
}

function Confirmable(message: string) {
  return function (
    target: Object,
    key: string | Symbol,
    descriptor: PropertyDescriptor
  ) {
    // 원본 값은 original 에 저장
    const original = descriptor.value;
    // 원하는대로 메서드 수정(다만 화살표 함수여선 안 된다. this 를 쓸 일이 있어)
    descriptor.value = function (...args: any[]) {
      // 여기서는 단순히 confirm 메시지 참/거짓에 따라 실행 or 취소
      const allow = confirm(message);
      if (allow) {
        const result = original.apply(this, args);
        return result;
      } else {
        return null;
      }
    };
  };
}

export class IceCreamComponent {
  toppings = [];

  @Confirmable('Are you sure?')
  addToping(topping='sprinkles') {
    this.toppings.push(topping);
  }

  @WithTax(0.15)
  get price() {
    return 5.0 + 0.25 * this.toppings.length;
  }
}
