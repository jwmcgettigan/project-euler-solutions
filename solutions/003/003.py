"""
Project Euler - Problem Solution 003
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def is_composite(num, p): return num >= (p*p)
def is_prime(num, p): return num % p == 0
def prime_factorization(number):
  p = 2
  while(is_composite(number, p)):
    if(is_prime(number, p)):
      number = number / p;
    else: p += 1
  return number

if __name__ == "__main__":
	print(prime_factorization(600851475143))