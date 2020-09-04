"""
Project Euler - Problem Solution 007
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def get_nth_prime(nth):
  limit = nth
  primes, composites = set(), set()
  num_primes = 0
  while(num_primes < nth):
    limit *= 2 # increase the limit if there are less than nth primes
    for i in range(2, limit+1):
      if i not in composites:
        if i not in primes:
          primes.add(i)
          if(len(primes) == nth):
            return i
        for j in range(i*i, limit+1, i):
          composites.add(j)
    num_primes = len(primes)

if __name__ == "__main__":
  print(get_nth_prime(10001))