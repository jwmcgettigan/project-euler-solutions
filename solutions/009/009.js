/**
 * Project Euler - Problem Solution 009
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

// I need to better explain each part of this function.
// It's not very readable in it's current iteration.
const pythagoreanTripletProduct = (n) => {
  for(let i = 1; i < Math.floor(n / 3) + 1; i++) {
    for(let j = i+1; j < Math.floor(n / 2) + 1; j++) {
      k = n - i - j;
      if (i * i + j * j == k * k) {
        if(i + j + k == n) {
          return i*j*k;
        }
      }
    }
  }
  console.log(`No Triplet Found for n: ${n}`);
};

console.log(pythagoreanTripletProduct(1000));