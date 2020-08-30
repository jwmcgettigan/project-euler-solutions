/**
 * Project Euler - Problem Solution 014
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

// Takes ~1.5s; much faster than python's ~36s

const collatzSequence = (n, length=1) => {
  while(n > 1) {
    if(n % 2 == 0) {
      n /= 2;
    } else {
      n = 3*n + 1;
    }
    length++;
  }
  return length;
}

const longestCollatzSequence = (n) => {
  let longestChain = {
    startingNumber: 0,
    length: 0
  };
  for(let i = 1; i < n; i++) {
    const chainLength = collatzSequence(i);
    if(chainLength > longestChain.length) {
      longestChain = {
        startingNumber: i,
        length: chainLength
      };
    }
  }
  return longestChain.startingNumber;
};

console.log(longestCollatzSequence(1000000));