/**
 * Project Euler - Problem Solution 012
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

// NOTE TO SELF:
// While this code takes ~0.6s to complete with n=500,
// the python equivalent takes 10x at ~6.2s.

const factors = (n) => {
  let cnt = 0;
  for(let i = 1; i < Math.floor(n**0.5) + 1; i++) {
    if(n % i == 0) {  
      if(n / i == i) { // If divisors are equal, count only one 
        cnt += 1;
      } else { // Otherwise count both 
        cnt += 2;
      }
    }
  }
  return cnt;
};

const triangleNumber = (n) => {
  return (n)*(n + 1) / 2;
};

const triangleNumWithOverNDivisors = (n) => {
  let term = 0, divisors = 0, i = 0;
  while(divisors <= n) {
    term = triangleNumber(i);
    divisors = factors(term);
    i++;
  }
  return term;
};

console.log(triangleNumWithOverNDivisors(500));