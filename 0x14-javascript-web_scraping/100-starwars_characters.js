#!/usr/bin/node

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const request = require('request');

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  for (const character of characters) {
    request(character, function (error, response, body) {
      if (error) console.error('error:', error);
      const actorData = JSON.parse(body);
      console.log(actorData.name);
    });
  }
});
