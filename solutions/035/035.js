/**
 * Project Euler - Problem Solution 035
 * Problem Title - Circular primes
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** The set of primes below a limit n. */
const primesBelow_n = (n) => {
  const composites = new Set();
  const primes = new Set();
  for(let i = 2; i < n+1; i++) {
    if(!composites.has(i)) {
      primes.add(i);
      for(let j = i*i; j < n+1; j += i) {
        composites.add(j);
      }
    }
  }
  return primes;
};

/** Generates every other digit rotation of a number. */
function* rotatedDigits(num) {
  let digits = String(num);
  let d_len = digits.length-1;
  for(let i = 0; i < d_len; i++) {
    digits = digits[d_len] + digits.substring(0, d_len);
    yield Number(digits);
  }
};

/** Finds the number of circular primes below a limit. */
const circularPrimes = (limit) => {
  let total = 0;
  const primes = primesBelow_n(limit);
  for(let prime of primes) {
    let cont = false;
    if(prime > 9) {
      for(let num of rotatedDigits(prime)) {
        if(!primes.has(num)) { // if num is not a prime number
          cont = true;
          break;
        }
      }
    }
    if(cont) { continue; }
    total++;
  }
  return total;
};

console.log(circularPrimes(1000000));