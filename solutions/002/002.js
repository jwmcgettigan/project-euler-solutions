/**
 * Project Euler - Problem Solution 002
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const isEven = (num) => num % 2 === 0;
const newTerms = (f) => [f[1], f[0] + f[1]];
const sumOfEvenFibonacciValues = (limit) => {
  let sum = 0, f = [1, 1];
  while(f[0] < limit) {
    if(isEven(f[0])) sum += f[0];
    f = newTerms(f);
  }
  return sum;
}

console.log(sumOfEvenFibonacciValues(4000000));