#!/usr/bin/node
const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(number1, number2);
