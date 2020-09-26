/**
 * Project Euler - Problem Solution 040
 * Problem Title - Champernowne's constant
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

/** Finds the nth digit of Champernowne's constant. */
const fractionalPart = (nth) => {
  let summation = 0, numSum = 0;
  let multiplier = 0, seriesNum = 0;
  while(summation < nth) {
    multiplier++;
    numSum += seriesNum;
    seriesNum = 9*(10**(multiplier-1));
    summand = seriesNum*multiplier;
    summation += summand;
  }
  summation -= summand;
  const digitsIn = nth-summation;
  const numbersIn = Math.round(digitsIn / multiplier);
  const charsExtra = digitsIn % multiplier;
  const number = numSum + numbersIn + (charsExtra != 0);
  return Number(String(number).charAt(charsExtra - (charsExtra != 0)));
};

/** Finds the product of the nth digits of Champernowne's constant. */
const champernownesConstant = () => {
  let product = 1;
  const nthDigits = [1, 10, 100, 1000, 10000, 100000, 1000000];

  nthDigits.forEach(nth => {
    product *= fractionalPart(nth);
  })

  return product;
};

console.log(champernownesConstant());