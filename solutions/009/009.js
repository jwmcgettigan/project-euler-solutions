/**
 * Project Euler - Problem Solution 009
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Finds the product of a pythagorean
 * triplet for the given perimeter (p). */
const pythagoreanTripletProduct = (p) => {
  for(let a = 1; a < Math.floor(p / 3) + 1; a++) {
    for(let b = a+1; b < Math.floor(p / 2) + 1; b++) {
      k = p - i - b;
      if (a * a + b * b == k * k) {
        if(a + b + k == p) {
          return a*b*k;
        }
      }
    }
  }
};

console.log(pythagoreanTripletProduct(1000));