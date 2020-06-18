"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
exports.__esModule = true;
function WithTax(rate) {
    return function (target, key, descriptor) {
        var original = descriptor.get;
        descriptor.get = function () {
            var result = original.apply(this);
            return (result * (1 + rate)).toFixed(2);
        };
        return descriptor;
    };
}
function Confirmable(message) {
    return function (target, key, descriptor) {
        // 원본 값은 original 에 저장
        var original = descriptor.value;
        // 원하는대로 메서드 수정(다만 화살표 함수여선 안 된다. this 를 쓸 일이 있어)
        descriptor.value = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            // 여기서는 단순히 confirm 메시지 참/거짓에 따라 실행 or 취소
            var allow = confirm(message);
            if (allow) {
                var result = original.apply(this, args);
                return result;
            }
            else {
                return null;
            }
        };
    };
}
var IceCreamComponent = /** @class */ (function () {
    function IceCreamComponent() {
        this.toppings = [];
    }
    IceCreamComponent.prototype.addToping = function (topping) {
        if (topping === void 0) { topping = 'sprinkles'; }
        this.toppings.push(topping);
    };
    Object.defineProperty(IceCreamComponent.prototype, "price", {
        get: function () {
            return 5.0 + 0.25 * this.toppings.length;
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Confirmable('Are you sure?')
    ], IceCreamComponent.prototype, "addToping");
    __decorate([
        WithTax(0.15)
    ], IceCreamComponent.prototype, "price");
    return IceCreamComponent;
}());
exports.IceCreamComponent = IceCreamComponent;
