#!/usr/bin/node

let arg = process.argv[2];
arg = parseInt(arg);
if (Number.isInteger(arg)){
  console.log(arg);
}
else{
  console.log("Not a number");
}
