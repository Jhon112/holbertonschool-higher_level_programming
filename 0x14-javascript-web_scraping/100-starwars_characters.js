#!/usr/bin/node

const request = require('request');
const url = `http://swapi.co/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body);

    for (const characterUrl of results.characters) {
      request(characterUrl, (errorCharacters, responseCharactersCharacters, bodyCharacters) => {
        if (
          !errorCharacters &&
          responseCharactersCharacters.statusCode === 200
        ) {
          console.log(JSON.parse(bodyCharacters).name);
        }
      });
    }
  }
});
