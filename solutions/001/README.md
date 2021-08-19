[My Project Euler Solutions](https://github.com/jwmcgettigan/project-euler-solutions) | [Project Euler Problem Link](https://projecteuler.net/problem=1) | [Problem Overview](https://projecteuler.net/overview=001)

<h2 style="color: #6b4e3d; font-family: 'Segoe UI';">Multiples of 3 or 5</h2>

<h3 style="font-family: 'Consolas';">Problem 1</h3>

<div style="border: 1px solid #999; padding: 0 0.5rem; box-shadow: 5px 5px 5px #999;">
   <p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p>
<p>Find the sum of all the multiples of 3 or 5 below 1000.</p>
</div>



### Defining the problem

**Natural numbers** are all positive integers from 1 to infinity. (1, 2, 3, 4, ..., infinity)

A **multiple** is:

- a number that can be divided by another number without a remainder.
- the product result of one number multiplied by another number.

A **sum** is the total amount resulting from the addition of two or more numbers.



### Analyzing the example

3, 5, 6, 9 = all natural numbers below 10 that are multiples of 3 or 5

3•1 = **3** | 3•2 = **6** | 3•3 = **9** | ~~3•4 = 12~~

5•1 = **5** | ~~5•2 = 10~~ 

We can see above how all of the multiples are found.



### Pseudocode Solution

```pseudocode
/** checks if num is a multiple of the given value */
function is_multiple_of_value(num, value)
	return num % value == 0 // Can num be divided by the value without a remainder?

/** adds all multiples of 3 or 5 below 1000 */
function sum_of_multiples()
	sum = 0
	for (i = 1; i < 1000; i++)
		if(is_multiple_of_value(i, 3) or is_multiple_of_value(i, 5))
			sum = sum + i
	return sum
```

