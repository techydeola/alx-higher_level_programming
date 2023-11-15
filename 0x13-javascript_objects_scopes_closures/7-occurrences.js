#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listLen = list.length;
  let count = 0;

  for (let i = 0; i < listLen; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
};
