/**
 * Project Euler - Problem Solution 034
 * Problem Title - Digit factorials
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** The product of all positive integers less than or equal to n. */
const factorial = (n) => {
  if(n < 2) { return 1; }
  else { return n * factorial(n-1); }
};

/** The sum of the factorial of each digit in n. */
const digitFactorialSum = (factorials, n) => {
  let s = 0;
  while(n > 0) {
    remainder = n % 10;
    s += factorials[remainder];
    n = (n - remainder) / 10;
  }
  return s;
};

/** The sum of all numbers which are equal to the
 * sum of the factorial of their digits. */
const digitFactorials = (limit) => {
  let total = 0;
  const factorials = '0123456789'.split('').map(i => factorial(i));
  let num = 3;
  while(num < limit) {
    if(digitFactorialSum(factorials, num) === num) {
      total += num;
    }
    num++;
  }
  return total;
};

console.log(digitFactorials(2540160));