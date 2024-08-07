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

  rotate () {
    this.width = this.width ^ this.height;
    this.height = this.width ^ this.height;
    this.width = this.width ^ this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
