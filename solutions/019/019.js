/**
 * Project Euler - Problem Solution 019
 * Copyright (c) Justin McGettigan. All rights reserved.
 * https://github.com/jwmcgettigan/project-euler-solutions
 */

#TODO: Make more readable

start = {
  day: 1,
  month: 1,
  year: 1901,
  weekday: 1
}
end = {
  day: 31,
  month: 12,
  year: 2000
}

const isLeapYear = (year) => {
  if(year % 100 === 0) {
    return year % 400 === 0;
  } else {
    return year % 4 === 0;
  }
};

const monthsInYear = (year) => {
  const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if(isLeapYear(year)) {
    months[1]++;
  }
  return months;
};

const isSunday = (days) => {
  return days % 7 === 0;
};

const countingSundays = () => {
  let days = 0, sundays = 0;
  const years = end.year - start.year;
  for(let year = 0; year < years; year++) {
    monthsInYear(start.year + year).map(month => {
      for(let day = 0; day < month; day++) {
        days++;
        if(day == 0 && isSunday(days)) {
          sundays++;
        }
      }
    })
  }
  return sundays;
};

console.log(countingSundays());