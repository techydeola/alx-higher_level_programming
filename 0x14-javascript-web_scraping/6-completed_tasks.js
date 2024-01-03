#!/usr/local/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);

  const myDict = {};
  for (let i = 1; i < 11; i++) {
    let count = 0;
    for (const element of data) {
      if (element.userId === i && element.completed === true) {
        count += 1;
      }
    }
    myDict[String(i)] = count;
  }
  console.log(myDict);
});
