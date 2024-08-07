#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = `${'X'.repeat(this.width) + '\n'}`.repeat(this.height);
    str = str.slice(0, -1);
    console.log(str);
  }
}

module.exports = Rectangle;
