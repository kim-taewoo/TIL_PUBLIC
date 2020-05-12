const add = (a: number, b: number): number => {
  return a + b;
};

const subtract = (a: number, b: number): number => {
  return a - b;
};

function divide(a: number, b: number): number {
  return a / b;
}

const multiply = function (a: number, b: number): number {
  return a * b;
};

const logger = (message: string): void => {
  console.log(message);
};

// never 같이 결코 함수의 끝에 다다를 수 없는 리턴 타입도 정의할 수 있다.
// 하지만 보통의 경우라면 이렇게까지 극단적인 함수는 잘 없다.
// 보통 다른 if 문이나(void 가 되겠지) default return 문이 있곤 하기 땜에..
const throwError = (message: string): never => {
  throw new Error(message);
};

const todaysWeather = {
  date: new Date(),
  weather: 'sunny',
};

const logWeather = (forecast: { date: Date; weather: string }): void => {
  console.log(forecast.date);
  console.log(forecast.weather);
};

// ES2015
const logWeather2015 = ({ date, weather }: { date: Date; weather: string }) => {
  console.log(date);
  console.log(weather);
};

logWeather2015(todaysWeather);
