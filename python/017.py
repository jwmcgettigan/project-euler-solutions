"""
Project Euler - Problem Solution 017
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

from helpers import *

numerals = {
  'ones': {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'},
  'tens': {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
}

def number_to_numeral(num):
  if num < 20:
    return numerals['ones'][num]
  elif num < 100:
    return numerals['tens'][num // 10] + numerals['ones'][num % 10]
  elif num < 1000:
    return (number_to_numeral(num // 100) + 'hundred'
          + ('and' if num % 100 else '')
          + number_to_numeral(num % 100))
  elif num == 1000:
    return 'onethousand'

def number_letter_counts(n):
  s = 0
  for i in range(1, n+1):
    s += len(number_to_numeral(i))
  return s

if __name__ == "__main__":
  print(number_letter_counts(1000))