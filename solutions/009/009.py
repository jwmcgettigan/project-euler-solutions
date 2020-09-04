"""
Project Euler - Problem Solution 009
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

# I need to better explain each part of this function.
# It's not very readable in it's current iteration.
def pythagorean_triplet_product(n):
  for i in range(1, n // 3 + 1):
    for j in range(i + 1, n // 2 + 1):
      k = n - i - j
      if (i * i + j * j == k * k):
        if(i + j + k == n):
          return i*j*k
  print('No Triplet Found for n: {}'.format(n))

if __name__ == "__main__":
  print(pythagorean_triplet_product(1000))