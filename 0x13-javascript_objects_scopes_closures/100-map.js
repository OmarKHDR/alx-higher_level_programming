#!/usr/bin/node

list = require('./100-data.js').list;

console.log(list);
console.log(list.map( (x, ind)=> x * ind));

