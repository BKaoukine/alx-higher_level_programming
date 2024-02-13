#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += 'C';
        }
        console.log(str);
      }
    }
  }
}

module.exports = Square;
