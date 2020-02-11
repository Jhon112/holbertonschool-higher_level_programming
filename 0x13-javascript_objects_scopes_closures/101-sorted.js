#!/usr/bin/node

const dict = require('./101-data').dict;

const newObj = {};

for (const key in dict) {
  if (Object.hasOwnProperty.call(dict, key)) {
    const id = dict[key];
    newObj[id] = newObj[id] ? [...newObj[id]] : [];
    newObj[id].push(key);
  }
}

console.log(newObj);
