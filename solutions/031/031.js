/**
 * Project Euler - Problem Solution 031
 * Problem Title - Coin sums
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const coinSums = () => {
  let combinations = 1 // from 1*200 = 200
  let b, c, d, e, f, g, h;
  for(b = 200; b >= 0; b -= 100) {
    for(c = b; c >= 0; c -= 50) {
      for(d = c; d >= 0; d -= 20) {
        for(e = d; e >= 0; e -= 10) {
          for(f = e; f >= 0; f -= 5) {
            for(g = f; g >= 0; g -= 2) {
              combinations++;
            }
          }
        }
      }
    }
  }
  return combinations;
};

console.log(coinSums());