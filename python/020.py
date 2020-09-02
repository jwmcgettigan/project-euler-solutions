"""
Project Euler - Problem Solution 020
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def factorial(n):
  # reused from problem 015
  if n < 2: return 1
  else: return n * factorial(n-1)

def sum_digits(n):
  # reused from problem 016
  s = 0
  while n:
    s, n = s + n % 10, n // 10
  return s

def factorial_digit_sum(n):
  return sum_digits(factorial(n))
  

if __name__ == "__main__":
  print(factorial_digit_sum(100))