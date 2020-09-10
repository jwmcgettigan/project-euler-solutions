"""
Project Euler - Problem Solution 025
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def newTerms(f): return [f[1], f[0] + f[1]]
def index_of_1000_digit_fibonacci_value():
  # repurposed from problem 002
  index, f = 1, [1, 1]
  while(len(str(f[0])) < 1000):
    f = newTerms(f)
    index += 1
  return index

if __name__ == "__main__":
	print(index_of_1000_digit_fibonacci_value())