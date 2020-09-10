/**
 * Project Euler - Problem Solution 025
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const newTerms = (f) => [f[1], f[0] + f[1]];
const indexOf1000DigitFibonacciValue = () => {
  // repurposed from problem 002
  let index = 1, f = [BigInt(1), BigInt(1)];
  while(f[0].toString().length < 1000) {
    f = newTerms(f);
    index++;
  }
  return index;
};

console.log(indexOf1000DigitFibonacciValue());