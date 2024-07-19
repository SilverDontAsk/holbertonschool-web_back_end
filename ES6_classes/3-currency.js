export default class Currency {
  constructor(code, name) {
    this._code = Currency._validatecode(code);
    this._name = Currency._validatename(name);
  }

  static _validatecode(code) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    return code;
  }

  static _validatename(name) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    return name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(value) {
    this._code = Currency._validatecode(value);
  }

  set name(value) {
    this._name = Currency._validatename(value);
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
