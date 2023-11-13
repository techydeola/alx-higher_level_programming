#!/usr/local/bin/node

const argLen = process.argv.length - 1;

if (argLen <= 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
