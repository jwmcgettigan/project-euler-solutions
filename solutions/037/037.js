/**
 * Project Euler - Problem Solution 037
 * Problem Title - Truncatable primes
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Return the sum of all elements in an iterable of numbers. */
const sum = (iterable) => {
  let s = 0;
  iterable.forEach((num) => { s += num; });
  return s;
}

/** Generates every truncation of a number. */
function* truncatedNums(prime) {
  const digits = String(prime);
  for(let i = 1; i < digits.length; i++) {
    yield Number(digits.substring(i));
    yield Number(digits.substring(0, digits.length-i));
  }
};

/** Finds the sum of the only eleven primes that are
 * both truncatable from left to right and right to left. */
const truncatablePrimes = () => {
  let limit = 1000;
  const primes = new Set(), composites = new Set();
  const tPrimes = new Set(), not_tPrimes = new Set([2, 3, 5, 7]);

  while(tPrimes.size < 11) {
    limit *= 2;
    
    for(let i = 2; i < limit+1; i++) {
      if(!composites.has(i)) {
        primes.add(i);
        for(let j = i*i; j < limit+1; j += i) {
          composites.add(j);
        }
        // -------------------------------------
        let truncatable = true;
        for(let num of truncatedNums(i)) {
          if(!primes.has(num)) {
            truncatable = false;
            break;
          }
        }
        if(truncatable && !not_tPrimes.has(i)) {
          tPrimes.add(i);
        }
      }
    }
  }

  return sum(tPrimes);
};

console.log(truncatablePrimes());