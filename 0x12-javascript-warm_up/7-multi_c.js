#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number) {
  const string = 'C is fun';
  let i = 0;
  while (i < number) {
    console.log(string);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
