"""
Project Euler - Problem Solution 040
Problem Title - Champernowne's constant
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#TODO: Come back and make this more readable.

def fractional_part(nth):
  ''' Finds the nth digit of Champernowne's constant. '''
  summation, num_sum = 0, 0
  multiplier, series_num = 0, 0
  while summation < nth:
    multiplier += 1
    num_sum += series_num
    series_num = 9*(10**(multiplier-1))
    summand = series_num*multiplier
    summation += summand
  summation -= summand
  digits_in = nth-summation
  numbers_in = digits_in // multiplier
  chars_extra = digits_in % multiplier
  number = num_sum + numbers_in + (chars_extra != 0)
  return int(str(number)[chars_extra - (chars_extra != 0)])

def champernownes_constant():
  ''' Finds the product of the nth digits of Champernowne's constant. '''
  product = 1
  nth_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]

  for nth in nth_digits:
    product *= fractional_part(nth)
  
  return product

if __name__ == "__main__":
	print(champernownes_constant())
