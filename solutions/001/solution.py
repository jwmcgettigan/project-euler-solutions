def multiple_of(num, multiple):
  return num % multiple == 0

def sum_of_multiples(limit):
  return sum(x for x in range(limit) if multiple_of(x, 3) or multiple_of(x, 5))

if __name__ == "__main__":
	print(sum_of_multiples(1000))