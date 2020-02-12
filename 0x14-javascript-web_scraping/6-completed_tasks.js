#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const result = {};

  data.map(todo1 => {
    if (!result[todo1.userId]) {
      result[todo1.userId] = data.reduce((accomulator, todo) => {
        return todo1.userId === todo.userId && todo.completed === true
          ? accomulator + 1
          : accomulator;
      }, 0);
    }
  });
  console.log(result);
});
