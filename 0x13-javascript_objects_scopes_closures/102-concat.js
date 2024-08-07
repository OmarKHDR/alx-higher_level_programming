#!/usr/bin/node
const fs =require('fs')
concat = function (source1, source2, dist) {
  const txt1 = fs.readFileSync(source1);
  const txt2 = fs.readFileSync(source2);
  fs.writeFileSync(dist, txt1 + txt2)
}

args = process.argv;
concat(args[2], args[3], args[4]);
