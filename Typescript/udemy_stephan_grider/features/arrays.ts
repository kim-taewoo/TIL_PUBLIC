const carMakers: string[] = ['ford', 'toyata', 'chevy'];
const dates: Date[] = [new Date(), new Date()];

// string 타입의 일차원배열의 string 이란 뜻으로 앞부터 읽으면 된다.
const carsByMake: string[][] = [];

// Help with inference when extracting values
const car1 = carMakers[0];
const myCar = carMakers.pop();

// Prevent incompatible values
carMakers.push(100);

// Help with 'map'
carMakers.map((car: string): string => {
  return car.toUpperCase();
});

// Multiple Types in an array
// Flexible types
const importantDates: (Date | string)[] = [new Date(), '2030-10-10'];
importantDates.push('2030-10-10');
importantDates.push(new Date());
