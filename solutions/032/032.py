"""
Project Euler - Problem Solution 032
Problem Title - Pandigital products
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_pandigital(identity):
  return len(identity) == 9 and set(identity) == set('123456789')

def product_identity(multiplicand, multiplier):
  product = multiplicand*multiplier
  identity = '{}{}{}'.format(multiplicand, multiplier, product)
  return product, identity

def pandigital_products():
  products = set()

  for multiplicand in range(10):
    for multiplier in range(1000, 10000):
      product, identity = product_identity(multiplicand, multiplier)
      if len(identity) > 9: break
      if is_pandigital(identity):
        products.add(product)
  
  for multiplicand in range(10, 100):
    for multiplier in range(100, 1000):
      product, identity = product_identity(multiplicand, multiplier)
      if len(identity) > 9: break
      if is_pandigital(identity):
        products.add(product)
  
  return sum(products)

if __name__ == "__main__":
  print(pandigital_products())