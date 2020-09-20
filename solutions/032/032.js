/**
 * Project Euler - Problem Solution 032
 * Problem Title - Pandigital products
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

const set = (iterable) => new Set(iterable);

function equalSets(a, b) {
  if (a.size !== b.size) return false;
  for (const i of a) if (!b.has(i)) return false;
  return true;
}

const isPandigital = (identity) => (
  identity.length === 9 && equalSets(set(identity), set('123456789'))
);

const productIdentity = (multiplicand, multiplier) => {
  const product = multiplicand*multiplier;
  const identity = `${multiplicand}${multiplier}${product}`;
  return [product, identity];
}

const pandigitalProducts = () => {
  const products = set();
  for(let multiplicand = 0; multiplicand < 10; multiplicand++) {
    for(let multiplier = 1000; multiplier < 10000; multiplier++) {
      [product, identity] = productIdentity(multiplicand, multiplier);
      if(identity.length > 9) { break; }
      if(isPandigital(identity)) {
        products.add(product);
      }
    }
  }
  for(let multiplicand = 10; multiplicand < 100; multiplicand++) {
    for(let multiplier = 100; multiplier < 1000; multiplier++) {
      [product, identity] = productIdentity(multiplicand, multiplier);
      if(identity.length > 9) { break; }
      if(isPandigital(identity)) {
        products.add(product);
      }
    }
  }
  let sumOfProducts = 0;
  products.forEach((num) => { sumOfProducts += num; });
  return sumOfProducts;
};

console.log(pandigitalProducts());