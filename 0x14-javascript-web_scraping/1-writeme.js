#!/usr/bin/node

const fs = require('fs');

const data = process.argv[3];
fs.writeFileSync(process.argv[2], data, 'utf8');
