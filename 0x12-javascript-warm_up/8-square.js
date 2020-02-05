#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number && number > 0) {
  let height = 0;

  while (height < number) {
    let str = '';
    for (let width = 0; width < number; width++) {
      str += 'X';
    }
    console.log(str);
    height++;
  }
} else {
  console.log('Missing size');
}
