const Dupe = Symbol('clone');

class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  [Dupe]() {
    return new this.constructor(this._brand, this._motor, this._color);
  }

  cloneCar() {
    return this[Dupe]();
  }
}

export default Car;
