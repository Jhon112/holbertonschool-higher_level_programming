#!/usr/bin/node

const request = require('request');
const url = `http://swapi.co/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body);

    const promises = [];
    for (const characterUrl of results.characters) {
      promises.push(getName(characterUrl));
    }
    Promise.all(promises).then(names => {
      for (const name of names) {
        console.log(name);
      }
    });
  }
});

function getName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) throw error;
      resolve(JSON.parse(body).name);
    });
  });
}
