const add = (a, b) => a + b;
const generateGreeting = (name = 'Anonymous') => `Hello ${name}!`;

test('should add two numbers', () => {
  const result = add(3, 4);

  if (result !== 7) {
    throw new Error('You added 4 and 3. The result was ${result}. Expected 7');
  }
})

test('Should generate greeting from name', () => {
  const result = generateGreeting('태우');
  expect(result).toBe('Hello 태우!');
});

test('Should generate greeting without args', () => {
  const result = generateGreeting();
  expect(result).toBe('Hello Anonymous!');
});