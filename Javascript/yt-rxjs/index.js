import { from } from 'rxjs';
import { map, filter } from 'rxjs/operators';

const numbersObservable = from([1, 2, 3, 4, 5]);
const squaredNumbers = numbersObservable.pipe(
  filter((val) => val > 2),
  map((val) => val * val)
);

const subscription = squaredNumbers.subscribe((result) => {
  console.log(result);
  subscription.unsubscribe();
});

document.getElementById("app").innerHTML = `
  <h1>Hello Vanilla!</h1>
  <div>
    hello hello
  </div>
`