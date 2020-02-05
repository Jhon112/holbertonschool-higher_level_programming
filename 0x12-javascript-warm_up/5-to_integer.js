#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number) {
  console.log(number);
} else {
  console.log('Not a number');
}
