#!/usr/bin/node

let arg1 = process.argv[2];
arg1 = parseInt(arg1);

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }
  if (number === 0) {
    return 1;
  }
  let result = number * (factorial(number - 1));
  return result;
}

console.log(factorial(arg1));
