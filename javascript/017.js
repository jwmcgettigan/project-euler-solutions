/**
 * Project Euler - Problem Solution 017
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

numerals = {
  ones: {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'},
  tens: {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
}

const numberToNumeral = (num) => {
  if(num < 20) {
    return numerals.ones[num];
  } else if (num < 100) {
    return numerals.tens[Math.floor(num / 10)] + numerals.ones[num % 10];
  } else if (num < 1000) {
    return (numberToNumeral(Math.floor(num / 100)) + 'hundred'
          + (num % 100 ? 'and' : '')
          + numberToNumeral(num % 100));
  } else if (num === 1000) {
    return 'onethousand';
  }
};

const numerLetterCounts = (n) => {
  let s = 0;
  for(let i = 1; i < n+1; i++) {
    s += numberToNumeral(i).length
  }
  return s;
};

console.log(numerLetterCounts(1000));