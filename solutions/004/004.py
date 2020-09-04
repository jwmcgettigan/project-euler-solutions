"""
Project Euler - Problem Solution 004
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_palindrome(product) -> bool:
  return str(product) == str(product)[::-1]

def largest_palindrome_of_products(lower_limit, upper_limit) -> int:
  products = []
  for x in range(lower_limit, upper_limit):
    for y in range(x, upper_limit):
      product = x * y
      if(is_palindrome(product)):
        products.append(product)
  return max(products)

if __name__ == "__main__":
	print(largest_palindrome_of_products(100, 1000))