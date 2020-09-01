/**
 * Project Euler - Problem Solution 016
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const sumDigits = (n) => {
  let s = BigInt(0), base = BigInt(10);
  while(n > 0) {
    remainder = n % base
    s += remainder;
    n = (n - remainder) / base;
  }
  return Number(s);
};

const powerDigitSum = (power) => {
  return sumDigits(BigInt(2**power));
};

console.log(powerDigitSum(1000));