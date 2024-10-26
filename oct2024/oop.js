class Person {
  constructor(name) {
    this.name = name;
  }
  greet(name) {
    return `Hello ${name}, my name is ${this.name}`;
  }
}

class Cuboid {
  constructor(length, width, height) {
    this.length = length;
    this.width = width;
    this.height = height;
  }

  get surfaceArea() {
    return (
      2 *
      (this.length * this.width +
        this.width * this.height +
        this.height * this.length)
    );
  }

  get volume() {
    return this.length * this.width * this.height;
  }
}
class Cube extends Cuboid {
  // Don't forget to make a call to super ;)
  constructor(length) {
    super(length, length, length);
  }
}
