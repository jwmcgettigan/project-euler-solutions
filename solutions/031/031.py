"""
Project Euler - Problem Solution 031
Problem Title - Coin sums
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def coin_sums():
  combinations = 1 # from 1*200 = 200
  b, c, d, e, f, g, h = [None for _ in range(7)]
  for b in range(200, -1, -100):
    for c in range(b, -1, -50):
      for d in range(c, -1, -20):
        for e in range(d, -1, -10):
          for f in range(e, -1, -5):
            for g in range(f, -1, -2):
              combinations += 1
  return combinations

if __name__ == "__main__":
	print(coin_sums())


""" 
This method worked in ~5s in JavaScript but took WAY too
long in Python so I knew that I was approaching the solution
incorrectly and decided to think in reverse.  I realized
that I could start with the maximum amount of each currency
and increment downward to count only relevant combinations.

# a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h*1
def coin_sum(a, b, c, d, e, f, g, h):
  return a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h*1

def coin_sums():
  combinations = 0
  for a in range(2):
    for b in range(3):
      for c in range(5):
        for d in range(11):
          for e in range(21):
            for f in range(41):
              for g in range(101):
                for h in range(201):
                  if coin_sum(a, b, c, d, e, f, g, h) == 200:
                    combinations += 1
  return combinations """