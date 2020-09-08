"""
Project Euler - Problem Solution 023
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def sum_of_divisors(n):
  # reused from problem 021
  if n == 0: return 0
  total = 1 # start at one since 1 is also a divisor
  for i in range(2, int(n**0.5)+1):
    if(n % i == 0):
      if(n / i == i): # If divisors are equal, add only one
        total += i
      else: # Otherwise add both
        total += (i + n // i)
  return total

def is_abundant(num):
  return sum_of_divisors(num) > num

def non_abundant_sums():
  total, limit = 0, 28123
  abundant_nums = list()
  abundant_sums = set()
  for i in range(limit + 1):
    if is_abundant(i):
      abundant_nums.append(i)
  
  for i in abundant_nums:
    for j in abundant_nums:
      abundant_sum = i + j
      if abundant_sum > limit:
        break
      abundant_sums.add(i + j)

  for i in range(limit + 1):
    if i not in abundant_sums:
      total += i

  return total
  

if __name__ == "__main__":
  print(non_abundant_sums())