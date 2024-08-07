#!/usr/bin/node

const square = require('./5-square');

class Square extends square {

  charPrint (c = 'X') {
    super.print(c);
  }
}

module.exports = Square;
