/**
 * Project Euler - Problem Solution 033
 * Problem Title - Digit cancelling fractions
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Turns iterable into a Set(). */
const set = (iterable) => new Set(iterable);

/** Creates a Set that contains elements that both Sets a and b contain.  */
const intersection = (a, b) => set([...a].filter(x => b.has(x)));

/** Gets the first element in a Set. */
const pop = (a) => a.values().next().value;

/** Finds the greatest common divisor. */
const gcd = (a, b) => {
  return !b ? a : gcd(b, a % b);
};

/** Removes the common digit from n and d. */
const cancelDigits = (n, d) => {
  const commonDigit = pop(intersection(set(String(n)), set(String(d))));
  const canceled_n = Number(String(n).replace(commonDigit, ''));
  const canceled_d = Number(String(d).replace(commonDigit, ''));
  return [canceled_n, canceled_d];
};

/** Finds the reduced denominator of the product of
 * non-trivial digit-cancelling fractions. */
const digitCancellingFractions = () => {
  let product = [1, 1];
  for(let n = 10; n < 100; n++) {
    for(let d = n + 1; d < 100; d++) { // n / d must be less than 1 in value
      if(intersection(set(String(n)), set(String(d))).size !== 1) {
        continue; // n and d must have 1 common digit
      }

      [cn, cd] = cancelDigits(n, d);
      if(cn === (n / 10) && cd === (d / 10)) {
        continue; // must be non-trivial
      }
      if(cd !== 0 && (cn / cd) === (n / d)) {
        product = [product[0]*cn, product[1]*cd];
      }
    }
  }
  return product[1] / gcd(...product); // the reduced denominator
};

console.log(digitCancellingFractions());