/**
 * Project Euler - Problem Solution 036
 * Problem Title - Double-base palindromes
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Digits are the same forwards and backwards. */
const isPalindrome = (num) => {
  const digits = String(num).replace(/^0+/, ''); // remove leading zeros
  return digits == [...digits].reverse().join('');
};

/** Finds the sum of all numbers which are palindromic
 * in base 10 and base 2 below a limit. */
const doubleBasePalindromes = (limit) => {
  let total = 0;
  for(let i = 0; i < limit; i++) {
    if(isPalindrome(i) && isPalindrome(i.toString(2))) {
      total += i;
    }
  }
  return total;
};

console.log(doubleBasePalindromes(1000000));