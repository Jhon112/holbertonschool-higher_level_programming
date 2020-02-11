#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c) {
      let index = 0;
      while (index < this.height) {
        let str = '';
        for (let row = 0; row < this.width; row++) {
          str += c;
        }
        console.log(str);
        index++;
      }
    } else {
      super.print();
    }
  }
};
