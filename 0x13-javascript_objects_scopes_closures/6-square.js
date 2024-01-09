#!/usr/bin/node
const SquareA = require('./5-square.js');
module.exports = class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(s);
      }
    }
  }
};
