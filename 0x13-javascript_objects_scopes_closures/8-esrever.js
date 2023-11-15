#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const listLen = list.length - 1;

  for (let i = listLen; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
