"""
Project Euler - Problem Solution 010
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

# I essentially modified my answer to problem 007.
def sum_of_primes_below_n(n):
  sum_of_primes = 0
  composites = set()
  for i in range(2, n+1):
    if i not in composites:
      sum_of_primes += i
      for j in range(i*i, n+1, i):
        composites.add(j)
  return sum_of_primes

if __name__ == "__main__":
  print(sum_of_primes_below_n(2000000))