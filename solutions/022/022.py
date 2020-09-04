"""
Project Euler - Problem Solution 022
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def name_scores(names):
  return names

if __name__ == "__main__":
  file = open('names.txt', 'r')
  names = file.read()
  print(name_scores(names))
  file.close()