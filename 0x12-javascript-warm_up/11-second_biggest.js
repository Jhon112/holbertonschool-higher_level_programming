#!/usr/bin/node
if (process.argv.length > 3) {
  process.argv.splice(0, 2);
  const max = Math.max(...process.argv);
  const data = process.argv.filter(ele => ele !== max.toString());
  console.log(Math.max(...data));
} else {
  console.log(0);
}
