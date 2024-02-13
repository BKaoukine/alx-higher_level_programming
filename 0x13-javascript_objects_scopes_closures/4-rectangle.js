#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rex = '';
      for (let j = 0; j < this.width; j++) {
        rex += 'X';
      }
      console.log(rex);
    }
  }

  rotate () {
    const tmph = this.height;
    this.height = this.width;
    this.width = tmph;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
