"""
Project Euler - Problem Solution 039
Problem Title - Integer right triangles
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def pythagorean_triplet_solutions(p):
  ''' Finds the pythagorean triplets
  for the given perimeter (p). '''
  seen = set()
  for a in range(1, p // 3 + 1):
    for b in range(a + 1, p // 2 + 1):
      c = p - a - b
      if (a * a + b * b == c * c):
        if(a + b + c == p):
          seen.add((a, b, c))
  return seen

def integer_right_triangles(limit):
  ''' Finds the maximum number of
  solutions for perimeters under a limit. '''
  max_solutions = 0, 0
  for p in range(limit):
    solutions = len(pythagorean_triplet_solutions(p))
    if solutions > max_solutions[0]:
      max_solutions = solutions, p
  return max_solutions[1]

if __name__ == "__main__":
	print(integer_right_triangles(1000))