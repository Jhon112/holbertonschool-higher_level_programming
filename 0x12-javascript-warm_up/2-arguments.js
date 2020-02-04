#!/usr/bin/node
if (process.argv.length > 2) {
  process.argv.length > 3
    ? console.log('Arguments found')
    : console.log('Argument found');
} else {
  console.log('No argument');
}
