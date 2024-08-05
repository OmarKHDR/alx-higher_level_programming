#!/usr/bin/node

function add(a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}
const arr = process.argv;
console.log(add(arr[2], arr[3]));
