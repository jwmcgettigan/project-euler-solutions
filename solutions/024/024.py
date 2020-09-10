"""
Project Euler - Problem Solution 024
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#TODO: Create my own easy-to-understand permutations function

def permutations(iterable, r=None):
  # from https://docs.python.org/2/library/itertools.html#itertools.permutations
  # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
  # permutations(range(3)) --> 012 021 102 120 201 210
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = list(range(n))
  cycles = list(range(n, n-r, -1))
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return

def perm(digits):
  # from https://stackoverflow.com/a/43260158/11342791
  permutations = []

  for i in range(len(digits)):
    rest = perm(digits[0:i] + digits[i+1:])
    
    if(not len(rest)):
      permutations.append([digits[i]])
    else:
      for j in range(len(rest)):
        permutations.append([digits[i]] + rest[j])
  
  return permutations


def millionth_lexicographic_permutation(digits):
  #for i, p in enumerate(sorted(permutation(digits))):
  for i, p in enumerate(perm(digits)):
    if i == 999999:
      return int(''.join(str(n) for n in p))

if __name__ == "__main__":
	print(millionth_lexicographic_permutation(list(range(10))))