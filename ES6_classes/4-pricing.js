import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = Pricing._validateamount(amount);
    this._currency = Pricing._validatecurrency(currency);
  }

  static _validateamount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a number');
    }
    return amount;
  }

  static _validatecurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('currency must be a currency');
    }
    return currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(value) {
    this._amount = Pricing._validateamount(value);
  }

  set currency(value) {
    this._currency = Pricing._validatecurrency(value);
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversion rate must be numbers');
    }
    return amount * conversionRate;
  }
}
