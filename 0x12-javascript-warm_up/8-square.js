#!/usr/bin/node

let myArg = process.argv[2];
myArg = parseInt(myArg);

if (isNaN(myArg)) {
  console.log('Missing size');
} else {
  const myString = 'X';
  const stringRepeat = myString.repeat(myArg);
  for (let i = 0; i < myArg; i++) {
    console.log(stringRepeat);
  }
}
