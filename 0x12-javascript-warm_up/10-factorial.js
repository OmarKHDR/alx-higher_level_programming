#!/usr/bin/node

function fact(num) {
  num = parseInt(num);
  if (num == 1 || isNaN(num)) return 1;
  return num * fact(num - 1);
}

const arr = process.argv;
console.log(fact(arr[2]));
