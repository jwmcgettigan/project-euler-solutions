"""
Project Euler - Problem Solution 001
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def multipleOf(num, multiple):
  return num % multiple == 0

def sumOfMultiples(limit):
  return sum(x for x in range(limit) if multipleOf(x, 3) or multipleOf(x, 5))

if __name__ == "__main__":
	print(sumOfMultiples(1000))