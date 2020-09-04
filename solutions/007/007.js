/**
 * Project Euler - Problem Solution 007
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const getNthPrime = (nth) => {
  let limit = nth;
  const primes = new Set(), composites = new Set();
  let num_primes = 0;
  while(num_primes < nth) {
    limit *= 2;
    for(let i = 2; i < limit+1; i++) {
      if(!composites.has(i)) {
        if(!primes.has(i)) {
          primes.add(i);
          if(primes.size === nth) {
            return i;
          }
        }
        for(let j = i*i; j < limit+1; j += i) {
          composites.add(j);
        }
      }
    }
    num_primes = primes.size;
  }
};

console.log(getNthPrime(10001));