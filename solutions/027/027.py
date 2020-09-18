"""
Project Euler - Problem Solution 027
Problem Title - Quadratic primes
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#Currently takes ~9s

def is_prime(n): 
  return n > 1 and all(n % p for p in range(2, int(n**0.5)))

def quadratic_formula(n, a, b):
  return n**2 + a*n + b

def consecutive_primes(a, b):
  n = 0
  while True:
    num = quadratic_formula(n, a, b)
    if is_prime(num):
      n += 1
    else:
      break
  return n

def quadratic_primes():
  most_consecutive_primes = 0
  best_coefficients = (0, 0)
  for a in range(-999, 1000):
    for b in range(-1000, 1001):
      num_primes = consecutive_primes(a, b)
      if num_primes > most_consecutive_primes:
        most_consecutive_primes = num_primes
        best_coefficients = (a, b)
  return best_coefficients[0] * best_coefficients[1]

if __name__ == "__main__":
	print(quadratic_primes())