/**
 * Project Euler - Problem Solution 028
 * Problem Title - Number spiral diagonals
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const spiralSum = (width) => {
  let total = 1;
  let cornerValue = 1;
  let increment = 2;

  const radius = (width - 1) / 2;
  for(let i = 0; i < radius; i++) {
    for(let corner = 0; corner < 4; corner++) {
      cornerValue += increment;
      total += cornerValue;
    }
    increment += 2;
  }
  return total;
}

console.log(spiralSum(1001));