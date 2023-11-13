#!/usr/bin/node

let arg1 = process.argv[2];
let arg2 = process.argv[3];
arg1 = parseInt(arg1);
arg2 = parseInt(arg2);

function add(a, b) {
  console.log(a + b);
}

add(arg1, arg2);
