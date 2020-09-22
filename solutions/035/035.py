"""
Project Euler - Problem Solution 035
Problem Title - Circular primes
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def primes_below_n(n) -> set:
  ''' The set of primes below a limit n. '''
  composites = set()
  primes = set()
  for i in range(2, n+1):
    if i not in composites:
      primes.add(i)
      for j in range(i*i, n+1, i):
        composites.add(j)
  return primes

def rotated_digits(num) -> 'Generator[int]':
  ''' Generates every other digit rotation of a number. '''
  digits = str(num)
  for i in range(len(digits)-1):
    digits = digits[-1] + digits[:-1]
    yield int(digits)

def circular_primes(limit):
  ''' Finds the number of circular primes below a limit. '''
  total = 0
  primes = primes_below_n(limit)
  for prime in primes:
    cont = False
    if prime > 9:
      for num in rotated_digits(prime):
        if num not in primes: # if num is not a prime number
          cont = True
          break
    if cont: continue
    total += 1
  return total

if __name__ == "__main__":
  print(circular_primes(1000000))
