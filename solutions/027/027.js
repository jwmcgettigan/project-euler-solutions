/**
 * Project Euler - Problem Solution 027
 * Problem Title - Quadratic primes
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

//Currently takes ~0.28s

const isPrime = (n) => {
  for(let i = 2; i <= n**0.5; i++)
    if(n % i === 0) return false; 
  return n > 1;
};

const quadraticFormula = (n, a, b) => {
  return n**2 + a*n + b;
};

const consecutivePrimes = (a, b) => {
  let n = 0;
  while(true) {
    const num = quadraticFormula(n, a, b);
    if(isPrime(num)) {
      n++;
    } else {
      break;
    }
  }
  return n;
};

const quadraticPrimes = () => {
  let mostConsecutivePrimes = 0;
  let bestCoefficients = [0, 0];
  for(let a = -999; a < 1000; a++) {
    for(let b = -1000; b < 1001; b++) {
      const numPrimes = consecutivePrimes(a, b);
      if(numPrimes > mostConsecutivePrimes) {
        mostConsecutivePrimes = numPrimes;
        bestCoefficients = [a, b];
      }
    }
  }
  return bestCoefficients[0] * bestCoefficients[1];
};

console.log(quadraticPrimes());