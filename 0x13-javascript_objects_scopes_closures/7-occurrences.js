#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let considences = 0;

  list.map(ele => ele === searchElement ? considences++ : ele);

  return considences;
}