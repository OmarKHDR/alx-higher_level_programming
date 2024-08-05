#!/usr/bin/node

const arg = process.argv[2];
if (arg.isInteger())
{
    console.log(parseInt(arg));
}
else
{
    console.log("Not a number");
}
