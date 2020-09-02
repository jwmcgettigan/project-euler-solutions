/**
 * Project Euler - Problem Solution 020
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const factorial = (n) => {
  // reused from problem 015 w/BigInt added
  if(n < 2) { return BigInt(1); }
  else { return BigInt(n) * factorial(n-1); }
};

const sumDigits = (n) => {
  // reused from problem 016
  let s = BigInt(0), base = BigInt(10);
  while(n > 0) {
    remainder = n % base;
    s += remainder;
    n = (n - remainder) / base;
  }
  return Number(s);
};

const factorialDigitSum = (n) => {
  return sumDigits(factorial(n));
};

console.log(factorialDigitSum(100));