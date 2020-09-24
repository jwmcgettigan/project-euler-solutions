"""
Project Euler - Problem Solution 038
Problem Title - Pandigital multiples
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_pandigital(identity):
  ''' Checks if a number contains all digits among 1-9. '''
  return len(identity) == 9 and set(identity) == set('123456789')

def concatenated_product(num):
  ''' Return the concatentated product of an integer
  with (1,2, ... , n) where n > 1. '''
  concat_product = ''
  multiplier = 1
  while len(concat_product) < 9:
    concat_product += str(num*multiplier)
    multiplier += 1
  return concat_product

def pandigital_multiples():
  ''' Finds the largest 1 to 9 pandigital 9-digit number
  that can be formed as a concatenated product. '''
  pandigitals = set()
  for i in range(9876):
    concat_product = concatenated_product(i)
    if is_pandigital(concat_product):
      pandigitals.add(int(concat_product))
  return max(pandigitals)

if __name__ == "__main__":
	print(pandigital_multiples())