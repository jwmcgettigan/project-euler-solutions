

const range = (start, stop, step=1) => {
  var a = [start], b = start;
  while (b < stop) a.push(b += step);
  return a;
}

module.exports = {
  range
}