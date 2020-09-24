"""
Project Euler - Problem Solution 009
Problem Title - Special Pythagorean triplet
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def pythagorean_triplet_product(p):
  ''' Finds the product of a pythagorean
  triplet for the given perimeter (p). '''
  for a in range(1, p // 3 + 1):
    for b in range(a + 1, p // 2 + 1):
      c = p - a - b
      if (a * a + b * b == c * c):
        if(a + b + c == p):
          return a*b*c

if __name__ == "__main__":
  print(pythagorean_triplet_product(1000))