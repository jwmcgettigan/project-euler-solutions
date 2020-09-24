/**
 * Project Euler - Problem Solution 038
 * Problem Title - Pandigital multiples
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Turns iterable into a Set(). */
const set = (iterable) => new Set(iterable);

/** Compares whether two sets contain the same elements. */
const equalSets = (a, b) => {
  if (a.size !== b.size) return false;
  for (const i of a) if (!b.has(i)) return false;
  return true;
}

/** Checks if a number contains all digits among 1-9. */
const isPandigital = (identity) => (
  identity.length === 9 && equalSets(set(identity), set('123456789'))
);

/** Return the concatentated product of an integer
 * with (1,2, ... , n) where n > 1. */
const concatenatedProduct = (num) => {
  let concat_product = '';
  let multiplier = 1;
  while(concat_product.length < 9) {
    concat_product += String(num*multiplier);
    multiplier++;
  }
  return concat_product;
};

/** Finds the largest 1 to 9 pandigital 9-digit number
 * that can be formed as a concatenated product. */
const pandigitalMultiples = () => {
  const pandigitals = new Set();
  for(let i = 0; i < 9876; i++) {
    const concat_product = concatenatedProduct(i);
    if(isPandigital(concat_product)) {
      pandigitals.add(Number(concat_product));
    }
  }
  return Math.max(...pandigitals);
};

console.log(pandigitalMultiples());