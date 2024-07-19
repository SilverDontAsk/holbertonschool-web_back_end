export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = HolbertonCourse._validatename(name);
    this._length = HolbertonCourse._validatelength(length);
    this._students = HolbertonCourse._validatestudents(students);
  }

  static _validatename(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    return name;
  }

  static _validatelength(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    return length;
  }

  static _validatestudents(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array');
    }
    return students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(value) {
    this._name = HolbertonCourse._validatename(value);
  }

  set length(value) {
    this._length = HolbertonCourse._validatelength(value);
  }

  set students(value) {
    this._students = HolbertonCourse._validatestudents(value);
  }
}
