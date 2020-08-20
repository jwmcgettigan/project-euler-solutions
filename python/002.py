"""
Project Euler - Problem Solution 002
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def isEven(num): return num % 2 == 0
def newTerms(f): return [f[1], f[0] + f[1]]
def sumOfEvenFibonacciValues(limit):
  sum, f = 0, [1, 1]
  while(f[0] < limit):
    if(isEven(f[0])): sum += f[0]
    f = newTerms(f)
  return sum


if __name__ == "__main__":
	print(sumOfEvenFibonacciValues(4000000))