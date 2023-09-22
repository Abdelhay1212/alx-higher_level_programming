#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    let char = '';
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }

    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += char;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
