"""
Project Euler - Problem Solution 029
Problem Title - Distinct powers
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def distinct_powers(limit):
  distinct_terms = set()
  for a in range(2, limit+1):
    for b in range(2, limit+1):
      distinct_terms.add(a**b)
  return len(distinct_terms)

if __name__ == "__main__":
	print(distinct_powers(100))