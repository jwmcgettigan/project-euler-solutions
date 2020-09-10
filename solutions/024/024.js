/**
 * Project Euler - Problem Solution 024
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

function perm(digits) {
  // from https://stackoverflow.com/a/43260158/11342791
  let permutations = [];

  for (let i = 0; i < digits.length; i++) {
    let rest = perm(digits.slice(0, i).concat(digits.slice(i + 1)));

    if(!rest.length) {
      permutations.push([digits[i]])
    } else {
      for(let j = 0; j < rest.length; j++) {
        permutations.push([digits[i]].concat(rest[j]))
      }
    }
  }
  return permutations;
}

const millionthLexicographicPermutation = () => {
  perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).forEach((p, i) => {
    if(i === 999999) {
      console.log(Number(p.join('')))
    }
  })
}
console.log(millionthLexicographicPermutation());