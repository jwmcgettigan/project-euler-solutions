/**
 * Project Euler - Problem Solution 005
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */
const { range } = require('../../helpers/helpers');

const greatestCommonDivisor = (a, b) => {
  return !b ? a : greatestCommonDivisor(b, a % b);
};

const leastCommonMultiple = (a, b) => {
  return Math.floor((a * b) / greatestCommonDivisor(a, b));
};

const smallestMultiple = (divisors) => {
  let multiple = divisors[0];
  divisors.forEach(divisor => {
    multiple = leastCommonMultiple(multiple, divisor);
  });
  return multiple;
};

console.log(smallestMultiple(range(1, 20)));