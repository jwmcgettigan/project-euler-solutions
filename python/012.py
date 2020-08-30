"""
Project Euler - Problem Solution 012
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#TODO: Needs optimization
#! javascript code runs much faster, why is that?
#! I suspect the problem lies in python's for loops.

def isComposite(num, p): return num >= (p*p)
def isPrime(num, p): return num % p == 0
def primeFactorization(number):
  # Reusing methods from problem 003.
  primes = []
  p = 2
  while(isComposite(number, p)):
    if(isPrime(number, p)):
      number = number / p;
      primes.append(number);
    else: p += 1
  return primes
  
def factors2(n):
  #! WIP
  primes = primeFactorization(n)
  total = 1
  for p in range(2, len(primes)):
    count = 0
    if(isPrime(n, p)):
      while(isPrime(n, p)):
        n = n // p
        count += 1
      total *= count + 1
  return total

def factors3(n):
  cnt = 0
  for i in range(1, (int)(n**0.5) + 1):
    if(n % i == 0):  
      if(n / i == i): # If divisors are equal, count only one 
        cnt += 1
      else: # Otherwise count both 
        cnt += 2
  return cnt 


def factors(n):
  # Slow method of finding number of factors
  return len(set(
    factor for i in range(1, int(n**0.5) + 1) if n % i == 0
    for factor in (i, n//i)
  ))

def triangle_number(n):
  return (n)*(n + 1) / 2

def triangle_num_with_over_n_divisors(n):
  term, divisors, i = 0, 0, 0
  while divisors <= n:
    term = triangle_number(i)
    divisors = factors3(term)
    i += 1
  return term

if __name__ == "__main__":
  #print(factors(500))
  #print(factors2(50))
  #print(factors3(500))
  print(triangle_num_with_over_n_divisors(500))