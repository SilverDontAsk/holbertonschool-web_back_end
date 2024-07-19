export default class Building {
  constructor(sqft) {
    this._sqft = Building._validatesize(sqft);
  }

  static _validatesize(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Building must have a size');
    }
    return sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = Building._validatesize(value);
  }

  evacuationWarningMessage() {
    if (this) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
}
