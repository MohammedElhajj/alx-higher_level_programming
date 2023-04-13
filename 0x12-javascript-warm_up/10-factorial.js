#!/usr/bin/node
function factorial (n) {
  const number = parseInt(n);
  if (isNaN(number)) return 1;
  if (number === 0) return 1;
  return number * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
