/**
 * Project Euler - Problem Solution 026
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

// the key is long-division

 /**
  * Returns the recurring part of the decimal
  * representation of the fraction 1 / d.
  * @param {*} a - numerator
  * @param {*} b - denominator
  */
const recurringCycleLength = (d) => {
  if(d == 0) { throw error; }
  let remainder = 1 % d;
  let seen = {remainder: 0}; // Holds position where each remainder was first seen.
  const digits = [];
  while(true) { // Loop executed at most b times (as remainders must be distinct)
    remainder *= 10;
    digits.push(Math.floor(remainder / d));
    remainder %= d;
    if(remainder in seen) { // Digits have begun to recur.
      const where = seen[remainder];
      return digits.splice(where).length;
    } else {
      seen[remainder] = digits.length;
    }
  }
}

const longestRecurringCycle = (limit) => {
  let longestCycle = [0, 0];
  for(let d = 1; d < limit; d++) {
    const cycle_len = recurringCycleLength(d);
    if(cycle_len > longestCycle[0]) {
      longestCycle = [cycle_len, d];
    }
  }
  return longestCycle[1];
}

console.log(longestRecurringCycle(1000));