/**
 * Project Euler - Problem Solution 030
 * Problem Title - Digit fifth powers
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const fifthPowerSums = (limit) => {
  let total = 0;
  let num = 10;
  while(num < limit) {
    let digit_sum = 0;
    String(num).split('').forEach(digit => {
      digit_sum += Number(digit)**5;
    })
    if(digit_sum === num) {
      total += num;
    }
    num++;
  }
  return total;
}

console.log(fifthPowerSums(354294));