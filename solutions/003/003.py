"""
Project Euler - Problem Solution 003
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

def isComposite(num, p): return num >= (p*p)
def isPrime(num, p): return num % p == 0
def primeFactorization(number):
  p = 2
  while(isComposite(number, p)):
    if(isPrime(number, p)):
      number = number / p;
    else: p += 1
  return number

if __name__ == "__main__":
	print(primeFactorization(600851475143))