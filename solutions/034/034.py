"""
Project Euler - Problem Solution 034
Problem Title - Digit factorials
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def factorial(n) -> int:
  ''' The product of all positive integers less than or equal to n. '''
  if n < 2: return 1
  else: return n * factorial(n-1)

def digit_factorial_sum(factorials, n) -> int:
  ''' The sum of the factorial of each digit in n. '''
  s = 0
  while n:
    s += factorials[n % 10]
    n //= 10
  return s

def digit_factorials(limit) -> int:
  ''' The sum of all numbers which are equal to the
  sum of the factorial of their digits. '''
  total = 0
  factorials = [factorial(i) for i in range(10)] # pre-calculate 0-9
  num = 3
  while num < limit:
    if digit_factorial_sum(factorials, num) == num:
      total += num
    num += 1
  return total

if __name__ == "__main__":
	print(digit_factorials(2540160))