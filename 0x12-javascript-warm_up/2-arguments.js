#!/usr/bin/node

const argLen = process.argv.length - 1;

if (argLen <= 1) {
  console.log('No argument');
} else if (argLen === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
