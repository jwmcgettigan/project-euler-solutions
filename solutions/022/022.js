/**
 * Project Euler - Problem Solution 022
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const alphabet = [...'abcdefghijklmnopqrstuvwxyz']
const charPosition = (letter) => {
  return alphabet.indexOf(letter.toLowerCase()) + 1;
};

const nameScores = (names) => {
  let total = 0
  const sorted_names = (names.trim().replace(/"/g, '').split(',')).sort()
  for(let i = 0; i < sorted_names.length; i++) {
    const name = [...sorted_names[i]]
    let alpha_value = 0
    name.forEach(letter => { alpha_value += charPosition(letter) });
    const name_score = (i + 1) * alpha_value
    total += name_score
  }
  return total
};

const fs = require('fs');
names = fs.readFileSync('names.txt', 'utf8');
console.log(nameScores(names));