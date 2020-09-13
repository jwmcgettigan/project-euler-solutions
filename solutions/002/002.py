"""
Project Euler - Problem Solution 002
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_even(num): return num % 2 == 0
def new_terms(f): return [f[1], f[0] + f[1]]
def sum_of_even_fibonacci_values(limit):
  sum, f = 0, [1, 1]
  while(f[0] < limit):
    if(is_even(f[0])): sum += f[0]
    f = new_terms(f)
  return sum


if __name__ == "__main__":
	print(sum_of_even_fibonacci_values(4000000))