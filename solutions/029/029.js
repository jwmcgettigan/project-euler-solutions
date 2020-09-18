/**
 * Project Euler - Problem Solution 029
 * Problem Title - Distinct powers
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const distinctPowers = (limit) => {
  const distinctTerms = new Set();
  for(let a = 2; a < limit+1; a++) {
    for(let b = 2; b < limit+1; b++) {
      distinctTerms.add(a**b);
    }
  }
  return distinctTerms.size;
}
console.log(distinctPowers(100));