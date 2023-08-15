#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
      if (c === undefined) {this.print()}
      else {
        let s = ''
        for(let i = 0; i < this.width; i++)
          s += c;
        for(let i = 0; i < this.height; i++)
          console.log(s);
    }
  }
}
module.exports = Square;
