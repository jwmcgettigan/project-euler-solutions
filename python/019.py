"""
Project Euler - Problem Solution 019
Copyright (c) Justin McGettigan. All rights reserved.
https://github.com/jwmcgettigan/project-euler-solutions
"""

#TODO: Make more readable

start = {
  'day': 1,
  'month': 1,
  'year': 1901,
  'weekday': 1
}
end = {
  'day': 31,
  'month': 12,
  'year': 2000
}

def is_leap_year(year):
  if year % 100 == 0:
    return year % 400 == 0
  else:
    return year % 4 == 0

def months_in_year(year):
  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap_year(year):
    months[1] += 1
  return months

def is_sunday(days):
  return days % 7 == 0

def counting_sundays():
  days = 0
  sundays = 0
  years = end['year'] - start['year']
  for year in range(years):
    for month in months_in_year(start['year'] + year):
      for day in range(month):
        days += 1
        if day == 0 and is_sunday(days):
          sundays += 1
  return sundays

if __name__ == "__main__":
  print(counting_sundays())