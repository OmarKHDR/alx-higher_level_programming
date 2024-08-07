#!/usr/bin/node

exports.esrever = function (list) {
  let count = 0;
  let arr = [];
  const len = list.length;
  while (count < len) {
    count = arr.push(list[-1 + -1 * count + len]);
  }
  return arr;
}
