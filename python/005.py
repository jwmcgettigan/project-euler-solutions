"""
Project Euler - Problem Solution 005
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def greatest_common_divisor(a, b):
  return a if not b else greatest_common_divisor(b, a % b)

def least_common_multiple(a, b):
  return a * b // greatest_common_divisor(a, b)

def smallest_multiple(divisors) -> int:
  multiple = divisors[0]
  for divisor in divisors:
    multiple = least_common_multiple(multiple, divisor)
  return multiple

if __name__ == "__main__":
	print(smallest_multiple(range(1,20)))