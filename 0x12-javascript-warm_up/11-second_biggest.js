#!/usr/bin/node

const arr = process.argv
let frst = 0;
let scnd = 0;

for (i = 2; i < arr.length; i++) {
    if (frst < arr[i]) {
        scnd = frst;
        frst = parseInt(arr[i]);
    }
    else if (scnd < arr[i]) {
        scnd = parseInt(arr[i]);
    }
}
console.log(scnd);
