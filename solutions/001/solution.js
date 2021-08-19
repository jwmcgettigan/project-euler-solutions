const multipleOf = (num, multiple) => num % multiple == 0;
const sumofMultiples = (limit) => {
  let sum = 0;
  for(let x = 0; x < limit; x++) {
    if(multipleOf(x, 3) || multipleOf(x, 5)) {
      sum += x;
    }
  }
  return sum;
}
console.log(sumofMultiples(1000));