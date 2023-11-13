#!/usr/bin/node

let biggest = 0;
let secondBiggest = 0;
const myArray = process.argv;
const arrayLen = myArray.length;

if (arrayLen === 2) {
  console.log(0);
  process.exit(0);
} else if (arrayLen === 3) {
  console.log(0);
  process.exit(0);
}

for (let i = 2; i < arrayLen; i++) {
  const temp = parseInt(myArray[i]);
  if (temp > biggest) {
    secondBiggest = biggest;
    biggest = temp;
  }
}

console.log(secondBiggest);
