"""
Project Euler - Problem Solution 041
Problem Title - Pandigital prime
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_pandigital(identity):
  ''' Checks if a number contains all digits 1-n exactly once. '''
  return len(identity) == max(str(identity)) and set(identity) == set([str(i) for i in range(1, len(identity)+1)])

def pandigital_prime(limit):
  '''  '''
  pan_primes, composites = set(), set()

  for i in range(2, limit+1):
    if i not in composites:
      for j in range(i*i, limit+1, i):
        composites.add(j)
      # ------------------------------------
      if is_pandigital(str(i)):
        pan_primes.add(i)

  return max(pan_primes)

def is_prime(num):
  if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
      if (num % i) == 0:
        print(num, "is not a prime number")
        break
      else:
        print(num, "is a prime number")
  else:
    print(num, "is not a prime number")

def pandigital_prime2(limit):
  c = 0
  for i in range(limit):
    c += 1
  return c

if __name__ == "__main__":
  print(is_pandigital(str(9999991)))
  print(pandigital_prime2(1000000000))
