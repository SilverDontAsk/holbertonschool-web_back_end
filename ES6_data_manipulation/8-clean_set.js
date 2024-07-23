function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const res = [];
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      res.push(value.slice(startString.length));
    }
  }
  return res.join('-');
}

export default cleanSet;
