"""
Project Euler - Problem Solution 036
Problem Title - Double-base palindromes
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_palindrome(num):
  ''' Digits are the same forwards and backwards. '''
  digits = str(num).lstrip('0') # remove leading zeros
  return digits == digits[-1::-1]

def double_base_palindromes(limit):
  ''' Finds the sum of all numbers which are palindromic
  in base 10 and base 2 below a limit. '''
  total = 0
  for i in range(limit):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
      total += i
  return total

if __name__ == "__main__":
	print(double_base_palindromes(1000000))