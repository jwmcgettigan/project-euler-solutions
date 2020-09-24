/**
 * Project Euler - Problem Solution 039
 * Problem Title - Integer right triangles
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Finds the pythagorean triplets
 * for the given perimeter (p). */
const pythagoreanTripletSolutions = (p) => {
  const seen = new Set();
  for(let a = 1; a < Math.floor(p / 3) + 1; a++) {
    for(let b = a+1; b < Math.floor(p / 2) + 1; b++) {
      c = p - a - b;
      if (a * a + b * b == c * c) {
        if(a + b + c == p) {
          seen.add([a, b, c]);
        }
      }
    }
  }
  return seen;
};

/** Finds the maximum number of
 * solutions for perimeters under a limit. */
const integerRightTriangles = (limit) => {
  let maxSolutions = [0, 0];
  for(let p = 0; p < limit; p++) {
    const solutions = pythagoreanTripletSolutions(p).size;
    if(solutions > maxSolutions[0]) {
      maxSolutions = [solutions, p];
    }
  }
  return maxSolutions[1];
};

console.log(integerRightTriangles(1000));