"""
Project Euler - Problem Solution 005
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def sum_of_squares(nums) -> int:
  return sum(map(lambda num: num ** 2, nums))

def square_of_sum(nums) -> int:
  return sum(nums) ** 2

def sum_square_difference(nums) -> int:
  return square_of_sum(nums) - sum_of_squares(nums)

if __name__ == "__main__":
	print(sum_square_difference(range(1, 101)))