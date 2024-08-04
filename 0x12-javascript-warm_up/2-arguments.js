#!/usr/bin/node

const myVar = process.argv.length;

switch (myVar) {
  case 2:
  console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
