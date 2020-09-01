/**
 * Project Euler - Problem Solution 018
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

let triangle = `
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
`.trim().split('\n');
triangle = triangle.map(row => row.split(' ').map(num => +num));

const adjacentNums = (row, i) => {
  return [triangle[row+1][i], triangle[row+1][i+1]];
};

const maxAdjacentPathSum = (num, adjacentNums) => {
  let adjacentPathSums = [];
  adjacentNums.forEach(adjacentNum => {
    adjacentPathSums.push(num + adjacentNum);
  })
  return Math.max(...adjacentPathSums);
};

const maxPathSum = () => {
  let row = triangle.length - 2;
  while(row >= 0) {
    for(let i = 0; i < triangle[row].length; i++) {
      triangle[row][i] = maxAdjacentPathSum(triangle[row][i], adjacentNums(row, i));
    }
    row--;
  }
  return triangle[0][0];
};

console.log(maxPathSum());