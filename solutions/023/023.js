/**
 * Project Euler - Problem Solution 023
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const sumOfDivisors = (n) => {
  // reused from problem 021
  if(n == 0) { return 0; }
  total = 1; // start at one since 1 is also a divisor
  for(let i = 2; i < Math.floor(n**0.5) + 1; i++) {
    if(n % i == 0) {
      if(n / i == i) { // If divisors are equal, add only one 
        total += i;
      } else { // Otherwise add both
        total += (i + n / i);
      }
    }
  }
  return total;
};

const isAbundant = (num) => {
  return sumOfDivisors(num) > num;
}

const nonAbundantSums = () => {
  let total = 0;
  let abundantNums = Array();
  let abundantSums = new Set();
  for(let i = 0; i < 28123 + 1; i++) {
    if(isAbundant(i)) {
      abundantNums.push(i);
    }
  }

  abundantNums.forEach(i => {
    abundantNums.forEach(j => {
      abundantSums.add(i + j);
    });
  });

  for(let i = 0; i < 28123 + 1; i++) {
    if(!abundantSums.has(i)) {
      total += i;
    }
  }

  return total;
};

console.log(nonAbundantSums());