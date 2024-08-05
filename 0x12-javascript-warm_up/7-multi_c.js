#!/usr/bin/node

const num = process.argv[2];
if (num === undefined) {
  console.log('Missing number of occurrences');
  process.exit();
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
