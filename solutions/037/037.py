"""
Project Euler - Problem Solution 037
Problem Title - Truncatable primes
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def truncated_nums(prime):
  ''' Generates every truncation of a number. '''
  digits = str(prime)
  for i in range(1, len(digits)):
    yield int(digits[i:])
    yield int(digits[:-i])

def truncatable_primes():
  ''' Finds the sum of the only eleven primes that are
  both truncatable from left to right and right to left. '''
  limit = 1000
  primes, composites = set(), set()
  t_primes = set()
  not_t_primes = {2, 3, 5, 7}

  while len(t_primes) < 11:
    limit *= 2
    for i in range(2, limit+1):
      if i not in composites:
        primes.add(i)
        for j in range(i*i, limit+1, i):
          composites.add(j)
        # ------------------------------------
        truncatable = True
        for num in truncated_nums(i):
          if num not in primes:
            truncatable = False
            break
        if truncatable and i not in not_t_primes:
          t_primes.add(i)
  
  return sum(t_primes)

if __name__ == "__main__":
	print(truncatable_primes())