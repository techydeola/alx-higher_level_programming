#!/usr/local/bin/node

const movieId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});
