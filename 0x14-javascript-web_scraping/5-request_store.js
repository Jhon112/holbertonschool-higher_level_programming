#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (err, response, body) => {
  if (!err) {
    fs.writeFile(fileName, body, { encoding: 'utf-8' }, (err, data) => {
      if (err) console.log(err);
    });
  }
});
