#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
  process.exit();
}
for (let i = 0; i < num; i++){
  for (let i = 0; i < num; i++){
    process.stdout.write('X');
  }
  console.log();
}
