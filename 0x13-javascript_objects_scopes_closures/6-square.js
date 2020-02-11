#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
