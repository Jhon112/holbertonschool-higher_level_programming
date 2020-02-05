#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 1 || !number) {
    return (1);
  }
  const fact = number * factorial(number - 1);
  return fact;
}

const res = factorial(number);
console.log(res);
