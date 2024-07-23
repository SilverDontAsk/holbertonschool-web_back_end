function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position out of range');
  }

  view.setInt8(position, value);

  return buffer;
}
// idk
export default createInt8TypedArray;
