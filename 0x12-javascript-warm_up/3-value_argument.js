#!/usr/bin/node

let arr = process.argv;

if (arr[2] === undefined)
{
    console.log("No argument");
}
else
{
    console.log(arr[2]);
}