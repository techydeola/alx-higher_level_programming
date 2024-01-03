#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const movieData = JSON.parse(body);
  const data = movieData.results;
  let count = 0;

  for (const element of data) {
    for (const character of element.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
