"""
Project Euler - Problem Solution 021
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#TODO: Make more readable; add more comments

# sum of proper divisors
# look into Sieve of Atkin

# --- Divisor function ---
# The sum of proper divisors of n (numbers less than n which divide evenly into n).
def d(n):
  # reused from problem 012
  total = 1 # start at one since 1 is also a divisor
  for i in range(2, int(n**0.5)):
    if(n % i == 0):

      if(n / i == i): # If divisors are equal, add only one 
        total += i
      else: # Otherwise add both
        total += (i + n // i);
  return total

def d2(n):
  total = 1 # start at one since 1 is also a divisor
  for i in range(2, int(n**0.5)):
    if n % i == 0:
      total += sum([d for d in (i, n//i)])
  return total

def amicable_numbers(n):
  amicable_sum = 0
  for a in range(1, n):
    d_a = d(a)
    for b in range(a+1, n):
      if d_a == b and d(b) == a:
        amicable_sum += a + b
  return amicable_sum
  

if __name__ == "__main__":
  print(amicable_numbers(10000))