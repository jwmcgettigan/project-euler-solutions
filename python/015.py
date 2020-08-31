"""
Project Euler - Problem Solution 015
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def factorial(n):
  if n < 2: return 1
  else: return n * factorial(n-1)

def num_routes_for_n_dimension_grid(n):
  # (n + n)! / (n)!n!
  return int(factorial(n+n)/(factorial(n)**2))

if __name__ == "__main__":
  print(num_routes_for_n_dimension_grid(20))