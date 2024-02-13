#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor (size) {
    super(size);
  }
  charPrint(c)
  {
    if (c === undefined)
    {
      super.print();
    }
    else
    {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
