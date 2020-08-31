"""
Project Euler - Problem Solution 016
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def sum_digits(n):
  s = 0
  while n:
    s, n = s + n % 10, n // 10
  return s

def power_digit_sum(power):
  return sum_digits(2**power)

if __name__ == "__main__":
  print(power_digit_sum(1000))