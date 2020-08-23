/**
 * Project Euler - Problem Solution 010
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

// I essentially modified by answer to problem 007.
const sumOfPrimesBelowN = (n) => {
  let sumOfPrimes = 0;
  const composites = new Set();
  for(let i = 2; i < n+1; i++) {
    if(!composites.has(i)) {
      sumOfPrimes += i;
      for(let j = i*i; j < n+1; j += i) {
        composites.add(j);
      }
    }
  }
  return sumOfPrimes;
};

console.log(sumOfPrimesBelowN(2000000));