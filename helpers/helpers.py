

# https://stackoverflow.com/questions/249372/how-to-calculate-recurring-digits
def divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder %= b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)

def gcd_of_pair(a, b) -> int:
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a*b)//gcd_of_pair(a,b)

def gcd_of_list(l) -> int:
  gcd = l[0]
  for i in range(1, len(l)):
    gcd = gcd_of_pair(gcd, l[i])
  return gcd

  def cf(a, b) -> list:
  n=[]
  g=gcd(a, b)
  for i in range(1, g+1): 
    if g%i==0: 
      n.append(i)
  return n

def simplify_fraction(n, d):
  common_divisor = gcd(n, d)
  reduced_n, reduced_d = (n / common_divisor, d / common_divisor)
  return reduced_n, reduced_d

def simplify_fraction2(n, d):
  reduced_fractions = []
  common_divisors = cf(n, d)
  for common_divisor in common_divisors:
    reduced_fractions.append( (n / common_divisor, d / common_divisor) )
  return reduced_fractions

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__