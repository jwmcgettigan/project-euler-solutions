"""
Project Euler - Problem Solution 033
Problem Title - Digit cancelling fractions
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def gcd(a, b) -> int:
  ''' Finds the greatest common divisor. '''
  while b:
    a, b = b, a % b
  return a

def cancel_digits(n, d) -> tuple:
  ''' Removes the common digit from n and d. '''
  common_digit = str(set(str(n)).intersection(set(str(d))).pop())
  canceled_n = int(str(n).replace(common_digit, '', 1))
  canceled_d = int(str(d).replace(common_digit, '', 1))
  return canceled_n, canceled_d

def digit_cancelling_fractions() -> int:
  ''' Finds the reduced denominator of the product of
  non-trivial digit-cancelling fractions. '''
  product = (1, 1)
  for n in range(10, 100):
    for d in range(n + 1, 100): # n / d must be less than 1 in value
      if len(set(str(n)).intersection(set(str(d)))) != 1:
        continue # n and d must have 1 common digit
      
      cn, cd = cancel_digits(n, d)
      if (cn, cd) == (n / 10, d / 10): continue # must be non-trivial
      if cd != 0 and (cn / cd) == (n / d):
        product = (product[0]*cn, product[1]*cd)
        #print("%d/%d is simplified to %d/%d" % (n, d, cn, cd))
  return product[1] // gcd(*product) # the reduced denominator

if __name__ == "__main__":
  print(digit_cancelling_fractions())