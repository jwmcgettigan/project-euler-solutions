/**
 * Project Euler - Problem Solution 041
 * Problem Title - Pandigital prime
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */
declare var require: any
const now = require('performance-now');

/** Finds the largest n-digit pandigital prime.
 * An n-digit number is pandigital if it makes
 * use of all the digits 1 to n exactly once.
 */
const template = (): number => {
  return 500;
}

const start: number = now();

const answer: number = template();

const end: number = now();
const duration: number = (end - start) / 1000; // Seconds

console.log(answer);
console.log(`\nTime taken: ${duration.toFixed(3)}s`);