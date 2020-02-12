#!/usr/bin/node

const request = require('request');
var rp = require('request-promise');
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
    rp(characterUrl).then(response => {
      resolve(JSON.parse(response).name);
    });
  });
}
