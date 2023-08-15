#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let s = '';
    let h;
    if (c === undefined) { h = 'X'; } else { h = c; }
    for (let i = 0; i < this.width; i++) { s += h; }
    for (let i = 0; i < this.height; i++) { console.log(s); }
  }
}
module.exports = Square;
