/**
 * Project Euler - Problem Solution 004
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const isPalindrome = (product) => (
  String(product) === String(product).split('').reverse().join('')
);

const largestPalindromeOfProducts = (lower_limit, upper_limit) => {
  let products = [];
  for(let x = lower_limit; x < upper_limit ; x++) {
    for(let y = x; y < upper_limit; y++) {
      let product = x * y;
      if(isPalindrome(product)) {
        products.push(product);
      }
    }
  }
  return Math.max(...products)
}

console.log(largestPalindromeOfProducts(100, 1000));