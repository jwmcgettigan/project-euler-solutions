"""
Project Euler - Problem Solution 030
Problem Title - Digit fifth powers
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

"""
Determining the upper bound:
find where: x(9^5) = an x digit number

x | number  | does x(9^5) = an x digit number?
----------------
1 | 59049   | X
2 | 118098  | X
3 | 177147  | X
4 | 236196  | X
5 | 295245  | X
6 | 354294  | ✓

thus, 354294 is our upper bound
"""

def fifth_power_sums(limit):
  total = 0
  num = 10
  while num < limit:
    digit_sum = 0
    for digit in str(num):
      digit_sum += int(digit)**5
    if digit_sum == num:
      total += num
    num += 1
  return total

if __name__ == "__main__":
	print(fifth_power_sums(354294))