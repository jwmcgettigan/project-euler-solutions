"""
Project Euler - Problem Solution 026
Problem Title - Reciprocal cycles
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

"""
the key is long-division
#TODO: create a step-by-step visualization of how 
       to derive the recurring part of the fraction through long division
"""

def recurring_cycle_len(d):
  '''Returns the recurring part of the decimal
  representation of the fraction 1 / d.'''
  assert d > 0
  remainder = 1 % d
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // d)
    remainder %= d
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return len(digits[where:])
    else:
      seen[remainder] = len(digits)

def longest_recurring_cycle(limit):
  longest_cycle = (0, 0)
  for d in range(1, limit):
    cycle_len = recurring_cycle_len(d)
    if cycle_len > longest_cycle[0]:
      longest_cycle = (cycle_len, d)
  return longest_cycle[1]

if __name__ == "__main__":
	print(longest_recurring_cycle(1000))