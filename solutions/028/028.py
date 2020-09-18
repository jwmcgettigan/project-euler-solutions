"""
Project Euler - Problem Solution 028
Problem Title - Number spiral diagonals
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def spiral_sum(width):
  total = 1
  corner_value = 1
  increment = 2

  radius = (width - 1) // 2
  for i in range(radius):
    for corner in range(4):
      corner_value += increment
      total += corner_value
    increment += 2
  return total

if __name__ == "__main__":
	print(spiral_sum(1001))