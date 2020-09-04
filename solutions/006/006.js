/**
 * Project Euler - Problem Solution 006
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */
const { range } = require('../../helpers/helpers');

const sum = (nums) => nums.reduce((a, b) => a + b);

const sumOfSquares = (nums) => {
  return sum(nums.map(num => num*num));
};

const squareOfSum = (nums) => {
  return Math.pow(sum(nums), 2);
};

const sumSquareDifference = (nums) => {
  return squareOfSum(nums) - sumOfSquares(nums);
};

console.log(sumSquareDifference(range(1, 100)));