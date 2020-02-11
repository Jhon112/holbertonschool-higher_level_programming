#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let index = 0;
    while (index < this.height) {
      let str = "";
      for (let row = 0; row < this.width; row++) {
        str += "X";
      }
      console.log(str);
      index++;
    }
  }

  rotate() {
    this.width = this.height + this.width;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
};
