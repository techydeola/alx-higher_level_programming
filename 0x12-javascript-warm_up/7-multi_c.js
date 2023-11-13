#!/usr/bin/node

let myArg = process.argv[2];
const myString = 'C is fun';
myArg = parseInt(myArg);

if (isNaN(myArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArg; i++) {
    console.log(myString);
  }
}
