let generator;
const getDataOne = () => {
  setTimeout(() => {
    generator.next('dummy data one')
    // 
  }, 1000); 
}

const getDataTwo = () => {
  setTimeout(() => {
    generator.next('dummy data two');
  }, 2000);
}; 

function* main() {
  const dataOne = yield getDataOne();
  console.log('data one', dataOne)
  console.log(new Date() - start);
  const dataTwo = yield getDataTwo();
  console.log('data two', dataTwo)
  console.log(new Date - start)
}

const start = new Date()
generator = main()
generator.next()