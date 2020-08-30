"""
Project Euler - Problem Solution 014
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#! needs optimization; best takes ~36s

def collatz_sequence(sequence):
  # w/this, takes ~1m13s
  n = sequence[-1]
  if n == 1:
    return len(sequence)
  elif n % 2 == 0:
    sequence.append(n/2)
  else:
    sequence.append(3*n + 1)
  return collatz_sequence(sequence)

def collatz_sequence2(n, length=1):
  # w/this, takes ~1m2s
  if n == 1:
    return length
  elif n % 2 == 0:
    n = n/2
  else:
    n = 3*n + 1
  length += 1
  return collatz_sequence2(n, length)

def collatz_sequence3(n, length=1):
  # w/this, takes ~36s
  while n > 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    length += 1
  return length

def longest_collatz_sequence(n):
  longest_chain = 0, 0 # starting_number, length
  for i in range(1, n):
    chain_length = collatz_sequence3(i)
    if chain_length > longest_chain[1]:
      longest_chain = (i, chain_length)
  return longest_chain[0]

if __name__ == "__main__":
  print(longest_collatz_sequence(1000000))