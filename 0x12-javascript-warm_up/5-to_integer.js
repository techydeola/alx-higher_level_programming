#!/usr/bin/node

let myArg = process.argv[2];
myArg = parseInt(myArg);

if (isNaN(myArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ', myArg);
}
