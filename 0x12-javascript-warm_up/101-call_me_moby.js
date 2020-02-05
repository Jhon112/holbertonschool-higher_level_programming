#!/usr/bin/node
module.exports = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
