"""
Project Euler - Problem Solution 022
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def char_position(letter):
  return ord(letter.lower()) - 96

def name_scores(names):
  total = 0
  sorted_names = sorted(names.strip().replace('\"', '').split(','))
  for i, name in enumerate(sorted_names, 1):
    alpha_value = sum([char_position(letter) for letter in name])
    name_score = i * alpha_value
    total += name_score
  return total

if __name__ == "__main__":
  file = open('names.txt', 'r')
  names = file.read()
  print(name_scores(names))
  file.close()