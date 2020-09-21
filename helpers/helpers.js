

const range = (start, stop, step=1) => {
  var a = [start], b = start;
  while (b < stop) a.push(b += step);
  return a;
}

 /**
  * Returns the decimal representation of the fraction a / b in three parts:
  *   integer part, non-recurring fractional part, and recurring part.
  * @param {*} a - numerator
  * @param {*} b - denominator
  */
 const divide = (a, b) => {
  if(b == 0) { throw error; }
  const integer = Math.floor(a / b);
  let remainder = a % b;
  let seen = {remainder: 0};
  const digits = [];
  while(true) {
    remainder *= 10;
    digits.push(Math.floor(remainder / b));
    remainder %= b;
    if(remainder in seen) {
      const where = seen[remainder];
      return [integer, digits.splice(null, where), digits.splice(where)];
    } else {
      seen[remainder] = digits.length;
    }
  }
}

/** Finds the greatest common divisor. */
const gcd = (a, b) => {
  return !b ? a : gcd(b, a % b);
};

module.exports = {
  range,
  gcd
}