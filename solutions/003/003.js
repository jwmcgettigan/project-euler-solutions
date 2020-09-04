/**
 * Project Euler - Problem Solution 003
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const isComposite = (num, p) => num >= (p*p);
const isPrime = (num, p) => num % p === 0;
const primeFactorization = (number) => {
  let p = 2;
  while(isComposite(number, p)) {
    if(isPrime(number, p)) {
      number = number / p;
    } else p += 1;
  }
  return number;
}

console.log(primeFactorization(600851475143));