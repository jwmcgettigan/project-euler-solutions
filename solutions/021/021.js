/**
 * Project Euler - Problem Solution 021
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const d = (n) => {
  // reused from problem 012
  total = 1; // start at one since 1 is also a divisor
  for(let i = 2; i < n**0.5; i++) {
    if(n % i == 0) {
      if(n / i == i) { // If divisors are equal, add only one 
        total += i;
      } else { // Otherwise add both
        total += (i + n / i);
      }
    }
  }
  return total;
}

const amicableNumbers = (n) => {
  amicable_sum = 0;
  for(let a = 1; a < n; a++) {
    d_a = d(a);
    for(let b = a+1; b < n; b++) {
      if(d_a == b && d(b) == a) {
        amicable_sum += a + b;
      }
    }
  }
  return amicable_sum;
};

console.log(amicableNumbers(10000));