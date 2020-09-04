/**
 * Project Euler - Problem Solution 015
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const factorial = (n) => {
  if(n < 2) { return 1; }
  else { return n * factorial(n-1); }
};

const numRoutesForNDimensionGrid = (n) => {
  // (n + n)! / (n)!n!
  return factorial(n+n)/(factorial(n)**2);
};

console.log(numRoutesForNDimensionGrid(20));