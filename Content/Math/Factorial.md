# Factorials

## What is it?

[Wikipedia](https://en.wikipedia.org/wiki/Factorial)

Factorials are a fundamental concept in mathematics, particularly useful in combinatorics, probability, and algebra. The factorial of a non-negative integer represents the product of all positive integers less than or equal to that number. It is denoted by an exclamation mark (n!).

For example, 4! (read as "4 factorial") is calculated as:

        4! = 4 × 3 × 2 × 1 = 24

Let's look at some other factorials:

        3! = 3 x 2 x 1 = 6
        2! = 2 x 1 = 2
        1! = 1

And finally, a special case: 

    0! is defined as 1.

This is because there is exactly 1 permutation (way to arrange) of the number 0.

## Why are factorials important?

Factorials display relationships in numbers. Often used in statistics, factorials can show up in many facets of optimization programming and calculus.

Because we are  a computer school, one important concept here is *memoization*. This is the practice of remembering work we've completed before. For instance, if we wanted to computer 4! and 5!, you may have already noticed from the previous example that 4! = 4 x 3!, and 3! = 3 x 2! and so on. Essentially, we can memoize 4! and use it in the calculation for 5! reducing the number of operations by 4.

A fun factorial to consider is 52! this factorial is the number of different ways a standard deck of cards can be arranged. This number is so large, that when fairly shuffling a deck it's likely that the exact order of those cards has never been done before.

52! is 
80658175170943878571660636856403766975289505440883277824000000000000

If you're curious about how large 52! is, [here's an article](https://drive.google.com/file/d/1E0oCf-0mPG6xvqSSTjTJEr8TJxRc3UPi/view)


## Practice

1. **Question 1: Factorial Calculation**  
   Calculate 4!
 <details>
 <summary>Show Answer</summary>
 **Answer:** 4! = 4 × 3 × 2 × 1 = 24.
 </details>

2. **Question 2: Special Case**  
   What is the value of 0!?
 <details>
 <summary>Show Answer</summary>
 **Answer:** By definition, 0! = 1.
 </details>

3. **Question 3: Factorial Growth**  
   Compare 5! and 6!. Which one is larger and why?
 <details>
 <summary>Show Answer</summary>
 **Answer:** 6! is larger than 5! because 6! = 6 × 5!. If 5! = 120, then 6! = 720.
 </details>
  

