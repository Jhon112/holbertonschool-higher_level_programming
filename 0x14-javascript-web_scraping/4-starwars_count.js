#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let counter = 0;

    for (const fiml of results) {
      if (isOnFilm(fiml)) counter++;
    }

    console.log(counter);
  }
});

function isOnFilm (film) {
  const characters = film.characters;
  return characters.includes('https://swapi.co/api/people/18/');
}
